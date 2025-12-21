from logging.config import fileConfig
from sqlalchemy import engine_from_config, pool
from alembic import context

import sys
from pathlib import Path

BASE_DIR = Path(__file__).resolve().parents[1]
sys.path.append(str(BASE_DIR))

from app.database import Base, engine
from app.models.bird import Bird
from app.models.device import Device
from app.models.device_command import DeviceCommand
from app.models.farm import Farm
from app.models.pen import Pen
from app.models.refresh_token import RefreshToken
from app.models.rule import Rule
from app.models.sensor import Sensor
from app.models.sensor_reading import SensorReading
from app.models.vision_event import VisionEvent
from app.models.user import User

Base.metadata.create_all(bind=engine)
target_metadata = Base.metadata
