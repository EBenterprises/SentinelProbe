import psutil # Ensure this is pre-installed or use loadavg
import requests

def get_health():
    return psutil.cpu_percent(interval=1)

def rebalance_mesh():
    # Fetch health stats from all peers
    nodes = [line.strip() for line in open("/home/user/sentinel_probe/data/nodes.list")]
    for node in nodes:
        try:
            health = requests.get(f"http://{node}:5001/status").json()
            if health['load'] > 80:
                # Offload tasks to lower-utilization peers
                pass
        except: continue
