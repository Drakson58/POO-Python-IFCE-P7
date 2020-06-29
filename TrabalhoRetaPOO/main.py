from Classes.Pontos import Ponto
from Classes.Reta import Reta


while True:
	
	print('1 - Calcular distancia entre pontos.')
	print('2 - Fechar programa.')
	opcao = int(input('Opção: '))
	print()
	if opcao == 2:
		break

	# Valores do ponto X
	x1 = int(input('X1: '))
	x2 = int(input('X2: '))
	print()

	# Valores do ponto Y
	y1 = int(input('Y1: '))
	y2 = int(input('Y2: '))
	print()

	p1 = Ponto(x1, x2)
	p2 = Ponto(y1, y2)

	reta = Reta(p1.getX(), p2.getX(), p1.getY(), p2.getY())
	print('A distancia é =',reta.calculaDistancia())
	print()