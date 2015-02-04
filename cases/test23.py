import json
import time


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
                TEST['request'][1]['data']['folder'] = folder['label']
                break
        if TEST['request'][1]['data'].get('mailbox_path') is None:
            return False
    return True


def list_handler(response):
    print response.text
    res = json.loads(response.text)
    if res['error_code'] != 0 or len(res['data']['list']) == 0:
        return False
    account_id = res['data']['account_id']
    resource_id = res['data']['list'][0]['resource_id']
    TEST['request'][2]['data']['account_id'] = account_id
    TEST['request'][2]['data']['resource_id'] = json.dumps([resource_id])
    return True


def get_handler(response):
    print response.text
    res = json.loads(response.text)
    if res['error_code'] != 0 or len(res['data']['list']) == 0:
        return False
    return True


TEST = {
        'name': 'Message Get API using list',
        'request': [
            {
                'method': 'POST',
                'url': '/a/v6/data/message/getfolderlist',
                'timeout': 60
            },
            {
                'method': 'POST',
                'url': '/a/v6/data/message/list',
                'data': {'ts': int(time.time()),
                         'count': 0,
                         'sync_hash': '{}'},
                'timeout': 60,
            },
            {
                'method': 'POST',
                'url': '/a/v6/data/message/get',
                'data': {},
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
                'hooks': list_handler
            },
            {
                'status_code': 200,
                'hooks': get_handler
            }
        ]
}



