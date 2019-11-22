# -*- coding: utf-8 -*-
"""...
"""
import pandas as pd
import sqlalchemy as sqlalc


def main():
    # 1533049923684
    frame = [{'dealId': 239565048, 'isDeleted': False, 'associatedVids': '1251', 'associatedCompanyIds': '629041982', 'associatedDealIds': '', 'associatedTicketIds': '', 'pipeline': 'default', 'dealname': 'ENP Kong fu tea', 'amount': '2772.09', 'closedate': '1514700000000', 'dealstage': 'closedlost', 'hs_object_id': '239565048'},
             {'dealId': 239570579, 'isDeleted': False, 'associatedVids': '951', 'associatedCompanyIds': '', 'associatedDealIds': '', 'associatedTicketIds': '', 'pipeline': 'default', 'dealname': 'ENP 2302 N Hoyne, Chicago', 'amount': '17649.45', 'closedate': '1514700000000', 'dealstage': 'closedlost', 'hs_object_id': '239570579'},
             {'dealId': 239573361, 'isDeleted': False, 'associatedVids': '801', 'associatedCompanyIds': '628625168', 'associatedDealIds': '', 'associatedTicketIds': '', 'pipeline': 'default', 'dealname': 'ENP Craftwood Products INC. -HUDSON CONTRACTORS', 'amount': '9517', 'closedate': '1514700000000', 'dealstage': 'closedlost', 'hs_object_id': '239573361'},
             {'dealId': 239680470, 'isDeleted': False, 'associatedVids': '1301', 'associatedCompanyIds': '629066211', 'associatedDealIds': '', 'associatedTicketIds': '', 'pipeline': 'default', 'dealname': 'ENP  Cezar Construction11540 Jenyglen Rd, Mokena 25cab', 'amount': '18388.04', 'closedate': '1516168800000', 'dealstage': 'closedlost', 'hs_object_id': '239680470'},
             {'dealId': 239686689, 'isDeleted': False, 'associatedVids': '', 'associatedCompanyIds': '628907762', 'associatedDealIds': '', 'associatedTicketIds': '', 'pipeline': 'default', 'dealname': 'PRC Maureen Manganiello', 'amount': '4624', 'closedate': '1514700000000', 'dealstage': 'closedlost', 'hs_object_id': '239686689'}]
    all_deals = pd.DataFrame(frame)
    all_deals['closedate'] = pd.to_datetime(all_deals['closedate'], unit='ms')
    conn = sqlalc.create_engine('sqlite:////home/alxfed/dbase/home.sqlite')
    all_deals.to_sql(name='test', con=conn, if_exists='replace', index=False)
    return


if __name__ == '__main__':
    main()
    print('main - done')