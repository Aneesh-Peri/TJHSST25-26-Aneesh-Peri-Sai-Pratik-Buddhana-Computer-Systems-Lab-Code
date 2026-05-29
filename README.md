# Solar Tracker Control System

A Raspberry Pi–powered solar tracking system with a web dashboard for controlling and monitoring stepper motors used to adjust solar panel positioning.

---

## Project Overview

This project combines:

* Raspberry Pi GPIO motor control
* TMC2209 stepper motor drivers
* NEMA 17 stepper motors
* Flask-based web interface
* Real-time dashboard control

The system allows solar panel movement control through a website hosted on the Raspberry Pi.

---

## Hardware Requirements

* Raspberry Pi (tested on Raspberry Pi 4)
* 2 × NEMA 17 Stepper Motors
* 2 × TMC2209 Stepper Drivers
* External Power Supply
* Breadboard / Jumper Wires
* Solar panel mounting system

---

## Software Requirements

Install Python 3 if not already installed.

Required libraries:

```bash
pip install flask RPi.GPIO requests
```

If using Raspberry Pi OS:

```bash
sudo apt update
sudo apt install python3-pip
```

---

## Project File Structure

```text
Main Code/
│
├── Motor Movement/
│   └── motor.py
│
└── website/
    ├── main.py
    │
    ├── static/
    │   └── style.css
    │
    └── templates/
        └── index.html
```

---

## File Descriptions

### Motor Movement/motor.py

Contains GPIO setup and stepper motor movement logic.

Functions include:

* GPIO initialization
* Stepper driver enable/disable
* Direction control
* Motor rotation functions
* Independent motor movement

Run using:

```bash
python3 motor.py
```

---

### website/main.py

Runs the Flask web server.

Responsibilities:

* Hosts website dashboard
* Receives user commands
* Sends commands to motor control functions
* Handles backend logic

Run using:

```bash
python3 main.py
```

---

### website/templates/index.html

Main dashboard webpage.

Provides:

* User interface controls
* Buttons / sliders / status display
* Sends requests to Flask backend

---

### website/static/style.css

Website styling and layout configuration.

---

## Running the Project

Navigate to the project directory:

```bash
cd project-folder
```

Start the Flask server:

```bash
python3 main.py
```

Open a browser and visit:

```text
http://<raspberry-pi-ip-address>:5000
```

To directly test motor controls:

```bash
python3 motor.py
```
