import json

def preferenceget_handler(response):
    print response.text
    res = json.loads(response.text)
    if res['error_code'] != 0:
        return False
    return True




TEST = {
    'name': 'Preference get api',
    'request': [
                    {   'method': 'POST',
                        'url': '/k/v6/preference/get',
                    }
                ],
    'response': [
                 {
                  'status_code': 200,
                  'hooks': preferenceget_handler
                  }
                ]
       }