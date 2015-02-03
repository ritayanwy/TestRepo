
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
                TEST['request'][2]['data']['mailbox_path'] = folder['mailbox_path']
                TEST['request'][1]['data']['folder'] = folder['label']
                break
        if TEST['request'][1]['data'].get('mailbox_path') is None:
            return False
    return True


def search_handler(response):
    print response.text
    res = json.loads(response.text)
    if res['error_code'] != 0 or len(res['data']['list']) == 0:
        return False
    account_id = res['data']['list'][0]['account_id']
    conversation_id = res['data']['list'][0]['conversation_id']
    TEST['request'][2]['data']['account_id'] = account_id
    TEST['request'][2]['data']['conversation_id'] = conversation_id
    return True


def preview_handler(response):
    print response.text
    res = json.loads(response.text)
    global sync_info
    if res['error_code'] != 0 or len(res['data']['list']) != 5:
        return False
    return True

TEST = {
        'name': 'Search conversation email previews check',
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
                         'query': 'email to test search conversation',
                         'sync_hash': '{}'},
                'timeout': 60,
            },
            {
                'method': 'POST',
                'url': '/a/v6/data/message/preview',
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
                'hooks': search_handler
            },
            {
                'status_code': 200,
                'hooks': preview_handler
            }
        ]
}



