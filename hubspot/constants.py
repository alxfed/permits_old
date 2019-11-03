# -*- coding: utf-8 -*-
"""...
"""
from os import environ


def hubspot_timestamp_from_date(date_object):
    from datetime import datetime
    date = datetime.fromisoformat(date_object)
    hubspot_timestamp = int(1000 * date.timestamp())
    return hubspot_timestamp


def date_from_hubsport_timestamp(hubspot_timestamp):
    from datetime import datetime
    date_time = datetime.fromtimestamp(int(hubspot_timestamp/1000))
    return date_time


parameters = {}
if 'API_KEY' in environ.keys():
    api_key = environ['API_KEY']
    parameters = {'hapikey': api_key}
else:
    print('No API_KEY')

header = {'Content-Type': 'application/json'}
oauth_header = {'Content-Type': 'application/x-www-form-urlencoded;charset=utf-8'}

COMPANY_CREATE_URL  = 'https://api.hubapi.com/companies/v2/companies'
COMPANY_DELETE_URL  = 'https://api.hubapi.com/companies/v2/companies/'
COMPANY_UPDATE_URL  = 'https://api.hubapi.com/companies/v2/companies/'
COMPANY_SEARCH_URL  = 'https://api.hubapi.com/companies/v2/domains/'
COMPANIES_ALL_URL   = 'https://api.hubapi.com/companies/v2/companies/paged'

CONTACT_URL         = 'https://api.hubapi.com/contacts/v1/contact'
CONTACTS_ALL_URL = 'https://api.hubapi.com/contacts/v1/lists/all/contacts/all'
CONTACT_SEARCH_QUERY_URL = 'https://api.hubapi.com/contacts/v1/search/query?q='

ASSOCIATIONS_URL    = 'https://api.hubapi.com/crm-associations/v1/associations'

DEALS_ALL_URL       = 'https://api.hubapi.com/deals/v1/deal/paged'
DEAL_URL            = 'https://api.hubapi.com/deals/v1/deal'

ENGAGEMENTS_URL     = 'https://api.hubapi.com/engagements/v1/engagements'

OAUTH_TOKEN_URL     = 'https://api.hubapi.com/oauth/v1/token'