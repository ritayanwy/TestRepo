import json

def getdetails_handler(response):
    print response.text
    res = json.loads(response.text)
    if res['error_code'] != 0:
        return False
    print res['data'][0]['udi']
    TEST['request'][2]['data']['udi'] = res['data'][0]['udi']
    return True

def changeget_handler1(response):
    print response.text
    res = json.loads(response.text)
    if res['error_code'] != 0:
        return False
    print res['data']['hash']
    TEST['request'][3]['data']['hash'] = res['data']['hash']
    return True

def initiatewipe_handler(response):
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
    if len(res['data']['change']) == 0:
        return False
    return True


TEST = {
        'name': 'Remote Wipe API- Check change log from ChangeGet after doing RemoteWipe Check',
        'request': [
        {
                'method': 'POST',
                'url': '/v6/device/get_details'
        },
        {
                'method': 'POST',
                'url': '/k/v6/change/get'
        },
        {
                'method': 'POST',
                'url': '/v6/device/initiate_wipe',
                'data': { }
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
                'hooks': getdetails_handler
        },
        {
                'status_code': 200,
                'hooks': changeget_handler1
        },
        {
                'status_code': 200,
                'hooks': initiatewipe_handler
        },
        {
                'status_code': 200,
                'hooks': changeget_handler2
        }
        ]
}

