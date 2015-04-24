import json

def handler1(response):
    print response.text
    res = json.loads(response.text)
    if res['error_code'] != 0:
        return False
    return True

def handler2(response):
    print response.text
    res = json.loads(response.text)
    if res['error_code'] != 1006:
        return False
    return True

def handler3(response):
    print response.text
    res = json.loads(response.text)
    if res['error_code'] != 0:
        return False
    return True

def handler4(response):
    print response.text
    res = json.loads(response.text)
    if res['error_code'] != 1006:
        return False
    return True


TEST = {
        'name': 'Session destroy with 2 iterations check',
        'request': [
            {
                'method': 'POST',
                'url': '/k/v4/user/session_destroy?ct=ti&cv=6.1.3&pv=8.1.3'
            },
            {
                'method': 'POST',
                'url': '/a/v6/data/message/getfolderlist?ct=ti&cv=6.1.3&pv=8.1.3',
                'timeout': 60
            },
            {
                'method': 'POST',
                'url': '/k/v4/user/session_destroy?ct=ti&cv=6.1.3&pv=8.1.3'
            },
            {
                'method': 'POST',
                'url': '/a/v6/data/message/getfolderlist?ct=ti&cv=6.1.3&pv=8.1.3',
                'timeout': 60
            }
        ],
        'response': [
        {
                'status_code': 200,
                'hooks': handler1
        },
        {
                'status_code': 200,
                'hooks': handler2
        },
        {
                'status_code': 200,
                'hooks': handler3
        },
        {
                'status_code': 200,
                'hooks': handler4
        }
]}