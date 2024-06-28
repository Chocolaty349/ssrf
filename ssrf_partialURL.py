from flask import Flask, request
from requests import get

app = Flask('__main__')
SITE_NAME = 'https://google.com'

@app.route('/')
def proxy():
  path = request.args.get('path')
  return get(f'{SITE_NAME}{path}').content

if __name__ == "__main__":
    app.run(threaded=False)