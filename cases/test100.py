import json
import os,sys


def AttachmentUploader(response):
    print response.text
    res = json.loads(response.text)
    if res['error_code'] != 0:
        return False
    return True

filename = 'random_text_file'
path = '/Users/webyog/code/cm-kangaroo/resources/'
file = open(path+filename, 'r')
TEST = {
    'name': 'Attachment Upload',
    'request': [
        {
            'method': 'POST',
            'url': '/k/v6/mailattachment/upload',
            'headers':{
                'X-ACCOUNTID':13,
                'X-CONTENT-TYPE':'text/plain',
                'X-FILENAME':'a.txt'
            },
            'data_binary': 'test',
            'timeout': 60
        }
    ],
    'response': [
        {
            'status_code': 200,
            'hooks': AttachmentUploader
        }
    ]
}