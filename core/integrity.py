import hashlib
import os

def generate_ledger_hash():
    ledger_path = os.path.expanduser("~/sentinel_probe/data/mesh.ledger")
    if not os.path.exists(ledger_path):
        return None
    hasher = hashlib.sha256()
    with open(ledger_path, 'rb') as f:
        while chunk := f.read(8192):
            hasher.update(chunk)
    return hasher.hexdigest()
