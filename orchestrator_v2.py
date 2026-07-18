from flask import Flask, request, jsonify
from quorum import broadcast_prepare
from resource_monitor import can_claim_task

app = Flask(__name__)

@app.route('/ledger/prepare', methods=['POST'])
def prepare():
    if broadcast_prepare(request.json):
        return jsonify({"status": "commit"}), 200
    return jsonify({"status": "abort"}), 400

@app.route('/task/claim', methods=['GET'])
def claim():
    if not can_claim_task():
        return jsonify({"status": "overloaded"}), 503
    return jsonify({"status": "ready"}), 200

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5001)
