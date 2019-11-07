# -*- coding: utf-8 -*-
"""...
"""
import pandas as pd
import hubspot
import datetime


def main():
    downloaded_engagements_file_path = '/home/alxfed/archive/engagements_downloaded.csv'
    engagements_columns = ['id', 'portalId', 'active', 'createdAt', 'lastUpdated', 'type', 'timestamp',
                           'contactIds', 'companyIds', 'dealIds', 'ownerIds', 'workflowIds',
                           'ticketIds', 'contentIds', 'quoteIds', 'attachments', 'metadata']
    reference = pd.read_csv(downloaded_engagements_file_path, usecols=engagements_columns, dtype=object)

    update_file_path = '/home/alxfed/archive/engagements_to_update.csv'
    update_columns = ['id', 'portalId', 'active', 'createdAt', 'lastUpdated', 'type', 'timestamp',
                           'contactIds', 'companyIds', 'dealIds', 'ownerIds', 'workflowIds',
                           'ticketIds', 'contentIds', 'quoteIds', 'attachments', 'metadata']
    update_table = pd.read_csv(update_file_path, usecols=update_columns, dtype=object)

    parameters = {}

    for index, engagement_to_update in update_table.iterrows():
        engagementId = engagement_to_update['id']
        gotten = hubspot.engagements.get_an_engagement(engagementId)
        gokeys = gotten.keys()
        parameters['timestamp'] = int(datetime.datetime.now().timestamp()*1000)
        updated = hubspot.engagements.update_an_engagement(engagementId, parameters)
        print('ok')
    return


if __name__ == '__main__':
    main()
    print('main - done')