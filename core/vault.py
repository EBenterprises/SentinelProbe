import json
import os
import time

VAULT_PATH = os.path.expanduser("~/sentinel_probe/data/vault.json")

def rotate_secret():
    # Load existing or create new vault
    vault = {}
    if os.path.exists(VAULT_PATH):
        with open(VAULT_PATH, 'r') as f: vault = json.load(f)
    
    # Generate new versioned key
    new_version = len(vault) + 1
    vault[str(new_version)] = os.urandom(32).hex()
    vault['active'] = str(new_version)
    
    with open(VAULT_PATH, 'w') as f: json.dump(vault, f)
    print(f"[+] Secret rotated to version {new_version}")

if __name__ == "__main__":
    rotate_secret()
