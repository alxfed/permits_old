# -*- coding: utf-8 -*-
"""https://dev.socrata.com/foundry/data.cityofchicago.org/r5kz-chrr
"""
import datetime as dt
import requests
import pandas as pd
from os import environ


def main():
    """Read a file of business licenses and drop duplicates in a column
    """
    data = pd.read_csv('/home/alxfed/archive/business_licenses.csv', dtype=object)
    all_columns = data.columns.tolist()
    examples = data.drop_duplicates(subset=['BUSINESS ACTIVITY'], keep='first', inplace=False)
    known = set()
    activities = examples['BUSINESS ACTIVITY']
    for line in activities:
        spl = line.str.split(' | ')
    activities.to_csv('/home/alxfed/archive/activities_of_business_licenses.csv')
    return


if __name__ == '__main__':
    main()
    print('main - done')
