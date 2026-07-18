import subprocess
import time
import os

def check_fabric_health():
    # Verify core processes
    required_services = ["orchestrator.py", "gossip_node.py", "dashboard_server.py"]
    for service in required_services:
        result = subprocess.run(["pgrep", "-f", service], capture_output=True)
        if result.returncode != 0:
            print(f"[!] {service} down. Restarting...")
            subprocess.run(["systemctl", "restart", "sovereign_fabric.service"])

def main():
    while True:
        check_fabric_health()
        time.sleep(30)

if __name__ == "__main__":
    main()
