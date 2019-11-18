# -*- coding: utf-8 -*-
"""https://www.chicago.gov/city/en/depts/bldgs/provdrs/gen_contract.html
"""
import pandas as pd
from datetime import datetime
import numpy as np
from numpy import nan
import sqlalchemy as sqlalc
import unicodedata


def dateparse(x):
    if x is nan:
        return # datetime(2018, 12, 8, 0, 0)
    else:
        return pd.datetime.strptime(x, '%m/%d/%y') #  %H:%M:%S.%f if there are hours, minutes, seconts and milliseconds


def main():
    # active General Contractors are on https://webapps1.chicago.gov/activegcWeb/

    gen_cont_file_path = '/home/alxfed/archive/licensed_general_contractors.csv'

    gen_contractors = pd.read_csv(gen_cont_file_path,
                                    parse_dates=['license_expr',
                                                 'primary_insurance_expr',
                                                 'secondary_insurance_expr'],
                                    date_parser=dateparse,
                                    dtype=object)
    # gen_contractors['address'].str.encode('UTF-8')
    # gen_contractors.replace(u'\xa0', u' ', inplace=True)
    all_rows = []
    for index, contractor in gen_contractors.iterrows():
        row = {}
        address = contractor['address']
        street_address, city, state_zip = address.split('\xa0\xa0')
        state, zip = state_zip.split('\xa0')
        # ).replace(u'\xa0', u' ')
        contractor['address'] = address
        phone = contractor['phone'].replace('x', '')
        contractor['phone'] = phone

    conn = sqlalc.create_engine('sqlite:////home/alxfed/dbase/home.sqlite')
    gen_contractors.to_sql(name='licensed_general_contractors', con=conn, if_exists='replace')
    return


if __name__ == '__main__':
    main()
    print('main - done')