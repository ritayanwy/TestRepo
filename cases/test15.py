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
        TEST['request'][2]['data']['account_id'] = res['data']['list'][0]['account_id']
        for folder in res['data']['list'][0]['list']:
            if folder['folder_type'] == 4:
                TEST['request'][1]['data']['mailbox_path'] = folder['mailbox_path']
                TEST['request'][2]['data']['mailbox_path'] = folder['mailbox_path']
                TEST['request'][1]['data']['folder'] = folder['label']
                TEST['request'][2]['data']['folder'] = folder['label']
                break
        if TEST['request'][1]['data'].get('mailbox_path') is None:
            return False
    return True


def search_handler1(response):
    print response.text
    res = json.loads(response.text)
    if res['error_code'] != 0 or res['data']['has_more'] != 1:
        return False
    TEST['request'][2]['data']['ts'] = res['data']['list'][9]['date_ts']
    TEST['request'][2]['data']['sync_hash'] = res['data']['sync_hash']

    return True

def search_handler2(response):
    print response.text
    res = json.loads(response.text)
    if res['error_code'] != 0 or len(res['data']['list']) == 0:
        return False
    return True


TEST = {
        'name': 'Gmail Search has more check',
        'request': [
            {
                'method': 'POST',
                'url': '/a/v6/data/message/getfolderlist',
                'timeout': 60
            },
            {
                'method': 'POST',
                'url': '/a/v6/data/message/search',
                'data': {'ts': int(time.time()),
                         'count': 0,
                         'query': 'test',
                         'sync_hash': '{}'},
                'timeout': 60,
            },
            {
                'method': 'POST',
                'url': '/a/v6/data/message/search',
                'data': {'count': 10,
                         'query': 'test'},
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
                'hooks': search_handler1
            },
            {
                'status_code': 200,
                'hooks': search_handler2
            }
        ]
}

