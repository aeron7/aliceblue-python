import threading
from client import Client
from ws_client import handle_streams


# example function to show use case of access token
# it fetches client profile from REST api
# and also logs market data from websockets
def data_from_resource_server(access_token):
    user = Client(access_token)
    profile = user.fetch_profile()
    print('profile', profile)
    th = threading.Thread(target=handle_streams, args=(access_token,))
    th.start()
    # handle_streams(access_token)
