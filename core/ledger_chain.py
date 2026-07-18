import hashlib
import json
import os

LEDGER_PATH = os.path.expanduser("~/sentinel_probe/data/mesh.ledger")

def get_block_hash(data):
    return hashlib.sha256(json.dumps(data, sort_keys=True).encode()).hexdigest()

def finalize_block():
    if not os.path.exists(LEDGER_PATH): return
    with open(LEDGER_PATH, 'r') as f:
        data = json.load(f)
    block_hash = get_block_hash(data)
    with open(LEDGER_PATH + ".hash", 'w') as f:
        f.write(block_hash)
    return block_hash
