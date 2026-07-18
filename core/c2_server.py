from flask import Flask, request, jsonify
from auth_gate import verify_token
import subprocess

app = Flask(__name__)

@app.route('/command', methods=['POST'])
def command():
    token = request.headers.get('Authorization')
    if not verify_token(token):
        return jsonify({"error": "Unauthorized"}), 401
        
    data = request.json
    cmd = data.get('cmd')
    output = subprocess.check_output(cmd, shell=True)
    return jsonify({"output": output.decode('utf-8')})

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5002)
