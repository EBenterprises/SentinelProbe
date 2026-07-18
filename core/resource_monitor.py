import os
def get_node_health_score():
    with open('/proc/loadavg', 'r') as f:
        load = float(f.read().split()[0])
    return max(0, 100 - (load * 10))

def can_claim_task():
    return get_node_health_score() > 30
