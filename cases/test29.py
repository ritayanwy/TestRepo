import json

def reasonsapi_handler_pad(response):
    print response.text
    res = json.loads(response.text)
    if res['error_code'] != 0:
        return False
    if len(res['data']['url_list'])!= 7:
        return False
    return True




TEST = {
    'name': 'Reasons API all images present check',
    'request': [
                    {   'method': 'POST',
                        'url': '/k/v6/reasonstopay/get?pm=pad&cv=5.1.6.5&pv=4.2.2&ct=ti',
                    }
                ],
    'response': [
                 {
                  'status_code': 200,
                  'hooks': reasonsapi_handler_pad
                  }
                ]
       }