import json

def getdetails_handler(response):
    print response.text
    res = json.loads(response.text)
    if res['error_code'] != 0:
        return False
    index = 0
    for devices in res['data']:
        TEST['request'][2]['data'][index]['udi'] == res['data'][index]['udi']
        print TEST['request'][2]['data'][index]['udi']
        index = index + 1
    return True

def initiatewipe_handler(response):
    print response.text
    res = json.loads(response.text)
    if res['error_code'] != 0:
        return False
    return True


TEST = {
        'name': 'Remote Wipe API actual',
        'request': [
        {
                'method': 'POST',
                'url': '/v6/device/get_details'
        }
        ,
        {
                'method': 'POST',
                'url': '/v6/device/initiate_wipe',
                'data': ''
        }
        ],
        'response': [
        {
                'status_code': 200,
                'hooks': getdetails_handler
        },
        {
                'status_code': 200,
                'hooks': initiatewipe_handler
        }
        ]
}

