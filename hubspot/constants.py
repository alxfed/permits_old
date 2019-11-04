# -*- coding: utf-8 -*-
"""...
"""
from os import environ
from os.path import getmtime
from datetime import datetime
import datetime

# files
AUTHORIZATION_TOKEN_FILE    = '/home/alxfed/credo/authorization_token.txt'
REFRESH_TOKEN_FILE          = '/home/alxfed/credo/refresh_token.txt'
CLIENT_ID_FILE              = '/home/alxfed/credo/client_id.txt'
CLIENT_SECRET_FILE          = '/home/alxfed/credo/client_secret.txt'

token_file = open(AUTHORIZATION_TOKEN_FILE, 'r')
authorization_token = token_file.read()
token_file.close()

parameters = {}
if 'API_KEY' in environ.keys():
    api_key = environ['API_KEY']
    parameters = {'hapikey': api_key}
else:
    print('No API_KEY')

bearer_string = f'Bearer {authorization_token}'
authorization_header = {'Authorization': bearer_string}
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