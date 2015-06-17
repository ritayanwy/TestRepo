import json

def password_handler(response):
    print response.text
    res = json.loads(response.text)
    if res['error_code'] != 0:
        return False
    return True


TEST = {
        'name': 'Password reset check',
        'request': [
            {
                'method': 'POST',
                'url': '/k/v6/user/password/reset_request?ct=ti&cv=6.1.3&pv=8.1.3',
                'data': {'email':'webyogiritayan@gmail.com'}
            }
        ],
        'response': [
        {
                'status_code': 200,
                'hooks': password_handler
        }
]}