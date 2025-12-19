# Smart Poultry Farm – Edge AI & Automation Platform

## Overview

This project is a **large-scale Smart Poultry Farm platform** designed for layers farming.
It combines **IoT simulation, edge computing, automation rules, and AI-ready architecture** to monitor and control poultry farm operations in real time.

The system is built **offline-first**, with a **local server** handling all critical operations and optional **cloud synchronization** for analytics and long-term storage.

Although the current setup uses **software simulation**, the architecture is identical to a real deployment using ESP32 devices, cameras, and edge Mini-PCs.

---

## Key Features

* Environmental monitoring (temperature, humidity, water flow)
* MQTT-based device communication (sensor → server → device)
* Rule-based automation engine (no-code rule changes)
* Web dashboard for managing automation rules
* Edge-ready architecture for computer vision and AI
* Scales from 10 birds to thousands without redesign

---

## System Architecture

```
[ Sensor Simulator ] ──MQTT──▶
                        [ Local Server (FastAPI) ]
                             ├── Rule Engine
                             ├── Database (PostgreSQL)
                             ├── MQTT Broker
                             └── Automation Logic
                                   │
                                   └──MQTT──▶ [ Device Simulator ]

[ Web Dashboard ] ──HTTP──▶ [ FastAPI API ]
```

---

## Tech Stack

### Backend

* Python
* FastAPI
* PostgreSQL
* MQTT (Mosquitto)
* SQLAlchemy

### Frontend

* React
* REST APIs

### Messaging

* MQTT (sensor and device communication)

### Simulation

* Python-based ESP32 sensor simulator
* Python-based ESP32 device simulator

---

## Project Structure

```
smart_poultry/
├── app/
│   ├── api/            # FastAPI routes
│   ├── models/         # Database models
│   ├── mqtt/           # MQTT client & handlers
│   ├── services/       # Automation & rule engine
│   ├── main.py         # Server entry point
│   └── database.py
│
├── simulators/
│   ├── esp32_sensor_sim.py
│   └── esp32_device_sim.py
│
├── webview/
│   └── (React frontend)
│
├── requirements.txt
└── README.md
```

---

## Prerequisites

Ensure the following are installed:

* Python 3.9+
* Node.js 18+
* PostgreSQL
* MQTT Broker (Mosquitto)

---

## Backend Setup (Local Server)

### 1. Create Virtual Environment

```bash
python -m venv venv
source venv/bin/activate  # Windows: venv\Scripts\activate
```

### 2. Install Dependencies

```bash
pip install -r requirements.txt
```

### 3. Start PostgreSQL

Create a database named:

```
smart_farm
```

Update database credentials in `app/database.py` if required.

---

### 4. Start MQTT Broker

```bash
mosquitto
```

---

### 5. Run the Server

```bash
uvicorn app.main:app --reload
```

Server will be available at:

* API: `http://127.0.0.1:8000`
* API Docs: `http://127.0.0.1:8000/docs`

---

## Start Simulated Devices

### 1. Start ESP32 Device Simulator (Actuators)

```bash
python simulators/esp32_device_sim.py
```

This simulates fans, heaters, feeders, and lights.

---

### 2. Start ESP32 Sensor Simulator

```bash
python simulators/esp32_sensor_sim.py
```

This publishes temperature, humidity, and water data to MQTT.

---

## Frontend Dashboard Setup

### 1. Navigate to Dashboard Folder

```bash
cd smart-poultry-dashboard
```

### 2. Install Dependencies

```bash
npm install
```

### 3. Start Dashboard

```bash
npm run dev
```

Dashboard will be available at:

```
http://localhost:5173
```

---

## Using the System

### 1. Create Automation Rules

* Open the dashboard
* Add rules such as:

  * If temperature > 30 → Fan ON
  * If temperature < 26 → Heater ON

### 2. Observe Automation

* Sensor simulator sends data
* Server evaluates rules
* Commands are sent to device simulator
* Device state updates are logged

---

## Rule Engine Logic

Rules are **data-driven**, not hard-coded.

Each rule defines:

* Pen (or global)
* Sensor type
* Condition
* Threshold
* Device
* Action
* Priority
* Enabled/Disabled state

Rules can be modified live without restarting the system.

---

## Scalability

This system is designed to scale:

| Scale        | Changes Required      |
| ------------ | --------------------- |
| 10 birds     | Simulation only       |
| 100 birds    | Add cameras & sensors |
| 1,000+ birds | Multiple edge nodes   |
| Multi-farm   | Cloud sync enabled    |

No architectural redesign is required.

---

## Future Extensions

* Computer vision (YOLO + tracking)
* Individual bird health scoring
* AI-based disease risk detection
* Cloud dashboards and analytics
* Mobile app for farm operators

---

## Purpose

This project is intended as:

* A **production-grade smart poultry platform**
* A **foundation for agri-tech startups**
* A **research and demonstration system**
* A **scalable automation and AI farm system**

---

## License

MIT License
