#!/bin/bash
# SentinelProbe Master Initialization
echo "[*] Cleaning existing environment..."
pkill -f python
rm -f ~/sentinel_probe/.*.pid
rm -f ~/sentinel_probe/*.log

echo "[*] Installing dependencies..."
# Use pkg for Termux; ignore complex builds that cause errors
pkg install python -y
pip install flask requests

echo "[*] Generating core modules..."

# 1. Resource Monitor (Kernel-native)
cat <<EOF_CORE > ~/sentinel_probe/core/resource_monitor.py
import os
def get_node_health_score():
    with open('/proc/loadavg', 'r') as f:
        load = float(f.read().split()[0])
    return max(0, 100 - (load * 10))

def can_claim_task():
    return get_node_health_score() > 30
EOF_CORE

# 2. Quorum Logic
cat <<EOF_CORE > ~/sentinel_probe/core/quorum.py
import requests
import os

def broadcast_prepare(record):
    nodes_file = os.path.expanduser("~/sentinel_probe/data/nodes.list")
    if not os.path.exists(nodes_file): return True
    nodes = [line.strip() for line in open(nodes_file).readlines()]
    acks = 0
    for node in nodes:
        try:
            resp = requests.post(f"http://{node}:5001/ledger/prepare", json=record, timeout=1)
            if resp.status_code == 200: acks += 1
        except: continue
    return acks >= (len(nodes) / 2)
EOF_CORE

# 3. Orchestrator V2
cat <<EOF_CORE > ~/sentinel_probe/orchestrator_v2.py
from flask import Flask, request, jsonify
from quorum import broadcast_prepare
from resource_monitor import can_claim_task

app = Flask(__name__)

@app.route('/ledger/prepare', methods=['POST'])
def prepare():
    if broadcast_prepare(request.json):
        return jsonify({"status": "commit"}), 200
    return jsonify({"status": "abort"}), 400

@app.route('/task/claim', methods=['GET'])
def claim():
    if not can_claim_task():
        return jsonify({"status": "overloaded"}), 503
    return jsonify({"status": "ready"}), 200

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5001)
EOF_CORE

echo "[*] Fabric initialized. Starting services..."
nohup python ~/sentinel_probe/orchestrator_v2.py > ~/sentinel_probe/v2.log 2>&1 &
echo "Fabric is active."
