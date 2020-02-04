# -*- coding: utf-8 -*-
"""...
"""
from .constants import *
from requests import Request, Session, get
import requests

def all_chicago_datasets():
    session = Session()
    params = {'domains': 'data.cityofchicago.org', 'search_context': 'data.cityofchicago.org'}
    request = Request(method='GET', url=DISCOVERY_API_URL, params=params)
    prepped = request.prepare()
    res = session.send(prepped)
    response = res.json()
    return response['results']


def datasets_of_domain(domain):
    session = Session()
    params = {'domains': domain, 'search_context': domain, 'offset': 0, 'limit': 1000}
    # f'&$limit={limit}&$offset={offset}'
    request = Request(method='GET', url=DISCOVERY_API_URL, headers=socrata_authorization_header, params=params)
    prepped = request.prepare()
    res = session.send(prepped)
    response = res.json()
    return response['results']


def all_datasets_of_domain(domain):
    def dataset_chunk(url):
        response = requests.get(url, headers=socrata_authorization_header)
        if response.status_code == 200:
            return response.json()
        elif response.status_code == 201:
            raise RuntimeError("Request Processing")
        elif response.status_code == 400:
            raise RuntimeError("Bad Request")
        elif response.status_code == 401:
            raise RuntimeError("Unauthorized")
        elif response.status_code == 403:
            raise RuntimeError("Forbidden")
        elif response.status_code == 404:
            raise RuntimeError("Not Found")
        elif response.status_code == 429:
            raise RuntimeError("Too many Requests")
        elif response.status_code == 500:
            raise RuntimeError("Server Error")
        else:
            return None  # silently return nothing

    api_url = f'https://{DISCOVERY_API_URL}'
    api_call = f'{api_url}?domains={domain}&search_context={domain}'

    limit = 10    # limit of the frame within the time window
    offset = 0
    data = []       # the accumulation of chunks for final result
    data_to_read_left = True

    while data_to_read_left:
        api_frame = f'{api_call}&offset={offset}&limit={limit}'
        new_chunk = dataset_chunk(api_frame)
        data.extend(new_chunk['results'])      # Append the newly acquired records to the list
        # a way to detect 'has_more' (with probability of error 1/2000)
        if len(new_chunk) == limit:
            offset += limit
            # print('offset: ', offset) # show the man that something's going on.
        else:
            data_to_read_left = False
    return data



def metadata_for_dataset(four_by_four):
    params = {'ids': four_by_four}
    response = get(url=DISCOVERY_API_URL, params=params)
    return response.json()['results']

def main():
    print('ok')
    return


if __name__ == '__main__':
    main()
    print('main - done')