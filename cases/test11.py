import json
from testcases import TEST_ENV


def handler(response):
    print response.text
    res = json.loads(response.text)
    if json.loads(response.text)['error_code'] != 0:
        return False

    for account in res['data']['list']:
        for folder in account["list"]:
            if folder ["folder_type"] == 0 and folder ["folder_rank"] != 1:  #inbox
              return False
            if folder ["folder_type"] == 1 and folder ["folder_rank"] != 4:  #sentmail
              return False
            if folder ["folder_type"] == 3 and folder ["folder_rank"] != 11: #trash
              return False
            if folder ["folder_type"] == 4 and folder ["folder_rank"] != 8:  #allmail
              return False
            if folder ["folder_type"] == 5 and folder ["folder_rank"] != 2:  #starred
              return False
            if folder ["folder_type"] == 7 and folder ["folder_rank"] != 10: #spam
              return False
            if folder ["folder_type"] == 8 and folder ["folder_rank"] != 3:  #important
              return False

    return True



TEST = {
        'name': 'GetFolderList API - Folder rank',
        'request': [
        {
                'method': 'POST',
                'url': '/a/v6/data/message/getfolderlist',
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


