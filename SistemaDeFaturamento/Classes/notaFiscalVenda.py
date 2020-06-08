from Classes.itemNotaFiscal import * 

class NotaFiscalVenda(ItemNotaFiscal):

    def __init__(self, codigo, data, valorNota):
        ItemNotaFiscal.__init__(self)
        self._codigo = codigo
        self._data = data
        self._valorNota = valorNota


    def getCodigo(self):
        return self._codigo
    def getData(self):
        return self._data
    def getValorNota(self):
        return self._valorNota

    
    def setCodigo(self, codigo):
        self._codigo = codigo
    def setData(self, data):
        self._data = data
    def setValorNota(self, valorNota):
        self._valorNota = valorNota


    def calcularValor(self):
        pass

    
    def criarItemNotaFiscal(self):
        pass


    def notaFiscalVenda(self):
        pass

    
    def toString(self):
        return f'Codigo:{self._codigo} \nData:{self._data} \nValor da nota:{self._valorNota}'


    def olaMundo(self):
        print('Ola, mundo!!!')
        




    