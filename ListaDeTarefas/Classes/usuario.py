from bancoDeDados import *

class Usuario(BancoDeDados):

    def __init__(self, nome, senha):
        BancoDeDados.__init__(self)
        #self._id = id_usuario
        self._nome = nome
        self._senha = senha

    
    #def getId(self):
       # return self._id
    def getNome(self):
        return self._nome
    def getSenha(self):
        return self._senha

    
    #def setId(self, id_usuario):
        #self._id = id_usuario
    def setNome(self, nome):
        self._nome = nome
    def setSenha(self, senha):
        self._senha = senha

    
    # CRUD
    def cadastrar(self):
        self._conn = self.conectar()
        # user.mostraConexao()
        query = "insert into usuarios (nome, senha) VALUES (%s, %s)"
        valores = (self._nome, self._senha)
        self._conn.execute(query, valores)
        self.atualizarDB()


    def usuariosCadastrados(self):
        self._conn = self.conectar()
        # user.mostraConexao()
        query = "SELECT id, nome, senha FROM usuarios WHERE 1"
        self._conn.execute(query)
        myresult = self._conn.fetchall()
        return myresult


    def apagarUsuario(self, nome_usuario):
        self._conn = self.conectar()
        # user.mostraConexao()
        query = f"DELETE FROM usuarios WHERE usuarios.nome = '{nome_usuario}'"
        self._conn.execute(query)
        self.atualizarDB()
    

    def atualizarUsuario(self):
        pass

#user = Usuario('Felipe', '1234')
#user.cadastrar()
#user.apagarUsuario('Felipe')
#print(user.usuariosCadastrados())

