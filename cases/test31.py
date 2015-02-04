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
    pref = res['data']['preference']['account']['13']
    if res['data']['preference']['general']['app_badge']!=0 or pref['nickname']!='string' or pref['auto_attachment_download']!="always" or pref['signature']!='API Testing' or pref['color']!='Turquoise' or pref['sent_using_cm']!=0 or pref['notifiable_folder'][0]['notification_sound']!=3:
        return False
    return True


TEST = {
    'name': 'PreferenceAPI set get match check',
    'request': [
                    {   'method': 'POST',
                        'url': '/k/v6/preference/set',
                        'data': {
                            'changes':'[{"change":{"account":{"13":{"nickname":"string","auto_attachment_download":"always","signature":"API Testing","color":"Turquoise","sent_using_cm":0,"notifiable_folder":[{"notification_sound":3}]}},"general":{"app_badge":0}},"type":"merge"}]'
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