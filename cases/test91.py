import json
import time

mailbox_path = None
account_id = None
hash1 = ''
counter = 0
clv = ''
ResourceId = None

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
            if folder['folder_type'] == 0:
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
    email = res['data']['list'][1]
    TEST['request'][3]['data']['account_id'].append(account_id)
    TEST['request'][3]['data']['payload'].append(json.dumps({'account_id':account_id,'reference_folder_info':{'is_trash':0,'mailbox_path':mailbox_path},'conversation_id': email['conversation_id'],'resource_id':email['resource_id'],'destination_folder_info':{'is_trash':0,'mailbox_path':"[Gmail]/All Mail"}}))
    global ResourceId
    ResourceId = email['resource_id']
    return True

def changeget_handler1(response):
    print response.text
    res = json.loads(response.text)
    if res['error_code'] != 0:
        return False
    global hash1
    global clv
    hash1 = res['data']['hash']
    clv = res['data']['clv']
    TEST['request'][4]['data']['hash'] = hash1
    TEST['request'][4]['data']['clv'] = clv
    return True

def Archive_handler(response):
    print response.text
    res = json.loads(response.text)
    if res['error_code'] != 0:
        return False
    return True

def changeget_handler2(response):
    print response.text
    res = json.loads(response.text)
    if res['error_code'] != 0:
        return False
    if len(res['data']['change']) > 0 :
        for changes in res['data']['change']:
            if changes['type'] == 'message_delete':
                if changes['payload'][0]['resource_id'] == ResourceId:
                    return True

    TEST['request'].append({'method': 'POST', 'url': '/k/v6/change/get', 'data':{'hash': hash1, 'clv': clv }})
    TEST['response'].append({'status_code': 200, 'hooks': changeget_handler2})
    time.sleep(5)
    global counter
    counter += 1
    if counter >=5:
        return False
    return True

TEST = {
        'name': 'ActionSetAPI-Archive an email in Inbox',
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
                'url': '/k/v6/change/get'
            },
            {
            'method': 'POST',
            'url': '/k/v6/action/set',
            'data': {'action_token': int(time.time()),
                     'action_type': 'archive',
                     'payload': [],
                     'account_id': []
                    },
            'timeout': 60
            },
            {
                'method': 'POST',
                'url': '/k/v6/change/get',
                'data': { }
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
                'hooks': changeget_handler1
            },
            {
                'status_code': 200,
                'hooks': Archive_handler
            },
            {
                'status_code': 200,
                'hooks': changeget_handler2
            }
        ]
}



