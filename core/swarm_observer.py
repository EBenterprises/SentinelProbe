import statistics

def analyze_swarm_health(peer_metrics):
    if len(peer_metrics) < 3: return []
    mean = statistics.mean(peer_metrics)
    stdev = statistics.stdev(peer_metrics)
    return [m for m in peer_metrics if abs(m - mean) > (3 * stdev)]

def propagate_anomaly_alert(anomalous_node):
    print(f"[CRITICAL] Swarm consensus: Node {anomalous_node} is behaving anomalously.")
