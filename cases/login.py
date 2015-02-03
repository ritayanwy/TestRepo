import json
from testcases import TEST_ENV


def handler(response):
    print response.text
    if json.loads(response.text)['error_code'] != 0:
        return False
    TEST_ENV['global_headers']['X-CMSESSION'] = json.loads(response.text)['data']['access_tokens']['CMSESSION']
    TEST_ENV['global_headers']['X-CMSID'] = json.loads(response.text)['data']['access_tokens']['CMSID']
    return True


TEST = {
        'name': 'Login API',
        'request': [
        {
                'method': 'POST',
                'url': '/k/v6/user/session_create?ct=pi&cv=6.5.0&pv=8.2.2',
                'timeout': 60,
                'data': {'email': 'webyogiritayan@gmail.com',
                         'password': 'webyog',
                         'udi':'EE5004D15CC2627B87937DE8CFB6B7DE41E56F5F',
                         'model_name': 'ritayans ipad'
                         }
        }
        ],
        'response': [
        {
                'status_code': 200,
                'hooks': handler
        }
        ]
}



