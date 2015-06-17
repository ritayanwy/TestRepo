import json

def setwipestate_handler1(response):
    print response.text
    res = json.loads(response.text)
    if res['error_code'] != 0:
        return False
    return True

def setwipestate_handler2(response):
    print response.text
    res = json.loads(response.text)
    if res['error_code'] != 0:
        return False
    return True

def setwipestate_handler3(response):
    print response.text
    res = json.loads(response.text)
    if res['error_code'] != 0:
        return False
    return True

def changeget_handler(response):
    print response.text
    res = json.loads(response.text)
    if res['error_code'] != 1006:
        return False
    return True


TEST = {
        'name': 'Remote Wipe API- check if server clears session id after remote wipe',
        'request': [
        {
                'method': 'POST',
                'url': '/v6/device/set_wipe_state',
                'data': {
                    'udi': '5B10FC39-D05E-44EA-B68E-8008054EDA0',
                    'wipe_status': 'requested'
                }
        },
        {
                'method': 'POST',
                'url': '/v6/device/set_wipe_state',
                'data': {
                    'udi': '5B10FC39-D05E-44EA-B68E-8008054EDA0',
                    'wipe_status': 'client_initiated'
                }
        },
        {
                'method': 'POST',
                'url': '/v6/device/set_wipe_state',
                'data': {
                    'udi': '5B10FC39-D05E-44EA-B68E-8008054EDA0',
                    'wipe_status': 'client_completed'
                }
        },
        {
                'method': 'POST',
                'url': '/k/v6/change/get'
        }
        ],
        'response': [
        {
                'status_code': 200,
                'hooks': setwipestate_handler1
        },
        {
                'status_code': 200,
                'hooks': setwipestate_handler2
        },
        {
                'status_code': 200,
                'hooks': setwipestate_handler3
        },
        {
                'status_code': 200,
                'hooks': changeget_handler
        }
        ]
}

