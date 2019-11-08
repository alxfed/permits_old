# -*- coding: utf-8 -*-
"""...
"""
import pandas as pd
from tabulate import tabulate


def main():
    data = pd.DataFrame()
    line1 = {'a': 1, 'c': 3, 'e':1}
    line2 = {'b': 2, 'd': 1}
    data = data.append(line1, ignore_index=True)
    data = data.append(line2, sort=True, ignore_index=True)
    tb = tabulate(data, showindex='never', tablefmt='plain')
    print(tb)
    return


if __name__ == '__main__':
    main()
    print('main - done')