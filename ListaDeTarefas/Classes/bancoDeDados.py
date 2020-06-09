import mysql.connector

class BancoDeDados:

    def __init__(self):
        self._host = "localhost"
        self._user = "root"
        self._password = ""
        self._database = "listadetarefas"
        self._mydb = ""
        self._conn = ""
    
    def getHost(self):
        return self._host
    def getUser(self):
        return self._user
    def getPassword(self):
        return self._password
    def getMydb(self):
        return 
    
    def setHost(self, host):
        self._host = host
    def setUser(self, user):
        self._user = user
    def setPassword(self, password):
        self._password = password
    

    def conectar(self):
        self._mydb = mysql.connector.connect(
        host= self._host,
        user= self._user,
        password= self._password,
        database= self._database
        )
        
        return self._mydb.cursor()


    def atualizarDB(self):
        return self._mydb.commit()

    def mostraConexao(self):
        print(self._mydb)


mydb = BancoDeDados()
# conn = mydb.conectar()

# sql = "insert into usuarios (nome, senha) VALUES (%s, %s)"
# val = ("John", "Highway 21")
# conn.execute(sql, val)
# mydb.atualizarDB()