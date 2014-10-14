cm-kangaroo
===========

CM test framework

This is a generic REST API test framework written in python.

To run

    python start.py --input testcases.py --threads=1

Sample testcases.py

    def init_handler(global_headers, global_post_param, global_query_param):
        global_headers['X-REST-API'] = 'testing'
        return True
    
    
    TEST_ENV = {
        'project_name': 'CloudMagic Gamma - Sync APIs',
        'global_headers': {},
        'global_post_param': {},
        'global_query_param': {},
        'init_hooks': init_handler,
        'global_info': {},
        'domain': 'api-gamma.cloudmagic.com',
        'protocol': 'https',
        'testcases': [
            'login.py',
            'test1.py',
            'test2.py',
        ]
    }
    
  

Sample test.py

    import json
    
    
    def handler(response):
        print response.text
        if json.loads(response.text)['error_code'] != 0:
            return False
        return True
    
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
    

