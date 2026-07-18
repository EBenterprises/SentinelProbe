import time
import os

NODE_REGISTRY = "~/sentinel_probe/data/nodes.list"
TIMEOUT_LIMIT = 300 # Seconds

def check_node_health(last_seen_timestamp):
    if (time.time() - last_seen_timestamp) > TIMEOUT_LIMIT:
        return False
    return True

def eject_node(node_ip):
    with open(NODE_REGISTRY, "r") as f:
        lines = f.readlines()
    with open(NODE_REGISTRY, "w") as f:
        for line in lines:
            if node_ip not in line:
                f.write(line)
    print(f"[!] Node {node_ip} ejected from mesh.")
