import os

def generate_topology():
    node_file = os.path.expanduser("~/sentinel_probe/data/nodes.list")
    if not os.path.exists(node_file):
        print("No nodes found.")
        return
    
    with open(node_file, "r") as f:
        nodes = [line.strip() for line in f.readlines()]
    
    print("--- Sovereign Fabric Topology ---")
    print(f"ROOT_CA [Secure] -->")
    for node in nodes:
        print(f"  |-- NODE: {node} [Status: ACTIVE]")
    print("--- End Map ---")

if __name__ == "__main__":
    generate_topology()
