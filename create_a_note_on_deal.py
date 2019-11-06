# -*- coding: utf-8 -*-
"""...
"""
import pandas as pd
import hubspot
import datetime as dt


def main():
    ownerId = 40202623 # Data Robot
    dealId = 1143450728
    appId = 205476
    note_date = dt.datetime(year=2019, month=10, day=18, hour=0, minute=0, second=0)
    hubspot_timestamp = int(note_date.timestamp()*1000)
    note_text = 'this is the note text</br> Etc.'
    params = {'ownerId': ownerId, 'timestamp': hubspot_timestamp, 'dealId': dealId,
              'note': note_text}
    res = hubspot.engagements.create_engagement_note(params)
    return


if __name__ == '__main__':
    main()
    print('main - done')