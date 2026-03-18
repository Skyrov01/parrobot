# 🦜 Open HRI Parrot Platform

An open-source, low-cost Human-Robot Interaction (HRI) platform designed for education, participatory design, and robotics workshops with children.

The platform combines:
- ROS2-based robot control
- HTTP API for interaction
- Web-based interface (Papegaai)
- EduBlocks-compatible programming

---

## ✨ Features

- 🧠 ROS2 architecture with modular nodes (control, sound, HTTP server)
- 🌐 HTTP bridge for simple interaction via Python requests
- 🎮 Interactive web UI for manual control and behavior execution
- 🧒 Educational integration with EduBlocks (block-based programming)
- 🔊 Sound interaction and multimodal feedback
- 🧩 Designed for workshops and participatory design activities

---

## 🚀 Quick Start

### 1. Setup the Robot (Raspberry Pi)

Install Ubuntu 24.04 and ROS2:

- Flash Ubuntu 24.04 LTS (64-bit)
- Boot Raspberry Pi and create a user
- Install ROS2 (Jazzy recommended)

👉 Full setup instructions:  
See **setup_parrots.pdf** 

Install dependencies:

```bash
sudo apt install -y \
  python3-pip python3-venv python3-dev build-essential \
  python3-flask python3-flask-cors python3-requests \
  python3-gpiozero \
  git curl wget tmux htop vim gparted net-tools \
  ros-jazzy-rmw-fastrtps-cpp ros-jazzy-rmw-cyclonedds-cpp
