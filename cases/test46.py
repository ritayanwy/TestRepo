import json

def initiatewipe_handler(response):
    print response.text
    res = json.loads(response.text)
    if res['error_code'] != 0:
        return False
    return True


TEST = {
        'name': 'Remote Wipe API- Initiate Wipe check',
        'request': [
        {
                'method': 'POST',
                'url': '/v6/device/initiate_wipe',
                'data': {'udi':'EE5004D15CC2627B87937DE8CFB6B7DE41E56F5F'}
        }],
        'response': [
        {
                'status_code': 200,
                'hooks': initiatewipe_handler
        }
]}