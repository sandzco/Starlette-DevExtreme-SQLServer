import pymssql, environ

class dbs:
    def __init__(self):
        self._conn = pymssql.connect(environ.GetValue('MSHOST'),
                                     environ.GetValue('MSUSER'),
                                     environ.GetValue('MSPASS'), 
                                     environ.GetValue('MSDB'),
                                     as_dict=True, autocommit=True)
        self._cursor = self._conn.cursor()
    
    def __enter__(self):
        return self
    
    def __exit__(self, exc_type, exc_val, exc_tb):
        self.close()
    
    @property
    def connection(self):
        return self._conn

    @property
    def cursor(self):
        return self._cursor
    
    def close(self):
        self.connection.close()
        print("closing!")