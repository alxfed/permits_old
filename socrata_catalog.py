# -*- coding: utf-8 -*-
"""...
"""
from socradata import meta
import pandas as pd


def main():
    output_file_path = '/home/alxfed/archive/all_chicago_datasets.csv'
    sections = ['resource', 'classification', 'metadata', 'permalink', 'link', 'preview_image_url', 'owner']
    catalog = pd.DataFrame()
    row = {}
    all_datasets = meta.all_chicago_datasets()
    for dataset in all_datasets:
        row = dataset['resource']
        catalog = catalog.append(row, ignore_index=True)
        print('ok')
    # metadata = meta.metadata_for_dataset('ydr8-5enu')
    catalog.to_csv(output_file_path, index=False)
    return


if __name__ == '__main__':
    main()
    print('main - done')