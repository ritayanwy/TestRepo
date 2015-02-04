import json

def preferenceset_handler(response):
    print response.text
    res = json.loads(response.text)
    if res['error_code'] != 0:
        return False
    return True

def preferenceget_handler(response):
    print response.text
    res = json.loads(response.text)
    if res['error_code'] != 0:
        return False
    if res['data']['preference']['account']['13']['notifiable_folder'][0]['notification_sound'] != 4 or res['data']['preference']['account']['13']['notifiable_folder'][1]['label'] != 'Parent folder':
        return False
    return True


TEST = {
    'name': 'PreferenceAPI set,delete,set data in one change - level 3 check',
    'request': [
                    {   'method': 'POST',
                        'url': '/k/v6/preference/set',
                        'data': {
                            'changes':'[{"change":{"account":{"13":{"notifiable_folder":[{"notification_sound":3},{"label":"Parent folder","mailbox_path":"[Gmail]/All Mail"}]}}},"type":"set"},{"change":{"account":{"13":{"notifiable_folder":[{"notification_sound":3},{"label":"Parent folder","mailbox_path":"[Gmail]/All Mail"}]}}},"type":"delete"},{"change":{"account":{"13":{"notifiable_folder":[{"notification_sound":4},{"label":"Parent folder","mailbox_path":"[Gmail]/All Mail"}]}}},"type":"set"}]'
                        }
                    },
                    {   'method': 'POST',
                        'url': '/k/v6/preference/get'
                    }
                ],
    'response': [
                 {
                  'status_code': 200,
                  'hooks': preferenceset_handler
                  },
                 {
                  'status_code': 200,
                  'hooks': preferenceget_handler
                  }
                ]
       }