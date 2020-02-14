from Trabalho_01.Classes import *
from pylab import show, plt



def ler_num(msg):

    while True:

        try:

            num = int(input(msg)) or float(input(msg))
            return num
        except ValueError:

            print('ERRO! Digite um número inteiro ou flotoante.')
            continue

print('Valores do ponto X.')
x2 = ler_num('Digite X1: ')
x1 = ler_num('Digite X2: ')


print('Valores do ponto P')
#y1 = ler_num('Digite Y1: ')
#y2 = ler_num('DIgite y2:')



ponto1 = Ponto_1(x1, x2)
pontos = ponto1.separando_pontos()

ponto2 = Pontos_p1_p2(2, 4)
pontosP = ponto2.separando_pontos()




                 #y1 y2                   #p1 p2
plt.plot((pontos[0], pontos[1]), (pontosP[0], pontosP[1]), 'bo-')


#Tamanho do plano cartesiano
plt.axis((0, 10, 1, 10))

show()

