from Trabalho_01.Classes import *
from pylab import show, plt


#Recebendo os dados da Classe 'Ponto_1'  (X, Y)
print(' --  VALORES DO PONTO 1 -- ')
x1 = ler_num('Digite o valor de X1: ')
y1 = ler_num('Digite o valor de Y1: ')

#Recebendo os dados da Classe 'Ponto_2'  (Y1, Y2)
print(' --  VALORES DO PONTO 2 -- ')
x2 = ler_num('Digite o valor de X2: ')
y2 = ler_num('Digite o valor de Y2: ')

#Colocando os valores em uma lista.
p1 = [x1, y1]
p2 = [x2, y2]

#Passando para a classe reta.
reta = Reta(p1, p2)
#reta.mostra_pontos()
reta.retornar_p1X()



'''
#Passando dados para as classes.
ponto1 = Ponto_1(x1, y1)
pontosX = ponto1.separando_pontos()

ponto2 = Pontos_2(x2, y2)
pontosP = ponto2.separando_pontos()
'''


#Codigo que forma o quadrante.
# Tamanho das linhas

        # Reta vertical
plt.plot([0, 0],[20, -20], linewidth=4, color='red' )
plt.plot([20, -20],[0, 0], linewidth=4, color='red' )
        # Reta horizontal

#Passando os valores dos pontos para o plano cartesiano.
plt.plot((reta.retornar_p1X(), reta.retornar_p2X()), (reta.retornar_p1Y(), reta.retornar_p2Y()), 'bo-')

#Tamanho do plano cartesiano.
plt.axis((-20, 20, -20, 20))

show()

