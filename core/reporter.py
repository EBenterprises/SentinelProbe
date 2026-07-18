import requests
import os

def broadcast_vulns():
    ledger = open(os.path.expanduser("~/sentinel_probe/data/mesh.ledger")).read()
    nodes = [line.strip() for line in open(os.path.expanduser("~/sentinel_probe/data/nodes.list")).readlines()]
    for node in nodes:
        requests.post(f"http://{node}:5001/ledger/update", json={"vuln_report": ledger})
