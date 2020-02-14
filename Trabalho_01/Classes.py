class Ponto_1:


    def __init__(self, x, y):
        self._x = x
        self._y = y


    #Getters
    def getX(self):
        self._x


    def getY(self):
        self._x


    #Setters
    def set_x(self, x):
        self._x = x


    def set_y(self, y):
        self._y = y


    def mostra_ponto1(self):
        print('X: ', self._x, 'Y: ', self._y)


    def separando_pontos(self):
        x1 = self._x
        x2 = self._y
        pontos = [x1, x2]
        return pontos


class Pontos_p1_p2:


    def __init__(self, p1, p2):
        self._p1 = p1
        self._p2 = p2


    #Getters
    def getX(self):
        self._p1


    def getY(self):
        self._p2


    #Setters
    def set_x(self, p1):
        self._p1 = p1


    def set_y(self, p2):
        self._p2 = p2


    def mostra_ponto1(self):
        print('X: ', self._p1, 'Y: ', self._p2)


    def separando_pontos(self):
        p1 = self._p1
        p2 = self._p2
        pontos = [p1, p2]
        return pontos


