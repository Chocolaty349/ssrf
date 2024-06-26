from flask import Flask, request
import requests
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

    try:
        with urlopen(url) as response:
            content = response.read().decode('utf-8')
        return content
    except:
        return 'Unable to fetch URL'

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000, debug=True)