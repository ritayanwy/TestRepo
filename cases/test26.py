import json
import time

def profileinfoset_handler1(response):
    print response.text
    res = json.loads(response.text)
    if res['error_code'] != 0:
        return False
    return True

def profileinfoget_handler1(response):
    print response.text
    res = json.loads(response.text)
    if res['error_code'] != 0:
        return False
    if res['data']['nickname']!= 'TestAccount1' or res['data']['profile_pic']!= 'arbitrary string1':
        return False
    return True

def profileinfoset_handler2(response):
    print response.text
    res = json.loads(response.text)
    if res['error_code'] != 0:
        return False
    return True

def profileinfoget_handler2(response):
    print response.text
    res = json.loads(response.text)
    if res['error_code'] != 0:
        return False
    for iteration in range (3):
        if res['data']['nickname']!= 'TestAccount2' or res['data']['profile_pic']!= 'arbitrary string2':
            iteration=iteration+1
            if iteration==2:
                return False
            time.sleep(120)
    return True

TEST = {
    'name': 'ProfileInfo set get iteration check',
    'request': [
        {   'method': 'POST',
            'url': '/k/v6/profileinfo/set',
            'data': {
                    'nickname': 'TestAccount1',
                    'profile_pic': 'arbitrary string1',
                    }
        },
        {   'method': 'POST',
            'url': '/k/v6/profileinfo/get',
        },
        {   'method': 'POST',
            'url': '/k/v6/profileinfo/set',
            'data': {
                    'nickname': 'TestAccount2',
                    'profile_pic': 'arbitrary string2',
                    }
        },
        {   'method': 'POST',
            'url': '/k/v6/profileinfo/get',
        }
    ],
        'response': [
            {
                'status_code': 200,
                'hooks': profileinfoset_handler1
            },
            {
                'status_code': 200,
                'hooks': profileinfoget_handler1
            },
            {
                'status_code': 200,
                'hooks': profileinfoset_handler2
            },
            {
                'status_code': 200,
                'hooks': profileinfoget_handler2
            }
    ]
}