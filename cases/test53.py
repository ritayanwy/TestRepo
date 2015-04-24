import json

def password_handler(response):
    print response.text
    res = json.loads(response.text)
    if res['error_code'] != 1003:
        return False
    return True


TEST = {
        'name': 'Password create for an account with password check',
        'request': [
            {
                'method': 'POST',
                'url': '/k/v6/user/password/create?ct=ti&cv=6.1.3&pv=8.1.3',
                'data': {'new_password':'webyog',
                         'confirm_password':'webyog'
                        }
            }
        ],
        'response': [
        {
                'status_code': 200,
                'hooks': password_handler
        }
]}