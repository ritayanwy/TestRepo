import json

def getdetails_handler(response):
    print response.text
    res = json.loads(response.text)
    if res['error_code'] != 0:
        return False
    return True


TEST = {
        'name': 'Remote Wipe API- Get Details check',
        'request': [
        {
                'method': 'POST',
                'url': '/v6/device/get_details'
        }],
        'response': [
        {
                'status_code': 200,
                'hooks': getdetails_handler
        }
]}