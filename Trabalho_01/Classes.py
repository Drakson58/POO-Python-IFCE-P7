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



#Função para testar se é um número.
def ler_num(msg):

    while True:

        try:

            num = float(input(msg))
            if num < 21 and num > -21:
                return num
        except ValueError:

            print('ERRO! Digite um número inteiro ou flotoante.')
