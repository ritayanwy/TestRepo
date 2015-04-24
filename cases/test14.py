import json


def folderlist_handler(response):
    print response.text
    res = json.loads(response.text)
    if res['error_code'] != 0:
        return False
    sync_info = [{'sync_hash': '', 'account_id': -1, 'mailbox_path': '', 'label': ''}]
    if len(res['data']['list']) > 0 and len(res['data']['list'][0]['list']) > 0:
        sync_info[0]['account_id'] = res['data']['list'][0]['account_id']
        folderindex = -1
        for folders in res['data']['list'][0]['list']:
            folderindex=folderindex+1
            if folders['label'] == 'Sync folder':
                break
        sync_info[0]['mailbox_path'] = res['data']['list'][0]['list'][folderindex]['mailbox_path']
        sync_info[0]['label'] = res['data']['list'][0]['list'][folderindex]['label']
    TEST['request'][1]['data']['sync_info'] = json.dumps(sync_info)
    return True


def sync_handler(response):
    print response.text
    res = json.loads(response.text)
    print len (res['data']['list'][0]['list'])
    if len (res['data']['list'][0]['list']) <= 0:
        return False
    return True


TEST = {
        'name': 'Sync API - sync folder syncing check',
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
            }
        ]
}