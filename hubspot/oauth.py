# -*- coding: utf-8 -*-
"""...
"""
import requests
from . import constants
from os import environ


# Get OAuth 2.0 Access Token and Refresh Tokens
def get_oauth_token():
    headers = constants.oauth_header
    client_id = environ['client_id']
    client_secret = environ['client_secret']
    redir = 'https://www.example.com/'
    code = environ['code']
    data = f'grant_type=authorization_code&client_id={client_id}&client_secret={client_secret}&redirect_uri={redir}&code={code}'
    response = requests.request('POST', url=constants.OAUTH_TOKEN_URL, json=data, headers=headers)
    if response.status_code == 400:
        pass
    return


def main():

    return


if __name__ == '__main__':
    main()
    print('main - done')