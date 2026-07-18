import socket

def scan_port(target, port):
    try:
        with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
            s.settimeout(0.5)
            result = s.connect_ex((target, port))
            return result == 0
    except Exception:
        return False

def run_recon(target, ports):
    print(f"[*] Starting scan on {target}...")
    open_ports = [p for p in ports if scan_port(target, p)]
    return open_ports
