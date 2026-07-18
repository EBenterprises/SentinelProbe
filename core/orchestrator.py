from flask import Flask, request, jsonify
from quorum import verify_and_commit
from ledger_chain import finalize_block

app = Flask(__name__)

@app.route('/ledger/prepare', methods=['POST'])
def prepare():
    # Enforce strict consistency
    if verify_and_commit(request.json):
        # Trigger cryptographic snaphot
        finalize_block()
        return jsonify({"status": "committed"}), 200
    return jsonify({"status": "abort"}), 400

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5001)

@app.route('/ledger/verify', methods=['POST'])
def verify_ledger():
    from ledger_chain import generate_ledger_hash
    incoming_hash = request.form.get('hash')
    local_hash = generate_ledger_hash()
    if incoming_hash != local_hash:
        return jsonify({"status": "tamper_detected"}), 403
    return jsonify({"status": "verified"}), 200
