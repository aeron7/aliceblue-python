import requests

# config
web_url = 'https://ant.aliceblueonline.com'


class Client(object):
    base_url = web_url
    def __init__(self, access_token):
        self.headers = {
            'Accept': 'application/json',
            'Authorization': f'Bearer {access_token}'
        }

    def _send_request(self, method='get', endpoint='', params={}):
        r = requests.request(
            method=method,
            headers=self.headers,
            url=f'{Client.base_url}{endpoint}',
            params=params)

        if r.status_code == 200:
            r_json = r.json()
            try:
                return r_json['data']
            except KeyError as e:
                print(e)
                return r_json
        
        print(r)
        print(r.json())

    def fetch_profile(self):
        endpoint = '/api/v2/profile'
        data = self._send_request(endpoint=endpoint)
        return data