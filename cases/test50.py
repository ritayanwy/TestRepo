import json

def password_handler(response):
    print response.text
    res = json.loads(response.text)
    if res['error_code'] != 1003:
        return False
    return True


TEST = {
        'name': 'Account password change(less than 6 characters) check',
        'request': [
            {
                'method': 'POST',
                'url': '/k/v6/user/password/change?ct=ti&cv=6.1.3&pv=8.1.3',
                'data': {
                    'email':'webyogiritayan@gmail.com',
                    'password':'webyog',
                    'new_password':'web',
                    'confirm_password':'web'
                        }
            }
        ],
        'response': [
        {
                'status_code': 200,
                'hooks': password_handler
        }
]}