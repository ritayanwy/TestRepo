import json
import time

def folderlist_handler(response):
    print response.text
    res = json.loads(response.text)
    if res['error_code'] != 0:
        return False
    TEST['request'][1]['data']['account_id'] = res['data']['list'][0]['account_id']
    return True

def compose_handler(response):
    print response.text
    res = json.loads(response.text)
    if res['error_code'] != 0:
        return False
    return True

payload = {
    "from": "webyogiritayan@gmail.com",
    "to": ["The terminator <ritayan.das@webyog.com>"],
    "bcc": ["suraj.sharma@webyog.com"],
    "cc": ["ritayan90@gmail.com"],
    "body": "body of the mail",
    "body_text": "test email 1",
    "is_body_html": 1,
    "subject": "Test email",
    "ts_compose": int(time.time()),
    "timezone_offset": 19800,
    "attachment": [],
    "sent_folder_info": {
        "label": "\\Sent",
        "mailbox_path": "[Gmail]/All Mail",
    }
}

TEST = {
    'name': 'compose check',
    'request': [{
                'method': 'POST',
                'url': '/a/v6/data/message/getfolderlist',
                'timeout': 60
            },
        {
            'method': 'POST',
            'url': '/k/v6/action/set',
            'data': {'action_token': int(time.time()),
                     'action_type': 'compose',
                     'payload': json.dumps(payload),
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
            'hooks': compose_handler
        }
    ]
}