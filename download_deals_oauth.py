# -*- coding: utf-8 -*-
"""...
"""
import hubspot
import csv


def main():
    '''
    authorization_token_file = '/home/alxfed/credo/authorization_token.txt'
    authorization_token = ''
    authorization_file = open(authorization_token_file, 'r')
    authorization_token = authorization_file.read()
    authorization_file.close()
    '''
    stage_values_to_names = {'815586': 'Permit Issued',
                             '815587': 'General Contractor Contacted',
                             '815588': 'Contact Info obtained. Won',
                             '815589': 'Not interested. Lost'}

    DOWNLOADED_DEALS_FILE_PATH = '/home/alxfed/archive/deals_downloaded.csv'
    request_params = ['dealname', 'closedate', 'amount', 'pipeline', 'dealstage',
                      'permit_issue_date', 'permit_', 'permit', 'permit_type',
                      'work_descrption',
                      'last_inspection', 'last_inspection_date', 'insp_n', 'insp_note']
    # my pipeline is 815585 , stage 815586
    include_associations = True

    all_deals_cdr, all_columns = hubspot.deals.get_all_deals_oauth(request_params, include_associations)

    with open(DOWNLOADED_DEALS_FILE_PATH, 'w') as f:
        f_csv = csv.DictWriter(f, fieldnames=all_columns)
        f_csv.writeheader()
        f_csv.writerows(all_deals_cdr)
    return


if __name__ == '__main__':
    main()
    print('main - done')