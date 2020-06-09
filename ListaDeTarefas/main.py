# coding=<utf-8>

from Classes.usuario import *
from menu import Menu

while True:
    opcoes = Menu()
    opcao = opcoes.menuInicial()

    if (opcao == 1):
        
        print('\n*** FAÇA SEU CADASTRO ***')
        print('*************************')
        nome = str(input('Nome de usuario: '))
        senha = str(input('Senha: '))
        email = str(input('Email: '))
        usuario = Usuario(nome, senha, email)
        print(usuario.getNome())
        usuario.cadastrar()
    elif (opcao == 2):
        
        print('\n*** USUARIOS CADASTRADOS ***')
        print('****************************')
        usuario = Usuario()
        #print(usuario.usuariosCadastrados())
        for x in usuario.usuariosCadastrados():
            print(f'Nome: {x[1]}.\nEmail: {x[3]}.\n')
    elif (opcao == 3):

        print('\n*** FAÇA SEU LOGIN ***')
        print('************************')
        email = str(input('Email: '))
        senha = str(input('Senha: '))
        usuario = Usuario()

        for x in usuario.usuariosCadastrados():
            if(x[3] == email):
                if(x[2] == senha):
                    usuario.setId(x[0])
                    #print('Usuario autenticado.', usuario.getId())
                    opcao = opcoes.menuLogado()
                    
                    if (opcao == 9):         
                        esc = opcoes.menuDeletarConta()
                        if(esc == 'Y' or esc == 'y'):
                            usuario.apagarUsuario(email)
                            print('\033[34m'+'Usuario apagado.'+'\033[0;0m')
                        else:
                            print('\033[32m'+'Operação cancelada.'+'\033[0;0m')
                else:
                    print('\033[31m'+'Usuario invalido!!'+'\033[0;0m')    
                continue
    elif (opcao == 0):
        
        print('Uma pena você ter que ir. Espero sua volta em breve.')
        break    
    