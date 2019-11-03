# -*- coding: utf-8 -*-
"""...
"""
import requests
from hubspot import constants
from os import environ


# Get OAuth 2.0 Access Token and Refresh Tokens
def get_oauth_token():
    headers = constants.oauth_header
    client_id = environ['client_id']
    client_secret = environ['client_secret']
    redir = environ['redirect_uri']
    code = environ['code']
    data = f'grant_type=authorization_code&client_id={client_id}&client_secret={client_secret}&redirect_uri={redir}&code={code}'
    response = requests.request('POST', url=constants.OAUTH_TOKEN_URL, data=data, headers=headers)
    if response.status_code == 400:
        print('400')
        return
    return response.json()


def refresh_oauth_token():
    refresh_token_file = './refresh_token.txt'
    authorization_token_file = './authorization_token.txt'
    rtf = open(refresh_token_file, 'r')
    refresh_token = rtf.read()
    rtf.close()
    headers = constants.oauth_header
    client_id = environ['client_id']
    client_secret = environ['client_secret']
    data = f'grant_type=refresh_token&client_id={client_id}&client_secret={client_secret}&refresh_token={refresh_token}'
    response = requests.request('POST', url=constants.OAUTH_TOKEN_URL, data=data, headers=headers)
    res = response.json()
    refresh_token = res['refresh_token']
    rtf.write(refresh_token)
    rtf.close()
    authorization_token = res['access_token']
    autf = open(authorization_token_file, 'w')
    autf.write(authorization_token)
    autf.close()
    return authorization_token


def main():
    res = get_oauth_token()
    return


if __name__ == '__main__':
    main()
    print('main - done')