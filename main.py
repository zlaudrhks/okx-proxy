from flask import Flask, request, jsonify
from flask_cors import CORS
import requests
import os

app = Flask(__name__)
CORS(app)

@app.route('/')
def index():
    return '✅ OKX Proxy Server is running'

@app.route('/okx/<path:endpoint>')
def okx_proxy(endpoint):
    base_url = 'https://www.okx.com/api/v5/'
    target_url = base_url + endpoint

    try:
        headers = {
            'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64)'
        }
        resp = requests.get(target_url, headers=headers, timeout=10)
        resp.raise_for_status()
        return jsonify(resp.json())
    except Exception as e:
        return jsonify({'error': str(e)}), 500

if __name__ == '__main__':
    port = int(os.environ.get("PORT", 10000))
    app.run(host='0.0.0.0', port=port)