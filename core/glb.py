from flask import Flask, redirect, request
import requests

app = Flask(__name__)

def get_optimized_node():
    with open("/home/user/sentinel_probe/data/nodes.list", "r") as f:
        nodes = [line.strip() for line in f.readlines()]
    for node in nodes:
        try:
            if requests.get(f"http://{node}:5001/task/claim", timeout=0.5).status_code == 200:
                return node
        except: continue
    return nodes[0]

@app.route('/', defaults={'path': ''})
@app.route('/<path:path>')
def proxy(path):
    best = get_optimized_node()
    return redirect(f"http://{best}:5001/{path}")

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=80)
