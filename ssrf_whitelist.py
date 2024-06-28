from flask import Flask, request
from urllib.parse import urlparse
import requests
from uuid import uuid4

app = Flask(__name__)

WHITELIST = [
    'webhook.site',
    None
]

@app.route('/')
def ssrf_demo():
    return 'SSRF Demo'

@app.route('/fetch', methods=['GET', 'POST'])
def fetch_url():
    if request.method == 'GET':
        url = request.args.get('url')
    elif request.method == 'POST':
        url = request.form.get('url')

    if not url:
        return 'Please provide a URL', 400

    # Extract the domain from the URL
    try:
        parsed_url = urlparse(url)
        domain = parsed_url.hostname
    except Exception as e:
        return f'Invalid URL: {e}', 400

    # Check if the domain is in the whitelist
    if domain not in WHITELIST:
        return f'{domain} is not allowed', 403

    try:
        content = requests.get(url=url).text
        return content
    except Exception as e:
        return f'Unable to fetch URL: {e}', 500

@app.route('/admin', methods = ['GET', 'POST'])
def admin_route():
    return f'flag: {uuid4()}'

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000, debug=True)
