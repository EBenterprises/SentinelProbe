import requests
import json
import os

def broadcast_prepare(record):
    nodes_file = os.path.expanduser("~/sentinel_probe/data/nodes.list")
    if not os.path.exists(nodes_file): return True
    
    with open(nodes_file, 'r') as f:
        nodes = [line.strip() for line in f.readlines()]
        
    acks = 0
    for node in nodes:
        try:
            resp = requests.post(f"http://{node}:5001/ledger/prepare", json=record, timeout=2)
            if resp.status_code == 200: acks += 1
        except: continue
        
    return acks >= (len(nodes) // 2) + 1
