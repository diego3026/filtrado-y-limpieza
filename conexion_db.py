import psycopg2

class Conexion:
    
    def __init__(self, host = None, dbname = None, user = None, password = None,sslmode= None):
        self.host = host
        self.dbname = dbname
        self.user = user
        self.password = password
        self.sslmode = sslmode
    
    def conect(self):
        conect_string = "host={0} dbname={1} user={2} password={3} sslmode={4}".format(self.host, self.dbname, self.user, self.password, self.sslmode)
        self.conexion = psycopg2.connect(self.conector)
        self.cursor = self.conexion.cursor() 
        
    
    def execute(self,sql):
        self.cursor.execute(sql)
        
    def commit(self):
        self.conexion.commit()
    
    def close(self):
        self.cursor.close()
        self.conexion.close()
        
    
        
    