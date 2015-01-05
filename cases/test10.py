import json
from testcases import TEST_ENV


def handler(response):
    print response.text
    res = json.loads(response.text)
    if json.loads(response.text)['error_code'] != 0:
        return False

    for account in res['data']['list']:
        for folder in account["list"]:
            if folder ['name'] == 'parent folder' :
                for subfolderlevel1 in folder['list']:
                    if subfolderlevel1 ['name'] == 'child folder 1' and subfolderlevel1 ['parent_id'] != folder ['id']:
                        return False
                    for subfolderlevel2 in subfolderlevel1['list']:
                        if subfolderlevel2 ['name'] == 'child folder 2' and subfolderlevel2 ['parent_id'] != subfolderlevel1 ['id']:
                            return False

    return True



TEST = {
        'name': 'GetFolderList API - Parent Child Relation',
        'request': [
        {
                'method': 'POST',
                'url': '/a/v5/data/message/getfolderlist',
                'timeout': 60
        }
        ],
        'response': [
        {
                'status_code': 200,
                'hooks': handler
        }
        ]
}
