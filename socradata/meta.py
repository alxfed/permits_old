# -*- coding: utf-8 -*-
"""...
"""
from .constants import *
from requests import Request, Session


def all_chicago_datasets():
    session = Session()
    params = {'domains': 'data.cityofchicago.org', 'search_context': 'data.cityofchicago.org'}
    request = Request(method='GET', url=DISCOVERY_API_URL, params=params)
    prepped = request.prepare()
    response = session.send(prepped)
    return response.json()


def main():
    all_datasets = all_chicago_datasets()
    print('ok')
    return


if __name__ == '__main__':
    main()
    print('main - done')