

def init_handler(global_headers, global_post_param, global_query_param):
    global_headers['X-REST-API'] = 'testing'
    return True


TEST_ENV = {
    'project_name': 'CloudMagic APIs',
    'global_headers': {},
    'global_post_param': {},
    'global_query_param': {'cv':'6.0.1'},
    'init_hooks': init_handler,
    'global_info': {},
    'smtp_setting': {},
    'domain': 'api-staging.cloudmagic.com',
    'protocol': 'https',
    'testcases': [
        'cases.login.py',
        'cases.test25.py',
        'cases.test26.py',
        'cases.test27.py',
        'cases.test28.py',
        'cases.test29.py',
        'cases.test30.py',
        'cases.test31.py',
        'cases.test32.py',
        'cases.test33.py',
        'cases.test34.py',
        'cases.test35.py',
        'cases.test36.py',
        'cases.test37.py',
        'cases.test38.py',
        'cases.test39.py',
        'cases.test40.py',
        'cases.test41.py',
        'cases.test42.py',
        'cases.test43.py',
        'cases.login.py',
        'cases.test44.py',
        'cases.login.py',
        'cases.test45.py',
        'cases.login.py',
        'cases.test46.py',
        'cases.login.py',
        'cases.test47.py',
        'cases.test48.py',
        'cases.test49.py',
        'cases.test50.py',
        ]
}
