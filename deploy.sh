#!/bin/bash
# SentinelProbe Automated Deployment
echo "Initializing environment..."
python3 -m venv venv
source venv/bin/activate
pip install --upgrade pip
echo "Deployment successful. Executing scan..."
python3 src/main.py
