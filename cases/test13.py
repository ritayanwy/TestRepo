import json


sync_info = [{'sync_hash': '', 'account_id': -1}]
def folderlist_handler1(response):
    print response.text
    res = json.loads(response.text)
    if res['error_code'] != 0:
        return False

    global sync_info
    if len(res['data']['list']) > 0 and len(res['data']['list'][0]['list']) > 0:
        sync_info[0]['account_id'] = res['data']['list'][0]['account_id']
    TEST['request'][1]['data']['sync_info'] = json.dumps(sync_info)
    return True


def sync_handler1(response):
    print response.text
    res = json.loads(response.text)
    if res['error_code'] != 0:
        return False
    if res['data']['list'][0]['has_more'] == 1:
        sync_info[0]['sync_hash'] = res['data']['list'][0]['sync_hash']
        TEST['request'][2]['data']['sync_info'] = json.dumps(sync_info)
        return True
    return False


def sync_handler2(response):
    print response.text
    res = json.loads(response.text)
    if res['error_code'] != 0:
        return False
    if len (res['data']['list'][0]['list']) <= 0:
        return False
    return True




TEST = {
        'name': 'Sync API - sync folder has_more check',
        'request': [
            {
                'method': 'POST',
                'url': '/a/v6/data/message/getfolderlist',
                'timeout': 60
            },
            {
                'method': 'POST',
                'url': '/a/v6/data/message/sync',
                'data': {},
                'timeout': 60,
            },
            {
                'method': 'POST',
                'url': '/a/v6/data/message/sync',
                'data': {},
                'timeout': 60,
            }
        ],
        'response': [
            {
                'status_code': 200,
                'hooks': folderlist_handler1
            },
            {
                'status_code': 200,
                'hooks': sync_handler1
            },
            {
                'status_code': 200,
                'hooks': sync_handler2
            }
        ]
}