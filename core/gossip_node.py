import socket
import threading
import random
import time
import hashlib
import os

def get_ledger_hash():
    # Returns current hash of the mesh.ledger
    with open(os.path.expanduser("~/sentinel_probe/data/mesh.ledger"), "rb") as f:
        return hashlib.sha256(f.read()).hexdigest()

def gossip():
    nodes = [line.strip() for line in open(os.path.expanduser("~/sentinel_probe/data/nodes.list"))]
    while True:
        target = random.choice(nodes)
        try:
            with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
                s.connect((target, 5002))
                s.sendall(get_ledger_hash().encode())
        except: pass
        time.sleep(10) # Gossip interval

threading.Thread(target=gossip, daemon=True).start()
