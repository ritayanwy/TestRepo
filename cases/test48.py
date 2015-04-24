import json

def handler(response):
    print response.text
    res = json.loads(response.text)
    if res['error_code'] != 0:
        return False
    if len(res['data']['account_groups']) <= 0:
        return  False
    if len(res['data']['account_groups'][0]['accounts']) != 2:
        return False
    if res['data']['can_add_more_accounts'] != 1:
        return  False
    return True


TEST = {
        'name': 'Account details(account,message,people,CanAddMoreAccounts) check',
        'request': [
        {
                'method': 'POST',
                'url': '/k/v6/account/details?ct=ti&cv=6.1.3&pv=8.1.3'
        }],
        'response': [
        {
                'status_code': 200,
                'hooks': handler
        }
]}