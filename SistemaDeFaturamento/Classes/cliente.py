
class Cliente:

    def __init__(self, codigo, nome, cnpjcpf):
        self._codigo = codigo
        self._nome = nome
        self._cnpjcpf = cnpjcpf

    def getCodigo(self):
        return self._codigo
    def getNome(self):
        return self._nome
    def getCnpjcpf(self):
        return self._cnpjcpf

    def setCodigo(self, codigo):
        self._codigo = codigo
    def setNome(self, nome):
        self._nome = nome
    def setCnpjcpf(self, cnpjcpf):
        self._cnpjcpf = cnpjcpf

    
    def cliente(self):
        return self._codigo


    def toString(self):
        return f'ID:{self._codigo} \nNome:{self._nome} \nCNPJ ou CPF:{self._cnpjcpf}'


cliente = Cliente('01291', 'Drakson Bezerra Santos', '06101176371')
print(cliente.toString())