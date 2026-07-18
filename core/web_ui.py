from flask import Flask, render_template_string
import os

app = Flask(__name__)

HTML_TEMPLATE = """
<html><body><h1>Sentinel Probe Alerts</h1>
<pre>{{ logs }}</pre>
</body></html>
"""

@app.route('/')
def index():
    logs = open(os.path.expanduser("~/sentinel_probe/fabric_metrics.log")).read()
    return render_template_string(HTML_TEMPLATE, logs=logs)

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5003)
