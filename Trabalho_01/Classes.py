class X_e_Y:
# Está classe recebe dois pontos no plano cartesiano.

    def __init__(self, x, y):
        self._x = x
        self._y = y


    #Getters
    def getX(self):
        return self._x


    def getY(self):
        return self._y


    #Seterrs
    def setX(self, x):
        self._x = x


    def setY(self, y):
        self._y = y


class Reta(X_e_Y):


    def __init__(self, p1, p2):
        self._p1 = p1
        self._p2 = p2


    #Geterrs
    def getP1(self):
        return self._p1


    def getP2(self):
        return self._p2


    #Setters
    def setP1(self, p1):
        self._p1 = p1


    def setP2(self, p2):
        self._p2 = p2


    def mostra_pontos(self):
        print(self._p1, self._p2)


    #Retornando os valores separados de cada ponto. (Retorna para o plano cartesiano)
    def retornar_p1X(self):
        return self._p1[0]
    def retornar_p1Y(self):
        return self._p1[1]


    def retornar_p2X(self):
        return self._p2[0]
    def retornar_p2Y(self):
        return self._p2[1]


    #Retornando quadrantes de cada ponto
    def quadrante_P1(self):

        if self._p1[0] > -1 and self._p1[1] > -1:
            print('Quadrante: 1')
            print(f'Nas posições -> X: {self._p1[0]} Y: {self._p1[1]}')

        elif self._p1[0] < 0 and self._p1[1] > 0:
            print('Quadrante: 2')
            print(f'Nas posições -> X: {self._p1[0]} Y: {self._p1[1]}')

        elif self._p1[0] < 0 and self._p1[1] < 0:
            print('Quadrante: 3')
            print(f'Nas posições -> X: {self._p1[0]} Y: {self._p1[1]}')

        elif self._p1[0] > -1 and self._p1[1] < 0:
            print('Quadrante: 4')
            print(f'Nas posições -> X: {self._p1[0]} Y: {self._p1[1]}')


    def quadrante_P2(self):
        if self._p2[0] > -1 and self._p2[1] > -1:
            print('O ponto P2 se encontra no quadrante: 1')
            print(f'Nas posições -> X: {self._p2[0]} Y: {self._p2[1]}')

        elif self._p2[0] < 0 and self._p2[1] > 0:
            print('O ponto P2 se encontra no Quadrante: 2')
            print(f'Nas posições -> X: {self._p2[0]} Y: {self._p2[1]}')

        elif self._p2[0] < 0 and self._p2[1] < 0:
            print('O ponto P2 se encontra no Quadrante: 3')
            print(f'Nas posições -> X: {self._p2[0]} Y: {self._p2[1]}')

        elif self._p2[0] > -1 and self._p2[1] < 0:
            print('O ponto P2 se encontra no Quadrante: 4')
            print(f'Nas posições -> X: {self._p2[0]} Y: {self._p2[1]}')

#Função para testar se é um número.
def ler_num(msg):
    while True:
        try:
            num = float(input(msg))
            if num < 21 and num > -21:
                return num
        except ValueError:
            print('ERRO! Digite um número inteiro ou flotoante.')

#Função para ler os pontos
def ler_pontos(msg):
    while True:
        try:
            ponto = str(input(msg))
            if ponto == 'P1' or ponto == 'p1':
                return 'p1'
            elif ponto == 'P2' or ponto == 'p2':
                return 'p2'
        except:
            print('ERRO!')
            continue
