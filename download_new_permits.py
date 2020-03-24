# -*- coding: utf-8 -*-
"""https://dev.socrata.com/foundry/data.cityofchicago.org/ydr8-5enu
"""
import datetime as dt
import requests
import pandas as pd
from os import environ


RESOURCE_URL = 'data.cityofchicago.org'
RESOURCE_ID  = 'ydr8-5enu'                      # permits data
api_token = environ['API_TOKEN']
api_url = f'https://{RESOURCE_URL}/resource/{RESOURCE_ID}.json'
header = {'Content-Type': 'application/json', 'X-App-Token': api_token}


def data_chunk(uri):
    response = requests.get(uri, headers=header)
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
        return None # silently return nothing


def main():
    """Read a chunk with date_issued in predefined window
    """
    data = pd.DataFrame()

    start_dt = dt.datetime(year=2019, month=10, day=18, hour=0, minute=0, second=0)
    start_str = start_dt.strftime('%Y-%m-%dT%H:%M:%S')
    end_dt = dt.datetime(year=2019, month=11, day=5, hour=0, minute=0, second=0)
    end_str = end_dt.strftime('%Y-%m-%dT%H:%M:%S')
    api_call = api_url + f'?$where=issue_date between "{start_str}" and "{end_str}"'

    limit = 1000  # limit of the frame within the time window
    offset = 0
    data_to_read_left = True

    while data_to_read_left:
        api_frame = api_call + f'&$limit={limit}&$offset={offset}'
        new_chunk = pd.DataFrame.from_records(data_chunk(api_frame))
        new_chunk['issue_date'] = pd.to_datetime(new_chunk['issue_date'])
        new_chunk['application_start_date'] = pd.to_datetime(new_chunk['application_start_date'])
        new_chunk['reported_cost'] = pd.to_numeric(new_chunk['reported_cost'], downcast='unsigned')
        data = data.append(new_chunk, sort=False, ignore_index = True)
        if new_chunk.id.count() == limit:
            offset += limit
            print('offset: ', offset)
        else:
            data_to_read_left = False
    data.to_csv('/media/alxfed/toca/presentation/all_new_permits.csv', index=False)
    data.to_json('/media/alxfed/toca/presentation/all_new_permits.jl', orient='records', lines=True)
    new_construction = data[data['permit_type'] == 'PERMIT - NEW CONSTRUCTION']
    new_construction.to_csv('/media/alxfed/toca/presentation/newconstruction.csv', index=False)
    new_construction.to_json('/media/alxfed/toca/presentation/newconstruction.jl', orient='records', lines=True)
    renovation = data[data['permit_type'] == 'PERMIT - RENOVATION/ALTERATION']
    renovation.to_csv('/media/alxfed/toca/presentation/renovationalt.csv', index=False)
    renovation.to_json('/media/alxfed/toca/presentation/renovationalt.jl', orient='records', lines=True)
    return


if __name__ == '__main__':
    main()
    print('main - done')

