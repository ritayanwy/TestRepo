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
                'url': '/k/v5/user/session_create',
                'timeout': 60,
                'data': {'email': 'anurag.shukla@webyog.com',
                         'password': 'AAXXAA'}
        }
        ],
        'response': [
        {
                'status_code': 200,
                'hooks': handler
        }
        ]
}



