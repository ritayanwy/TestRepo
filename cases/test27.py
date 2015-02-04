import json

def profilepic_handler(response):
    print response.text
    res = json.loads(response.text)
    if res['error_code'] != 0:
        return False
    return True


TEST = {
    'name': 'ProfilePic fetching check',
    'request': [
                    {   'method': 'POST',
                        'url': '/k/v6/profile/get_available_profile_pics',
                    }
                ],
    'response': [{
                'status_code': 200,
                'hooks': profilepic_handler
                 }
                ]
       }