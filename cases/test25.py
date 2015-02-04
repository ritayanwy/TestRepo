import json

def profileinfoset_handler(response):
    print response.text
    res = json.loads(response.text)
    if res['error_code'] != 0:
        return False
    return True

def profileinfoget_handler(response):
    print response.text
    res = json.loads(response.text)
    if res['error_code'] != 0:
        return False
    if res['data']['nickname']!= 'TestAccount' or res['data']['profile_pic']!= 'arbitrary string':
        return False
    return True

TEST = {
    'name': 'profileinfo set get check',
    'request': [
        {   'method': 'POST',
            'url': '/k/v6/profileinfo/set',
            'data': {
                    'nickname': 'TestAccount',
                    'profile_pic': 'arbitrary string',
                    }
        },
        {   'method': 'POST',
            'url': '/k/v6/profileinfo/get',
        }
    ],
        'response': [
            {
                'status_code': 200,
                'hooks': profileinfoset_handler
            },
            {
                'status_code': 200,
                'hooks': profileinfoget_handler
            }
    ]
}