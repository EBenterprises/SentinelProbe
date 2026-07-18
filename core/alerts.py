import requests

def send_alert(message):
    # Logic to trigger notification on state change
    print(f"[ALERT] {message}")

def monitor_state(current_ports, previous_ports):
    if current_ports != previous_ports:
        send_alert(f"Port state drift detected: {current_ports}")
