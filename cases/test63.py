import json
import time

hash1 = ''
counter = 0
resource_id = 0
account_id = 0

def folderlist_handler(response):
    print response.text
    res = json.loads(response.text)
    if res['error_code'] != 0:
        return False
    global account_id
    account_id = res['data']['list'][0]['account_id']
    TEST['request'][2]['data']['account_id'] = account_id
    return True

def changeget_handler1(response):
    print response.text
    res = json.loads(response.text)
    if res['error_code'] != 0:
        return False
    global hash1
    hash1 = res['data']['hash']
    TEST['request'][3]['data']['hash'] = hash1
    return True

def compose_handler(response):
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
    global resource_id
    if len(res['data']['change']) > 0 and res['data']['change'][0]['type'] == 'message_new':
        resource_id = res['data']['change'][0]['payload'][0]['resource_id']
        TEST['request'].append({'method': 'POST','url': '/k/v6/action/set','data': {'action_token': int(time.time()),'account_id': account_id,'action_type': 'reply','payload': json.dumps(payload2),},'timeout': 60})
        TEST['response'].append({'status_code': 200,'hooks': reply_handler})
        print resource_id
        return True
    else:
        TEST['request'].append({'method': 'POST', 'url': '/k/v6/change/get', 'data':{'hash': hash1 }})
        TEST['response'].append({'status_code': 200, 'hooks': changeget_handler2})
        time.sleep(5)
        global counter
        counter += 1
        if counter >=5:
            return False
        return  True


def reply_handler(response):
    print response.text
    res = json.loads(response.text)
    if res['error_code'] != 0:
        return False
    return True


payload1 = {
    "from": "webyogiritayan@gmail.com",
    "to": ["ritayan.das@webyog.com","ritayan.das@outlook.com"],
    "cc": ["ritayan90@gmail.com","ritayan@dascorp.onmicrosoft.com"],
    "bcc": ["ritayan90@icloud.com","webyogiritayan@gmail.com"],
    "body": "<div>compose <b>text</b></div>",
    "body_text": "compose text",
    "is_body_html": 1,
    "subject": "Reply check",
    "ts_compose": int(time.time()),
    "timezone_offset": 19800,
    "attachment": [],
    "sent_folder_info": {
        "label": "\\Sent",
        "mailbox_path": "[Gmail]/All Mail",
    }
}

payload2 = {
    "from": "webyogiritayan@gmail.com",
    "to": ["The terminator <ritayan.das@webyog.com>"],
    "cc": ["ritayan90@gmail.com"],
    "body": "reply text",
    "body_text": "test email 1",
    "is_body_html": 1,
    "subject": "Reply check",
    "ts_compose": int(time.time()),
    "timezone_offset": 19800,
    "attachment": [],
    "sent_folder_info": {
        "label": "\\Sent",
        "mailbox_path": "[Gmail]/All Mail",
    },
    'is_starred': 0,
    'reference_resource_id': json.dumps(resource_id)
}

TEST = {
    'name': 'Compose,GetChange and Reply check{removing 1 to,1 cc,all bcc}',
    'request': [{
                'method': 'POST',
                'url': '/a/v6/data/message/getfolderlist',
                'timeout': 60
            },
                {
                'method': 'POST',
                'url': '/k/v6/change/get'
        },
        {
            'method': 'POST',
            'url': '/k/v6/action/set',
            'data': {'action_token': int(time.time()),
                     'action_type': 'compose',
                     'payload': json.dumps(payload1),
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
                'hooks': changeget_handler1
        },
        {
                'status_code': 200,
                'hooks': compose_handler
        },
        {
                'status_code': 200,
                'hooks': changeget_handler2
        }
    ]
}