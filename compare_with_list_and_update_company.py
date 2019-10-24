# -*- coding: utf-8 -*-
"""...
"""
import hubspot
import pandas as pd
import numpy as np
import re


def main():
    def ask_yn(company, license):
        print('1. Company in the system:    ', NAME, '    ', company['address'])
        print('2. Company in the list:      ', LICENSE,'    ', license['address'])
        inputchar = input('y/n ? ')
        if inputchar == 'y':
            output = True
        else:
            output = False
        return output

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
        first_c = re.sub("[^a-zA-Z]+", "", NAME[:5])
        for ind, license in gen_contractors.iterrows():
            LICENSE = license['company_name'].upper()
            first_l = re.sub("[^a-zA-Z]+", "", LICENSE[:5])
            if first_c == first_l:
                [nam_one, nam_two, nam_three] = NAME.split('', max=3)
                [lic_one, lic_two, lic_three] = LICENSE.split('', max=3)
                if nam_one == lic_one and nam_two == lic_two:
                    companyId = company['companyId']
                    parameters = {"properties":
                        [
                            {
                                "name": "name",
                                "value": LICENSE.title()
                            },
                            {
                                "name": "category",
                                "value": "General Contractor"
                            }
                        ]
                    }
                    if not (company['address'] == np.nan or license['address'] == np.nan):
                        print('no address')
                        pass # company and license have some of the address
                        # TODO: some of the other words coincide
                        # TODO: zip code coincide
                        # TODO: building number coincides
                    else:
                        if ask_yn(company, license):
                            result = hubspot.companies.update_company(companyId, parameters)
                            print('updated the company')
                        else:
                            print('did not do anything')
            else:
                pass # first letters don't coincide at all
    return


if __name__ == '__main__':
    main()
    print('main - done')