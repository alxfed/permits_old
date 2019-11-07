# -*- coding: utf-8 -*-
"""...
"""
import hubspot
import csv


def main():
    # downloads ALL engagements! Can be a lot!
    DOWNLOADED_ENGAGEMENTS_FILE_PATH = '/home/alxfed/archive/engagements_downloaded.csv'

    all_engagements, all_columns = hubspot.engagements.get_all_engagements_oauth()
    with open(DOWNLOADED_ENGAGEMENTS_FILE_PATH, 'w') as f:
        f_csv = csv.DictWriter(f, fieldnames=all_columns)
        f_csv.writeheader()
        f_csv.writerows(all_engagements)
    return


if __name__ == '__main__':
    main()
    print('main - done')