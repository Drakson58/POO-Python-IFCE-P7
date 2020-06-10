from Classes.bancoDeDados import *

class Tarefa(BancoDeDados):

    def __init__(self, id_tarefa = '', id_usuario = '', tarefa = '', descricao = '', horario_inicio = '', horario_fim = ''):
        BancoDeDados.__init__(self)
        self._id_tarefa = id_tarefa
        self._id_usuario = id_usuario
        self._tarefa = tarefa
        self._descricao = descricao
        self._horario_inicio = horario_inicio
        self._horario_fim = horario_fim

    
    def getIdTarefa(self):
        return self._id_tarefa
    def getIdUsuario(self):
        return self._id_usuario
    def getTarefa(self):
        return self._tarefa
    def getDescricao(self):
        return self._descricao
    def getHorarioInicio(self):
        return self._horario_inicio
    def getHorarioFim(self):
        return self._horario_fim

    def setIdTarefa(self, id_tarefa):
        self._id_tarefa = id_tarefa 
    def setIdUsuario(self, id_usuario):
        self._id_usuario = id_usuario
    def setTarefa(self, tarefa):
        self._tarefa = tarefa
    def setDescricao(self, descricao):
        self._descricao = descricao
    def setHorarioInicio(self, horario_inicio):
        self._horario_inicio = horario_inicio
    def setHorarioFim(self, horario_fim):
        self._horario_fim = horario_fim

    # CRUD
    def salvarTarefa(self):
        self._conn = self.conectar()
        # user.mostraConexao()
        query = "insert into tarefas (id_usuario, tarefa, descricao, horario_inicio, horario_fim) VALUES (%s, %s, %s, %s, %s)"
        valores = (self._id_usuario, self._tarefa, self._descricao, self._horario_inicio, self._horario_fim)
        self._conn.execute(query, valores)
        self.atualizarDB()
    

    def listarTarefas(self):
        self._conn = self.conectar()
        # user.mostraConexao()
        query = "SELECT id_tarefa, id_usuario, tarefa, descricao, horario_inicio, horario_fim FROM tarefas WHERE 1"
        self._conn.execute(query)
        myresult = self._conn.fetchall()
        return myresult 

    
    def apagarTarefa(self):
        self._conn = self.conectar()
        # user.mostraConexao()
        query = f"DELETE FROM tarefas WHERE tarefas.tarefa = '{self._tarefa}'"
        self._conn.execute(query)
        self.atualizarDB()

    
    def atualizarTarefa(self):
        print('Atualizar tarefa.')