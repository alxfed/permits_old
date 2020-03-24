# -*- coding: utf-8 -*-
from scrapy.spiders import CSVFeedSpider
from collections import OrderedDict
import scrapy
from data.items import InspTableLine, PermTableLine
from datetime import datetime
import re


def not_identified(response):
    # //*[@id="search"]/div[2]/p
    NO_MATCH_XPATH = '//*[@id="search"]/div[2]/p/text()'
    no_address_found = response.xpath(NO_MATCH_XPATH).get()
    if no_address_found:
        if no_address_found.startswith('The address match was not found.'):
            return True
        else:
            return True
    else:
        return False


def not_found(response):
    # //*[@id="search"]/div[2]/p
    NO_RESULTS_XPATH = '//*[@id="search"]/div[2]/p/text()'
    no_address_found = response.xpath(NO_RESULTS_XPATH).get()
    if no_address_found:
        if no_address_found.startswith('No results found for this address.'):
            return True
        else:
            return True
    else:
        return False



class InspListCSpider(CSVFeedSpider):
    name = 'inspections'
    allowed_domains = ['webapps1.chicago.gov']
    start_urls = ['file:///home/alxfed/archive/deals_downloaded.csv']
    headers = ['dealId', 'isDeleted',
               'associatedVids', 'associatedTicketIds', 'associatedCompanyIds', 'associatedDealIds',
               'dealname', 'closedate', 'amount', 'pipeline', 'dealstage',
               'permit_issue_date', 'permit_', 'permit', 'permit_type', 'work_descrption',
               'last_inspection', 'last_inspection_date', 'insp_n', 'insp_note']

    INSPECTIONS_URL = 'https://webapps1.chicago.gov/buildingrecords/doSearch'
    VALIDATE_URL = 'https://webapps1.chicago.gov/buildingrecords/validateaddress'

    # Do any adaptations you need here
    #def adapt_response(self, response):
    #    return response

    def parse_row(self, response, row):
        address = ''
        keys = row.keys()
        header_start = self.headers[0]
        if row[header_start].startswith(header_start):
            yield None
        elif not row['permit_']:
            yield None
        else:
            if row['dealname'].startswith('RA ') or row['dealname'].startswith('NC '):
                address = row['dealname'][3:]
            elif not row['dealname']:
                yield None
            else:
                address = row['dealname']
            the_kwargs = {'permit_n': row['permit_'],
                          'full_address': address}
            yield scrapy.Request(url=self.INSPECTIONS_URL,
                                 dont_filter=True,
                                 callback=self.parse_table,
                                 cb_kwargs=the_kwargs)

    def parse_table(self, response, **kwargs):
        PERM_ROWS_XPATH = '//*[@id="resultstable_permits"]/tbody/tr'
        INSP_ROWS_XPATH = '//*[@id="resultstable_inspections"]/tbody/tr'
        table_line = OrderedDict()
        perm_list = []
        insp_list = []
        table_line.update({'full_address': kwargs['full_address'],
                           'input_address': kwargs['full_address'],
                           'permit': kwargs['permit_n'],
                           'range_address': '',
                           'perm_table': '',
                           'insp_table': ''})
        if response.url == self.INSPECTIONS_URL and not not_found(response):
            input_address = response.xpath('/html/body/div/div[4]/div[3]/p/text()').get()
            range_address = response.xpath('/html/body/div/div[4]/div[4]/p/text()').get()
            table_line.update({'input_address': input_address,
                               'range_address': range_address})
            perm_table_selector = response.xpath(PERM_ROWS_XPATH)
            # columns: PERMIT #, DATE ISSUED, DESCRIPTION OF WORK
            if perm_table_selector:
                for perm_line in perm_table_selector:
                    perm_table_line = PermTableLine()
                    # //*[@id="resultstable_permits"]/tbody/tr[1]/td[1]
                    perm_table_line['permit_n'] = perm_line.xpath('td[1]/text()').get()
                    perm_date = datetime.strptime(perm_line.xpath('td[2]/text()').get(), '%m/%d/%Y')
                    perm_table_line['perm_date'] = perm_date.strftime('%Y-%m-%d')
                    perm_table_line['work_desc'] = perm_line.xpath('td[3]/text()').get()
                    perm_list.append(perm_table_line)
            else:
                perm_list.append(dict())
            table_line.update({'perm_table': perm_list})
            insp_table_selector = response.xpath(INSP_ROWS_XPATH)
            # columns: INSP #, INSPECTION DATE, STATUS, TYPE DESCRIPTION
            if insp_table_selector:
                for insp_line in insp_table_selector:
                    insp_table_line = InspTableLine()
                    # //*[@id="resultstable_inspections"]/tbody/tr[1]/td[1]/a
                    insp_table_line['insp_n'] = insp_line.xpath('td[1]/a/text()').get()
                    # insp_date = datetime.strptime(insp_line.xpath('td[2]/text()').get(), '%m/%d/%Y')
                    insp_table_line['insp_date'] = insp_line.xpath('td[2]/text()').get() # insp_date.strftime('%Y-%m-%d')
                    # insp_table_line['insp_date'] = insp_line.xpath('td[2]/text()').get()
                    insp_table_line['status'] = insp_line.xpath('td[3]/text()').get()
                    insp_table_line['type_desc'] = insp_line.xpath('td[4]/text()').get()
                    insp_list.append(insp_table_line)
            else:
                insp_list.append(dict())
            table_line.update({'insp_table': insp_list})
            yield table_line
        elif response.url == self.VALIDATE_URL:
            if not_identified(response):
                table_line.update({'input_address': 'Not identified'})
                yield table_line
            else:
                table_line.update({'input_address': 'Not searcheable'})
                yield table_line
        else:
            table_line.update({'input_address': 'Not found'})
            yield table_line

