import time
from datetime import datetime

def log_metrics(data):
    with open('~/sentinel_probe/fabric_metrics.log', 'a') as f:
        timestamp = datetime.now().strftime('%Y-%m-%d %H:%M:%S')
        f.write(f"[{timestamp}] {data}\n")
