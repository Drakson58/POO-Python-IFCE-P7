from Classes.bancoDeDados import *

class Usuario(BancoDeDados):

    def __init__(self, nome = '', senha = '', email = ''):
        BancoDeDados.__init__(self)
        self._id_usuario = ''
        self._nome = nome
        self._senha = senha
        self._email = email

    
    def getIdUsuario(self):
        return self._id_usuario
    def getNome(self):
        return self._nome
    def getSenha(self):
        return self._senha
    def getEmail(self):
        return self._email

    
    def setIdUsuario(self, id_usuario):
        self._id_usuario = id_usuario
    def setNome(self, nome):
        self._nome = nome
    def setSenha(self, senha):
        self._senha = senha
    def setEmail(self, email):
        self._email = email
    
    # CRUD
    def cadastrar(self):
        self._conn = self.conectar()
        # user.mostraConexao()
        query = "insert into usuarios (nome, senha, email) VALUES (%s, %s, %s)"
        valores = (self._nome, self._senha, self._email)
        self._conn.execute(query, valores)
        self.atualizarDB()


    def usuariosCadastrados(self):
        self._conn = self.conectar()
        # user.mostraConexao()
        query = "SELECT id, nome, senha, email FROM usuarios WHERE 1"
        self._conn.execute(query)
        myresult = self._conn.fetchall()
        return myresult


    def apagarUsuario(self, email_usuario):
        self._conn = self.conectar()
        # user.mostraConexao()
        query = f"DELETE FROM usuarios WHERE usuarios.email = '{email_usuario}'"
        self._conn.execute(query)
        self.atualizarDB()
    

    def atualizarUsuario(self):
        pass


    def mostrarUsuario(self):
        self._conn = self.conectar()
        # user.mostraConexao()
        query = f"SELECT id_tarefa, id_usuario, tarefa, descricao, horario_inicio, horario_fim FROM tarefas WHERE tarefas.id_usuario = {self._id_usuario}"
        self._conn.execute(query)
        myresult = self._conn.fetchall()
        return myresult

#user = Usuario('Felipe', '1234')
#user.cadastrar()
#user.apagarUsuario('Felipe')
#print(user.usuariosCadastrados())

