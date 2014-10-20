__author__ = 'anurag'
import json
import time

def folderlist_handler(response):
    print response.text
    res = json.loads(response.text)
    if res['error_code'] != 0:
        return False
    sync_info = [{'sync_hash': '', 'account_id': -1}]
    if len(res['data']['list']) > 0 and len(res['data']['list'][0]['list']) > 0:
        sync_info[0]['account_id'] = res['data']['list'][0]['account_id']
        for folder in res['data']['list'][0]['list']:
            if folder['is_syncable'] == 1:
                sync_info[0]['mailbox_path'] = folder['mailbox_path']
                sync_info[0]['label'] = folder['label']
                break
        if sync_info[0].get('mailbox_path') is None:
            return False
    TEST['request'][1]['data']['sync_info'] = json.dumps(sync_info)
    return True


def sync_handler(response):
    print response.text
    res = json.loads(response.text)
    if res['error_code'] != 0 or len(res['data']['list']) == 0:
        return False
    account_id = res['data']['list'][0]['account_id']
    resource_id = res['data']['list'][0]['list'][0]['resource_id']
    TEST['request'][2]['data']['account_id'] = account_id
    TEST['request'][2]['data']['resource_id'] = json.dumps([resource_id])
    return True


def preview_handler(response):
    print response.text
    res = json.loads(response.text)
    if res['error_code'] != 0 or len(res['data']['list']) == 0:
        return False
    return True


TEST = {
        'name': 'Preview API with resource id',
        'request': [
            {
                'method': 'POST',
                'url': '/a/v5/data/message/getfolderlist',
                'timeout': 60
            },
            {
                'method': 'POST',
                'url': '/a/v5/data/message/sync',
                'data': {},
                'timeout': 60,
            },
            {
                'method': 'POST',
                'url': '/a/v5/data/message/preview',
                'data': {'ts': int(time.time()),
                         'show_all': 1},
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
                'hooks': sync_handler
            },
            {
                'status_code': 200,
                'hooks': preview_handler
            }
        ]
}



