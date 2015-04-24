import json


sync_folder = []
def folderlist_handler(response):
    print response.text
    res = json.loads(response.text)
    if res['error_code'] != 0:
        return False

    sync_info = [{'sync_hash': '', 'account_id': -1}]
    if len(res['data']['list']) > 0 and len(res['data']['list'][0]['list']) > 0:
        sync_info[0]['account_id'] = res['data']['list'][0]['account_id']
    TEST['request'][1]['data']['sync_info'] = json.dumps(sync_info)

    account_no=0
    global sync_folder
    sync_folder = [[0 for column_no in range(3)] for row_no in range(len(res['data']['list']))]
    for account in res['data']['list']:
        for folder in account["list"]:
            if folder ['folder_type'] == 0:   #inbox
                sync_folder[account_no].append(folder['id'])
            if folder ['folder_type'] == 5:   #starred
                sync_folder[account_no].append(folder['id'])
            if folder ['folder_type'] == 1:   #sentmail
                sync_folder[account_no].append(folder['id'])
        account_no = account_no+1
    return True


def sync_handler(response):
    print response.text
    res = json.loads(response.text)
    for accounts in res['data']['list']:
        for emails in accounts['list']:
            folder_present = False
            for sync_folder_single_row in sync_folder:
                for folderid in sync_folder_single_row:
                    if folderid in emails['folder_list']:
                        folder_present = True

            if folder_present is False:
                return False

    return True



TEST = {
        'name': 'Sync API - Sync folder email folderId check',
        'request': [
            {
                'method': 'POST',
                'url': '/a/v6/data/message/getfolderlist',
                'timeout': 60
            },
            {
                'method': 'POST',
                'url': '/a/v6/data/message/sync',
                'data': {},
                'timeout': 60,
            }
        ],
        'response': [
            {
                'status_code': 200,
                'hooks': folderlist_handler
            },
            {
                'status_code': 200,
                'hooks': sync_handler
            }
        ]
}
