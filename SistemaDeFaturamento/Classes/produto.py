
class Produto:
  
    def getCodigo(self):
        return self._codigo
    def getDescricao(self):
        return self._descricao
    def getValor(self):
        return self._valor

    
    def setCodigo(self, codigo):
        self._numero = codigo
    def setDescricao(self, descricao):
        self._quantidade = descricao
    def setValor(self, valor):
        self._valor = valor


    def toString(self):
        return f'Codigo do produto: {self._codigo} \nDescricao: {self._descricao} \nValor do produto: {self._valor}'

    