# -*- coding: utf-8 -*-
"""...
"""
import hubspot
import pandas as pd
import numpy as np
import re


def main():
    DOWNLOADED_COMPANIES_FILE_PATH = '/home/alxfed/archive/companies_downloaded.csv'
    companies_columns = ['companyId', 'isDeleted', 'name',
                         'phone', 'phone_mobile',
                         'address', 'city', 'zip', 'state', 'category', 'website']
    downl_companies = pd.read_csv(DOWNLOADED_COMPANIES_FILE_PATH,
                                    usecols=companies_columns,
                                    dtype=object)

    gen_cont_file_path = '/home/alxfed/archive/licensed_general_contractors.csv'
    licenses_columns = ['license_type',
                        'company_name', 'address', 'phone']
    gen_contractors = pd.read_csv(gen_cont_file_path,
                                    usecols=licenses_columns,
                                    dtype=object)

    for indx, company in downl_companies.iterrows():
        NAME = company['name'].upper()
        first = re.sub("[^a-zA-Z]+", "", NAME[:10])
        licenses = gen_contractors['company_name']
        for license in licenses:
            if first == license[:10]:
                print('1. Company in the system: ', NAME, company['address'], '\n')
                print('2. Company in the list:   ', license, '\n')
                inputchar = input('y/n ? ')
                if inputchar == 'y':
                    companyId = company['companyId']
                    parameters = {"properties":
                        [
                            {
                                "name": "name",
                                "value": license.title()
                            },
                            {
                                "name": "category",
                                "value": "General Contractor"
                            }
                        ]
                    }
                    result = hubspot.companies.update_company(companyId, parameters)
                    print('ok')
    return


if __name__ == '__main__':
    main()
    print('main - done')