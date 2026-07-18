import json
import os
from cryptography.fernet import Fernet

KEY = Fernet.generate_key()
CIPHER = Fernet(KEY)

def write_memory(key, val):
    data = {key: val}
    encrypted = CIPHER.encrypt(json.dumps(data).encode())
    with open(os.path.expanduser("~/sentinel_probe/data/shared.mem"), "ab") as f:
        f.write(encrypted + b"\n")

def read_memory():
    with open(os.path.expanduser("~/sentinel_probe/data/shared.mem"), "rb") as f:
        return [CIPHER.decrypt(line.strip()) for line in f.readlines()]
