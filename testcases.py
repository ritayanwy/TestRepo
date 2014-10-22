

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
        'cases.login.py',
        'cases.test1.py',
        'cases.test2.py',
        'cases.test3.py',
        'cases.test4.py',
        'cases.test5.py',
        'cases.test6.py',
        'cases.test7.py'
    ]
}
