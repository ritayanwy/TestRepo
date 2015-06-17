import json

def password_handler1(response):
    print response.text
    res = json.loads(response.text)
    if res['error_code'] != 0:
        return False
    return True

def password_handler2(response):
    print response.text
    res = json.loads(response.text)
    if res['error_code'] != 0:
        return False
    return True


TEST = {
        'name': 'Account password change(long password,special characters) check',
        'request': [
            {
                'method': 'POST',
                'url': '/k/v6/user/password/change?ct=ti&cv=6.1.3&pv=8.1.3',
                'data': {
                    'email':'webyogiritayan@gmail.com',
                    'password':'webyog',
                    'new_password':'@#$%^&*()!qwertergegnew;bnerbn eribheriqbeornneronb1234567890',
                    'confirm_password':'@#$%^&*()!qwertergegnew;bnerbn eribheriqbeornneronb1234567890'
                        }
            },{
                'method': 'POST',
                'url': '/k/v6/user/password/change?ct=ti&cv=6.1.3&pv=8.1.3',
                'data': {
                    'email':'webyogiritayan@gmail.com',
                    'password':'@#$%^&*()!qwertergegnew;bnerbn eribheriqbeornneronb1234567890',
                    'new_password':'webyog',
                    'confirm_password':'webyog'
                        }
            }
        ],
        'response': [
        {
                'status_code': 200,
                'hooks': password_handler1
        },
        {
                'status_code': 200,
                'hooks': password_handler2
        }
]}