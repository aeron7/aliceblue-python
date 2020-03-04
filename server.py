import os
import threading
from requests_oauthlib import OAuth2Session
from flask import Flask, request, redirect
from client import web_url
from example import data_from_resource_server

# to make oauth2 work with http
os.environ['OAUTHLIB_INSECURE_TRANSPORT'] = '1'


# config
client_id = 'your_app_id_here'
client_secret = 'your_app_secret_here'
redirect_uri = 'http://127.0.0.1/'
authorization_base_url = f'{web_url}/oauth2/auth'
token_url = f'{web_url}/oauth2/token'
scope=['orders']
# state='https://www.google.com'

# creating instance of Flask
app = Flask(__name__)


# access token
access_token = None


@app.route('/getcode')
def get_authorization_url():
    oauth = OAuth2Session(client_id, redirect_uri=redirect_uri, scope=scope)
    authorization_url, _state = oauth.authorization_url(authorization_base_url, access_type="authorization_code")
    print('authorization_url')
    print(authorization_url)
    return redirect(authorization_url)


@app.route('/')
def callback():
    global access_token
    oauth = OAuth2Session(client_id, redirect_uri=redirect_uri, scope=scope)
    token = oauth.fetch_token(token_url, authorization_response=request.url, client_secret=client_secret)
    access_token = token['access_token']
    print('access token is:', access_token)

    ## we will be shutting down the server after getting access_token
    ## the thread created here is copied in if __name__ == '__main__' block
    ## and will run after closing the server

    # th = threading.Thread(target=data_from_resource_server, args=(access_token,))
    # th.start()

    func = request.environ.get('werkzeug.server.shutdown')
    if func:
        print('stoping server')
        func()


    return 'see terminal for logs'


if __name__ == '__main__':
    app.secret_key = 'example'
    app.env = 'development'
    print()
    print('Open this url in browser:', 'http://127.0.0.1/getcode', end='\n\n')

    app.run(host='127.0.0.1', port='80')

    print('server stopped')

    ## got access_token, closed the server, now running ray integration code
    if access_token:
        th = threading.Thread(target=data_from_resource_server, args=(access_token,))
        th.start()
