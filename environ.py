params = {  'PROD_MSHOST' : 'SQLSERVER.DEMO.COM',
            'PROD_MSUSER' : 'AdvWrks',
            'PROD_MSPASS' : 'StrongPasswordPROD',
            'PROD_MSDB' : 'AdvWrks',
            'PROD_HOST' : 'prod.demo.com',
            'PROD_PORT' : 443,
            'PROD_RELOAD' : False,
            'PROD_DEBUG' : False,
            
            'UIT_MSHOST' : 'DEVSQLSERVER.DEMO.COM',
            'UIT_MSUSER' : 'AdvWrks',
            'UIT_MSPASS' : 'StrongPasswordUIT',
            'UIT_MSDB' : 'AdvWrks',
            'UIT_HOST' : 'localhost',
            'UIT_PORT' : 8000,
            'UIT_RELOAD' : True,
            'UIT_DEBUG' : True,
            }

envName = 'UIT'

def GetValue(name):
    value = params.get(envName + '_' + name)
    if value is not None:
        return value
    return None
