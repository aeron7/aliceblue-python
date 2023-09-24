Deprecated: [Unofficed](https://www.unofficed.com/) is no longer a partner of Aliceblue. We will not provide any support, and no further updates or code maintenance will be done.

## This program is written in Flask. 

- Tested with Python 3.6.7
- Recommended Python 3.6 or higher version
- Needs to run with sudo as redirect url is set to run on port 80

## Support of Coding:
- Support is limited to the people who are under subbrokership of Unofficed. For any help, raise a ticket at https://forum.unofficed.com/
- Otherwise, Please contact Aliceblue customer care. It is not possible to reply every Aliceblue customer.

## Install packages:

Download all the files from here and install all required python packages using command
`pip3 install -r requirements.txt`

## Usage:

- Update the variables `client_id` and `client_secret` config in server.py
```
# config
client_id = 'your_app_id_here'
client_secret = 'your_app_secret_here'
```
- Now run the Flask program using command
`sudo python3 server.py`

Now the app is ready! Open https://127.0.0.1/getcode/ and get started.
