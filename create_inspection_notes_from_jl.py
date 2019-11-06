# -*- coding: utf-8 -*-
"""https://jsonlines.readthedocs.io/en/latest/
"""
import jsonlines
import pandas as pd
import hubspot
import datetime as dt


def main():
    INP_FILE = '/home/alxfed/archive/deals_inspections.jl'
    OUT_FILE = '/home/alxfed/archive/inspections_procssd.jl'
    reference_file_path = '/home/alxfed/archive/deals_downloaded.csv'
    ownerId = 40202623  # Data Robot

    permit_inspections = ['PERMIT INSPECTION', 'BLDG_PERM IRON PERMIT INSP', 'VENT/HEAT PERMIT INSPECTION',
                          'WATER DEPT PERMIT INSPECTION', 'ELECTRICAL PERMIT INSPECTION', 'CONSTRUCTION EQUIPMENT PERMIT',
                          'PORCH/DECK PERMIT INSPECTION', 'BLDG_PERM IRON PERMIT INSP', 'BOILER PERMIT INSPECTION',
                          'DOB NEW CONSTRUCTION INSP', 'DOB PLUMBING INSPECTION', 'DOB VENT/FURNACE INSPECTION',
                          'DOB REFRIGERATION INSPECTION', 'DOB GARAGE INSPECTION',
                          'EQUIPMENT INSPECTION']

    with jsonlines.open(INP_FILE, mode='r') as reader:
        with jsonlines.open(OUT_FILE, mode='a') as writer:
            for line in reader:
                full_address = line['full_address']
                input_address = line['input_address']
                range_address = line['range_address']
                permit = line['permit']
                perm_table = pd.DataFrame.from_records(line['perm_table'])
                perm_table['perm_date'] = pd.to_datetime(perm_table['perm_date'], infer_datetime_format=True)
                permeat = perm_table.loc[perm_table['permit_n'] == permit]

                dealId = 1143450728
                note_date = dt.datetime(year=2019, month=10, day=18, hour=0, minute=0, second=0)
                hubspot_timestamp = int(note_date.timestamp() * 1000)
                note_text = permeat.to_string(index=False)
                params = {'ownerId': ownerId, 'timestamp': hubspot_timestamp, 'dealId': dealId,
                          'note': note_text}
                res = hubspot.engagements.create_engagement_note(params)

                insp_table = pd.DataFrame.from_records(line['insp_table'])
                insp_table['insp_date'] = pd.to_datetime(insp_table['insp_date'], infer_datetime_format=True)
                tab = insp_table.to_html(index=False)
                # transform
                writer.write(line)
        writer.close()
    reader.close()
    return


if __name__ == '__main__':
    main()
    print('main - done')