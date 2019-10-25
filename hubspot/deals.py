# -*- coding: utf-8 -*-
"""...
"""
import requests
from . import constants


def update_deal(companyId, parameters):
    request_url = f'{constants.COMPANY_UPDATE_URL}{companyId}'
    response = requests.request('PUT', url=request_url,
                                headers=constants.header,
                                json=parameters,
                                params=constants.parameters)
    if response.status_code == 200:
        resp = response.json()
        return resp
    else:
        print(response.status_code)
        return


def search_for_deal_by_domain(domain, paramlist):
    payload = {
              "limit": 2,
              "requestOptions": {
                "properties": paramlist
                },
              "offset": {
                "isPrimary": True,
                "companyId": 0
                }
              }
    request_url = f'{constants.COMPANY_SEARCH_URL}{domain}/companies'
    response = requests.request('POST', url=request_url,
                                headers=constants.header,
                                json=payload,
                                params=constants.parameters)
    if response.status_code == 200:
        resp = response.json()
        return resp
    else:
        print(response.status_code)
        return


def get_all_deals(request_parameters):
    """Downloads the complete list of companies from the portal
    :param request_parameters: list of Contact parameters
    :return all_companies: list of dictionaries / CDR
    :return output_columns: list of output column names
    """
    def make_parameters_string(parameters_substring, offset, limit):
        authentication = 'hapikey=' + constants.api_key
        parameters_string = f'{authentication}{parameters_substring} \
                                &offset={offset}&limit={limit}'
        return parameters_string
    # prepare for the (inevitable) output
    all_deals    = []
    output_columns  = ['dealId', 'isDeleted']
    output_columns.extend(request_parameters)

    # package the parameters into a substring
    param_substring = ''
    for item in request_parameters:
        param_substring = '{}&properties={}'.format(param_substring, item)

    # prepare for the pagination
    has_more = True
    offset = 0
    limit = 2  # max 250

    # Now the main cycle
    while has_more:
        api_url = '{}?{}'.format(constants.DEALS_ALL_URL,
                                 make_parameters_string(param_substring, offset, limit))
        response = requests.request("GET", url=api_url, headers=constants.header)
        if response.status_code == 200:
            res = response.json()
            has_more    = res['hasMore']
            offset      = res['offset']
            deals       = res['deals']
            for deal in deals:
                row = {}
                row.update({"dealId": deal["dealId"],
                            "isDeleted": deal["isDeleted"]})
                de_properties = deal['properties']
                for de_property in de_properties:
                    if de_property not in output_columns:
                        output_columns.append(de_property)
                        print('Adding a property to colunms list: ', de_property)
                    row.update({de_property: de_properties[de_property]['value']})
                all_deals.append(row)
            print('Now at offset: ', offset)
        else:
            print(response.status_code)
    return all_deals, output_columns


def main():
    return


if __name__ == '__main__':
    main()
    print('main - done')