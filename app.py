from flask import Flask, request, jsonify
import requests

app = Flask(__name__)

@app.route('/')
def home():
    return '✅ OKX Proxy Server is Running'

@app.route('/okx', methods=['GET'])
def okx_proxy():
    path = request.args.get('path', '')
    if not path.startswith('/'):
        path = '/' + path
    okx_url = f'https://www.okx.com{path}'
    
    try:
        response = requests.get(okx_url, headers={
            'User-Agent': 'Mozilla/5.0'
        })
        response.raise_for_status()
        return jsonify(response.json())
    except requests.exceptions.RequestException as e:
        return jsonify({'error': str(e)}), 500

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=10000)
