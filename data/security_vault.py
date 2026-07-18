import hashlib

def hash_key(key: str):
    return hashlib.sha256(key.encode()).hexdigest()

def verify_access(provided_key, stored_hash):
    return hash_key(provided_key) == stored_hash
