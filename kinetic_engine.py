import sys, hashlib, time
def render_pulse(node):
    # Obsidian-Teal Visual Heartbeat
    print(f"\033[1;36m[KINETIC-MESH]\033[0m Pulse -> {node}")
    time.sleep(0.05)

def route(path):
    return hashlib.sha256(path.encode()).hexdigest()[:12]

if __name__ == "__main__":
    path, op = sys.argv[1], sys.argv[2]
    node = route(path)
    render_pulse(node)
    print(f"\033[1;33m[EXEC]\033[0m Path: {path} | Hash: {node} | Op: {op}")
