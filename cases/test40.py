import json

def preferenceset_handler(response):
    print response.text
    res = json.loads(response.text)
    if res['error_code'] != 0:
        return False
    return True

def preferenceget_handler(response):
    print response.text
    res = json.loads(response.text)
    if res['error_code'] != 0:
        return False
    if len(res['data']['preference']['account']) == 0:
        return False
    return True


TEST = {
    'name': 'PreferenceAPI set,delete,set data in one change - level 2 check',
    'request': [
                    {   'method': 'POST',
                        'url': '/k/v6/preference/set',
                        'data': {
                            'changes':'[{"change":{"account":{"13":{}}},"type":"set"},{"change":{"account":{"13":{}}},"type":"delete"},{"change":{"account":{"13":{}}},"type":"set"}]'
                        }
                    },
                    {   'method': 'POST',
                        'url': '/k/v6/preference/get'
                    }
                ],
    'response': [
                 {
                  'status_code': 200,
                  'hooks': preferenceset_handler
                  },
                 {
                  'status_code': 200,
                  'hooks': preferenceget_handler
                  }
                ]
       }