import json
import time

mailbox_path = None
account_id = None

def folderlist_handler(response):
    print response.text
    res = json.loads(response.text)
    global mailbox_path
    global account_id
    if res['error_code'] != 0:
        return False
    if len(res['data']['list']) > 0 and len(res['data']['list'][0]['list']) > 0:
        account_id = res['data']['list'][0]['account_id']
        TEST['request'][1]['data']['account_id'] = account_id
        for folder in res['data']['list'][0]['list']:
            if folder['folder_type'] == 999 and folder['name'] == 'Sync folder':
                mailbox_path = folder['mailbox_path']
                TEST['request'][1]['data']['mailbox_path'] = mailbox_path
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
    email = res['data']['list'][0]
    TEST['request'][2]['data']['account_id'].append(account_id)
    TEST['request'][2]['data']['payload'].append(json.dumps({'account_id':account_id,'resource_id':email['resource_id'],'is_body_html':1}))
    return True

def meetingrequest_handler(response):
    print response.text
    res = json.loads(response.text)
    if res['error_code'] != 0:
        return False
    return True

TEST = {
        'name': 'ActionSetAPI- Decline meeting request. Custom folder email',
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
            'url': '/k/v6/action/set',
            'data': {'action_token': int(time.time()),
                     'action_type': 'decline_meeting_request',
                     'payload': [],
                     'account_id': []
                    },
            'timeout': 60
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
                'hooks': meetingrequest_handler
            }
        ]
}



