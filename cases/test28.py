import json

global ProfilePicLink

def profilepic_handler(response):
    print response.text
    res = json.loads(response.text)
    if res['error_code'] != 0:
        return False
    global ProfilePicLink
    ProfilePicLink = res['data']['profile_pic_urls'][0]
    TEST['request'][1]['data']['profile_pic'] = ProfilePicLink
    if ProfilePicLink == None:
        return False
    return True

def profileinfoset_handler(response):
    print response.text
    res = json.loads(response.text)
    if res['error_code'] != 0:
        return False
    return True

def profileinfoget_handler(response):
    print response.text
    res = json.loads(response.text)
    if res['error_code'] != 0:
        return False
    global ProfilePicLink
    print res['data']['profile_pic']
    if ProfilePicLink != res['data']['profile_pic']:
        return False
    return True

TEST = {
    'name': 'ProfilePic set get from server check',
    'request': [
        {   'method': 'POST',
            'url': '/k/v6/profile/get_available_profile_pics',
        },
        {   'method': 'POST',
            'url': '/k/v6/profileinfo/set',
            'data': {
                    'nickname': 'TestAccount',
                    }
        },
        {   'method': 'POST',
            'url': '/k/v6/profileinfo/get',
        }
    ],
        'response': [
            {
                'status_code': 200,
                'hooks': profilepic_handler
            },
            {
                'status_code': 200,
                'hooks': profileinfoset_handler
            },
            {
                'status_code': 200,
                'hooks': profileinfoget_handler
            }
    ]


}

class Cm_Url:

    @staticmethod
    def factory(self, path):
        self.path = path
        return self

    def add_ct(self, ct):
        self.ct = ct
        return self