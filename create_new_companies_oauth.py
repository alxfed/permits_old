# -*- coding: utf-8 -*-
"""...
"""
import pandas as pd
import hubspot


def main():
    params = {
                    'name': '',
                    'type':'PROSPECT',
                    'phone':'',
                    'address':'',
                    'city':'',
                    'state':'',
                    'zip': '',
                    'category':'General Contractor'
                  }

    companies_file_path = '/home/alxfed/archive/new_licensed_contractors_with_permits.csv'
    companies_columns = ['name', 'address', 'phone', 'category']
    contractors = pd.read_csv(companies_file_path,
                              usecols=companies_columns,
                              dtype=object)

    created_file_path = '/home/alxfed/archive/created_new_companies.csv'
    created = []

    for indx, contractor in contractors.iterrows():
            parameters = params.copy()
            parameters['name'] = contractor['name'].title()
            parameters['phone'] = contractor['phone']
            parameters['address'] = contractor['address']
            done = hubspot.companies.create_company(parameters)
            print('Created ', parameters['name'])
    return


if __name__ == '__main__':
    main()
    print('main - done')