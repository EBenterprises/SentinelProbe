from flask import Flask, render_template_string
import os
import subprocess

app = Flask(__name__)

@app.route('/')
def dashboard():
    # Fetch logs and status for the UI
    status = subprocess.check_output(['ps', 'aux']).decode('utf-8')
    with open('/home/user/sentinel_probe/ledger_sync.log', 'r') as f:
        logs = f.readlines()[-20:]
    
    html = """
    <html>
        <body style="background:#0a0a0a; color:#0f0; font-family:monospace;">
            <h1>Sovereign Fabric Control Plane</h1>
            <h3>Active Processes</h3>
            <pre>{{ status }}</pre>
            <h3>Recent Ledger Sync Logs</h3>
            <pre>{{ ''.join(logs) }}</pre>
        </body>
    </html>
    """
    return render_template_string(html, status=status, logs=logs)

if __name__ == "__main__":
    app.run(host='0.0.0.0', port=8080)
