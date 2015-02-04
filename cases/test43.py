import json

def remotewipe_handler(response):
    print response.text
    res = json.loads(response.text)
    if res['error_code'] != 0:
        return False
    return True



TEST = {
        'name': 'Remote Wipe API test 1',
        'request': [
        {
                'method': 'POST',
                'url': '/v6/device/set_wipe_state',
                'data': {
                    'udi': 'EE5004D15CC2627B87937DE8CFB6B7DE41E56F5F',
                    'wipe_status': 'requested'
                }
        }
        ],
        'response': [
        {
                'status_code': 200,
                'hooks': remotewipe_handler
        }
        ]
}

