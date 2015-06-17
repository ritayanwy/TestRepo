__author__ = 'anurag'
import json

#test git commet
#cooment 2

def handler(response):
    print response.text
    if json.loads(response.text)['error_code'] != 0:
        return False
    return True


#<request>
'''self, method, url,
        params=None,
        data=None,
        headers=None,
        cookies=None,
        files=None,
        auth=None,
        timeout=None,
        allow_redirects=True,
        proxies=None,
        hooks=None,
        stream=None,
        verify=None,
        cert=None'''


TEST = {
        'name': 'GetFolderList API',
        'request': [
        {
                'method': 'POST',
                'url': '/a/v5/data/message/getfolderlist',
                'timeout': 60,
        }
        ],
        'response': [
        {
                'http_status': 200,
                'hooks': handler
        }
        ]
}
