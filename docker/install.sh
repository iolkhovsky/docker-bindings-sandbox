#!/bin/bash

apt update && apt upgrade
apt install -y build-essential gdb cmake
apt install -y python3 python3-pip python3-venv
apt install -y libgl1-mesa-glx
apt install -y libboost-all-dev libpython3-dev
pip3 install -r requirements.txt