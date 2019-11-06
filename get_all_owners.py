# -*- coding: utf-8 -*-
"""...
"""
import hubspot


def main():
    owners_json = hubspot.owners.get_owners()
    print(owners_json)
    return


if __name__ == '__main__':
    main()
    print('main - done')