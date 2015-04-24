import json

def account_handler(response):
    print response.text
    res = json.loads(response.text)
    if res['error_code'] != 0:
        return False
   # for accounts in res['data']['account_groups']:
       # if accounts['display_name'] == 'webyogiritayan@gmail.com':
          #  for types in accounts[accounts]:
             #   if types['category'] == 'people':
                #    TEST['request'][1]['data']['syncstate'][0]['account_id'].append(types['id'])
    return True

def peoplesync_handler(response):
    print response.text
    res = json.loads(response.text)
    if res['error_code'] != 0:
        return False
    print len(res['data']['list'][0]['list'])
    return True

TEST = {
        'name': 'PeopleSync API',
        'request': [
            {
                'method': 'POST',
                'url': '/k/v5/account/details',
                'timeout': 60,
            },
            {
                'method': 'POST',
                'url': '/a/v5/data/people/sync',
                'data': {'syncstate':'[{"account_id":2 , "offset":0, "sync_hash":"0"}]', 'rank_update':0},
                'timeout': 60,
            }
        ],
        'response': [
            {
                'status_code': 200,
                'hooks': account_handler
            },
            {
                'status_code': 200,
                'hooks': peoplesync_handler
            }
        ]
}