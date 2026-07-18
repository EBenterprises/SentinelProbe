import sys, hashlib
def resolve_node(path):
    # Deterministic mapping for infinite branching
    return hashlib.md5(path.encode()).hexdigest()[:8]

def execute(path, action, payload):
    node_id = resolve_node(path)
    return f"FRACTAL_MESH | Path: {path} | NodeID: {node_id} | OP: {action} | STATUS: ACTIVE"

if __name__ == "__main__":
    print(execute(sys.argv[1], sys.argv[2], sys.argv[3]))
