
class Produto:

    def __init__(self, codigo, descricao, valor):
        self._codigo = codigo
        self._descricao = descricao
        self._valor = valor

    
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


produto = Produto('01212', 'Celular caro', 1250.50)
print(produto.toString())