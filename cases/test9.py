import json
from testcases import TEST_ENV


def handler(response):
    print response.text
    res = json.loads(response.text)

    if res['error_code'] != 0:
        return False

    for account in res['data']['list']:
        a=1
        for folder in account["list"]:
            a = a * folder['folder_type']

        if a != 0:
          return False

    return True


TEST = {
        'name': 'GetFolderList API - Check Inbox',
        'request': [
        {
                'method': 'POST',
                'url': '/a/v5/data/message/getfolderlist',
                'timeout': 60
        }
        ],
        'response': [
        {
                'status_code': 200,
                'hooks': handler
        }
        ]
}

