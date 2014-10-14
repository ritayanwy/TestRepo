import json
from testcases import TEST_ENV


def handler(response):
    print response.text
    if json.loads(response.text)['error_code'] != 0:
        return False
    return True


TEST = {
        'name': 'GetFolderList API',
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



