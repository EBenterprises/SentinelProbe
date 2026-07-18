import subprocess
import os

def block_ip(ip):
    # Applying iptables rules dynamically
    print(f"[!] Remediation: Blocking {ip}")
    subprocess.run(["iptables", "-A", "INPUT", "-s", ip, "-j", "DROP"], sudo=True)

def auto_remediate(vulnerability_log):
    if "Open Port" in vulnerability_log:
        # Extract IP and apply block
        block_ip("127.0.0.1")
