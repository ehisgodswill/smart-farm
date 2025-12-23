# app/mqtt/client.py
import json
import logging
from typing import Optional
import paho.mqtt.client as mqtt
from sqlalchemy.orm import Session

from app.database import SessionLocal
from app.mqtt.vision_handler import handle_vision_message
from app.config import settings

logger = logging.getLogger(__name__)

mqtt_client: Optional[mqtt.Client] = None


def on_connect(client: mqtt.Client, userdata, flags, rc):
    """Callback when MQTT client connects"""
    if rc == 0:
        logger.info("Connected to MQTT broker")
        # Subscribe to topics
        client.subscribe("vision/#")
        client.subscribe("sensors/#")
        logger.info("Subscribed to topics: vision/#, sensors/#")
    else:
        logger.error(f"Failed to connect to MQTT broker, return code: {rc}")


def on_disconnect(client: mqtt.Client, userdata, rc):
    """Callback when MQTT client disconnects"""
    if rc != 0:
        logger.warning(f"Unexpected MQTT disconnect: {rc}")
    else:
        logger.info("Disconnected from MQTT broker")


def on_message(client: mqtt.Client, userdata, msg: mqtt.MQTTMessage):
    """Callback when a message is received"""
    topic = msg.topic
    logger.debug(f"Received message on topic: {topic}")
    
    db: Session = SessionLocal()
    try:
        # Decode payload
        payload = json.loads(msg.payload.decode())
        logger.debug(f"Payload: {payload}")
        
        # Route to appropriate handler
        if topic.startswith("vision/"):
            handle_vision_message(db, topic, payload)
        elif topic.startswith("sensors/"):
            # Handle sensor messages
            logger.info(f"Sensor message received: {topic}")
            # handle_sensor_message(db, topic, payload)
        else:
            logger.warning(f"No handler for topic: {topic}")
            
    except json.JSONDecodeError as e:
        logger.error(f"Failed to decode JSON from topic {topic}: {e}")
    except Exception as e:
        logger.error(f"Error processing message from {topic}: {e}", exc_info=True)
    finally:
        db.close()


def start_mqtt():
    """Initialize and start MQTT client"""
    global mqtt_client
    
    try:
        mqtt_client = mqtt.Client(client_id="smart_poultry_server")
        mqtt_client.on_connect = on_connect
        mqtt_client.on_disconnect = on_disconnect
        mqtt_client.on_message = on_message
        
        # Set credentials if needed
        if hasattr(settings, 'MQTT_USERNAME') and settings.MQTT_USERNAME:
            mqtt_client.username_pw_set(
                settings.MQTT_USERNAME,
                settings.MQTT_PASSWORD
            )
        
        # Connect to broker
        mqtt_host = getattr(settings, 'MQTT_HOST', 'localhost')
        mqtt_port = getattr(settings, 'MQTT_PORT', 1883)
        
        logger.info(f"Connecting to MQTT broker at {mqtt_host}:{mqtt_port}")
        mqtt_client.connect(mqtt_host, mqtt_port, keepalive=60)
        
        # Start loop in background thread
        mqtt_client.loop_start()
        logger.info("MQTT client started successfully")
        
    except Exception as e:
        logger.error(f"Failed to start MQTT client: {e}", exc_info=True)


def stop_mqtt():
    """Stop MQTT client gracefully"""
    global mqtt_client
    
    if mqtt_client:
        logger.info("Stopping MQTT client")
        mqtt_client.loop_stop()
        mqtt_client.disconnect()
        mqtt_client = None
        logger.info("MQTT client stopped")