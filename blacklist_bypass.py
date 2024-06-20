from flask import Flask, request
import requests
from urllib.parse import urlparse
from uuid import uuid4
from urllib.request import urlopen

app = Flask(__name__)

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
        return 'Please provide a URL'
    blacklist = ['localhost', '127.0.0.1', 'admin']
    for item in blacklist:
        if item in url:
            return 'not allowed'
    try:
        with urlopen(url) as response:
            content = response.read().decode('utf-8')
        return content
    except:
        return 'Unable to fetch URL'

@app.route('/admin', methods = ['GET', 'POST'])
def admin_route():
    return f'flag: {uuid4()}'

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000, debug=True)
