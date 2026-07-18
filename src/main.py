from scanner import run_recon

if __name__ == "__main__":
    target = "127.0.0.1"
    ports = [21, 22, 80, 443, 8080]
    results = run_recon(target, ports)
    print(f"[+] Open ports found: {results}")
