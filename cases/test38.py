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
    if res['data']['preference']['general']['app_badge']!=5:
        return False
    return True


TEST = {
    'name': 'PreferenceAPI set garbage data level 1 check',
    'request': [
                    {   'method': 'POST',
                        'url': '/k/v6/preference/set',
                        'data': {
                            'changes':'[{"change":{"general":{"app_badge":5}},"type":"set"}]'
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