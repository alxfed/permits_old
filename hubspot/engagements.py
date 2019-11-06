# -*- coding: utf-8 -*-
"""...
"""
import requests
from . import constants


def create_engagement_note(parameters):
    data = {"engagement": {
                    "active": 'true',
                    "ownerId": parameters['ownerId'],
                    "type": "NOTE",
                    "timestamp": parameters['timestamp']
                },
                "associations": {
                    "contactIds": [],
                    "companyIds": [],
                    "dealIds": [parameters['dealId']],
                    "ownerIds": [parameters['ownerId']]
                },
                "attachments": [
                    {
                        "id": ''
                    }
                ],
                "metadata": {
                    "body": parameters['note']
                }
            }

    response = requests.request("POST", url=constants.ENGAGEMENTS_URL, json=data,
                                headers=constants.authorization_header)
    if response.status_code == 200:
        print('Created a note to deal ', parameters['dealId'])
    else:
        print('not ok! ', response.status_code)
    return



def main():
    return


if __name__ == '__main__':
    main()
    print('main - done')