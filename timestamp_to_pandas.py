# -*- coding: utf-8 -*-
"""...
"""
import pandas as pd
import sqlalchemy as sqlalc
import hubspot


def main():
    # 1533049923684
    '''
    all_deals_cdr = [{'dealId': 239565048, 'isDeleted': False, 'associatedVids': '1251', 'associatedCompanyIds': '629041982', 'associatedDealIds': '', 'associatedTicketIds': '', 'pipeline': 'default', 'dealname': 'ENP Kong fu tea', 'amount': '2772.09', 'closedate': '1514700000000', 'dealstage': 'closedlost', 'hs_object_id': '239565048'},
             {'dealId': 239570579, 'isDeleted': False, 'associatedVids': '951', 'associatedCompanyIds': '', 'associatedDealIds': '', 'associatedTicketIds': '', 'pipeline': 'default', 'dealname': 'ENP 2302 N Hoyne, Chicago', 'amount': '17649.45', 'closedate': '1514700000000', 'dealstage': 'closedlost', 'hs_object_id': '239570579'},
             {'dealId': 239573361, 'isDeleted': False, 'associatedVids': '801', 'associatedCompanyIds': '628625168', 'associatedDealIds': '', 'associatedTicketIds': '', 'pipeline': 'default', 'dealname': 'ENP Craftwood Products INC. -HUDSON CONTRACTORS', 'amount': '9517', 'closedate': '1514700000000', 'dealstage': 'closedlost', 'hs_object_id': '239573361'},
             {'dealId': 239680470, 'isDeleted': False, 'associatedVids': '1301', 'associatedCompanyIds': '629066211', 'associatedDealIds': '', 'associatedTicketIds': '', 'pipeline': 'default', 'dealname': 'ENP  Cezar Construction11540 Jenyglen Rd, Mokena 25cab', 'amount': '18388.04', 'closedate': '1516168800000', 'dealstage': 'closedlost', 'hs_object_id': '239680470'},
             {'dealId': 239686689, 'isDeleted': False, 'associatedVids': '', 'associatedCompanyIds': '628907762', 'associatedDealIds': '', 'associatedTicketIds': '', 'pipeline': 'default', 'dealname': 'PRC Maureen Manganiello', 'amount': '4624', 'closedate': '1514700000000', 'dealstage': 'closedlost', 'hs_object_id': '239686689'}]
    '''
    request_params = ['hs_object_id', 'dealname', 'closedate', 'amount', 'pipeline', 'dealstage',
                      'permit_issue_date', 'permit_', 'permit', 'permit_type',
                      'work_descrption',
                      'last_inspection', 'last_inspection_date', 'insp_n', 'insp_note']

    normal_columns = ['dealId', 'isDeleted',
                      'hs_object_id', 'dealname', 'closedate', 'amount', 'pipeline', 'dealstage',
                      'permit_issue_date', 'permit_', 'permit', 'permit_type',
                      'work_descrption',
                      'last_inspection', 'last_inspection_date', 'insp_n', 'insp_note']
    include_associations = True

    all_deals_cdr, all_columns = hubspot.deals.get_first_page_of_deals_oauth(request_params, include_associations)
    all_deals = pd.DataFrame(all_deals_cdr, columns=normal_columns)
    all_deals.fillna(value='', inplace=True)
    all_deals['dealId'] = all_deals['dealId'].astype(dtype=int)
    all_deals['isDeleted'] = all_deals['isDeleted'].astype(dtype=bool)
    all_deals['hs_object_id'] = all_deals['hs_object_id'].astype(dtype=int)
    all_deals['dealname'] = all_deals['dealname'].astype(dtype=object)
    all_deals['closedate'] = pd.to_datetime(all_deals['closedate'], unit='ms')
    all_deals['amount'] = pd.to_numeric(all_deals['amount'])
    all_deals['pipeline'] = all_deals['pipeline'].astype(dtype=object)
    all_deals['dealstage'] = all_deals['dealstage'].astype(dtype=object)
    all_deals['permit_issue_date'] = all_deals['permit_issue_date'].astype(dtype=object)
    all_deals['permit_'] = all_deals['permit_'].astype(dtype=object)
    all_deals['permit'] = all_deals['permit'].astype(dtype=object)
    all_deals['permit_type'] = all_deals['permit_type'].astype(dtype=object)
    all_deals['work_descrption'] = all_deals['work_descrption'].astype(dtype=object)
    all_deals['last_inspection'] = all_deals['last_inspection'].astype(dtype=object)
    all_deals['last_inspection_date'] = all_deals['last_inspection_date'].astype(dtype=object)
    all_deals['insp_n'] = all_deals['insp_n'].astype(dtype=object)
    all_deals['insp_note'] = all_deals['insp_note'].astype(dtype=object)

    conn = sqlalc.create_engine('sqlite:////home/alxfed/dbase/home.sqlite')
    all_deals.to_sql(name='test', con=conn, if_exists='replace', index=False)
    print('ok')
    return


if __name__ == '__main__':
    main()
    print('main - done')