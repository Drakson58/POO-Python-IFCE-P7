from Classes.produto import *

class ItemNotaFiscal(Produto):

    def __init__(self):
        Produto.__init__(self)

    def getNumero(self):
        return self._numero
    def getQuantidade(self):
        return self._quantidade
    def getValor(self):
        return self._valor

    def setNumero(self, numero):
        self._numero = numero
    def setQuantidade(self, quantidade):
        self._quantidade = quantidade
    def setValor(self, valor):
        self._valor = valor


    def valorItemNF(self):
        return self._quantidade * self._valor         

    def toString(self):
        return f'Numero:{self._numero} \nQuantidade:{self._quantidade} \nValor:{self._valor}' 


    