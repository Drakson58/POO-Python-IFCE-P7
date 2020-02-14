from Trabalho_01.Classes import *
from pylab import show, plt



def ler_num(msg):

    while True:

        try:

            num = float(input(msg))
            return num
        except ValueError:

            print('ERRO! Digite um número inteiro ou flotoante.')
            continue


#Recebendo os dados da Classe 'Ponto_1'  (X, Y)
print(' --  VALORES DO PONTO 1 -- ')
x1 = ler_num('Digite o valor de X1: ')
y1 = ler_num('Digite o valor de Y1: ')

#Recebendo os dados da Classe 'Ponto_2'  (Y1, Y2)
print(' --  VALORES DO PONTO 2 -- ')
x2 = ler_num('Digite o valor de X2: ')
y2 = ler_num('Digite o valor de Y2: ')

#Passando dados para as classes.
ponto1 = Ponto_1(x1, y1)
pontosX = ponto1.separando_pontos()

ponto2 = Pontos_2(x2, y2)
pontosP = ponto2.separando_pontos()

#Linhas que forma os quadrantes
plt.hold('on')
# Set x-axis range
plt.xlim((0,10))
# Set y-axis range
plt.ylim((1,10))
# Draw lines to split quadrants
plt.plot([5,5],[1,9], linewidth=4, color='red' )
plt.plot([1,9],[5,5], linewidth=4, color='red' )


#Passando os valores dos pontos para o plano cartesiano.
plt.plot((y1, y2), (x1, x2), 'bo-')

#Tamanho do plano cartesiano.
plt.axis((0, 10, 1, 10))

show()

