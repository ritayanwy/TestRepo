__author__ = 'anurag'
import json
import time

mailbox_path = None


def folderlist_handler(response):
    print response.text
    res = json.loads(response.text)
    if res['error_code'] != 0:
        return False
    if len(res['data']['list']) > 0 and len(res['data']['list'][0]['list']) > 0:
        TEST['request'][1]['data']['account_id'] = res['data']['list'][0]['account_id']
        for folder in res['data']['list'][0]['list']:
            if folder['folder_type'] == 4:
                TEST['request'][1]['data']['mailbox_path'] = folder['mailbox_path']
                TEST['request'][1]['data']['label'] = folder['label']
                break
        if TEST['request'][1]['data'].get('mailbox_path') is None:
            return False
    return True


def search_handler(response):
    print response.text
    res = json.loads(response.text)
    if res['error_code'] != 0 or len(res['data']['list']) == 0:
        return False
    return True


TEST = {
        'name': 'Search',
        'request': [
            {
                'method': 'POST',
                'url': '/a/v5/data/message/getfolderlist',
                'timeout': 60
            },
            {
                'method': 'POST',
                'url': '/a/v5/data/message/search',
                'data': {'ts': int(time.time()),
                         'count': 0,
                         'query': 'test',
                         'sync_hash': '{}'},
                'timeout': 60,
            }
        ],
        'response': [
            {
                'status_code': 200,
                'hooks': folderlist_handler
            },
            {
                'status_code': 200,
                'hooks': search_handler
            }
        ]
}



