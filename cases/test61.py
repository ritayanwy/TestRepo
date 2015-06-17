import json
import time

hash1 = ''
counter = 0

def folderlist_handler(response):
    print response.text
    res = json.loads(response.text)
    if res['error_code'] != 0:
        return False
    TEST['request'][2]['data']['account_id'] = res['data']['list'][0]['account_id']
    return True

def changeget_handler1(response):
    print response.text
    res = json.loads(response.text)
    if res['error_code'] != 0:
        return False
    global hash1
    print type(hash1 )
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
    if len(res['data']['change']) > 0 and res['data']['change'][0]['type'] == 'message_new':
        return True

    TEST['request'].append({'method': 'POST', 'url': '/k/v6/change/get', 'data':{'hash': hash1 }})
    TEST['response'].append({'status_code': 200, 'hooks': changeget_handler2})
    time.sleep(5)
    global counter
    counter += 1
    if counter >=5:
        return False
    return True


payload = {
    "from": "webyogiritayan@gmail.com",
    "to": ["The terminator <ritayan.das@webyog.com>"],
    "cc": ["ritayan90@gmail.com"],
    "body": "",
    "body_text": "",
    "is_body_html": 1,
    "subject": "",
    "ts_compose": int(time.time()),
    "timezone_offset": 19800,
    "attachment": [],
    "sent_folder_info": {
        "label": "\\Sent",
        "mailbox_path": "[Gmail]/All Mail",
    }
}


TEST = {
    'name': 'compose with blank subject,body,bodytext and GetChange check',
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
                     'payload': json.dumps(payload),
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