# coding=<utf-8>
from Classes.usuario import *
from Classes.tarefa import *
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
                    usuario.setIdUsuario(x[0])        
                    #print('Usuario autenticado.', usuario.getIdUsuario())
                    
                    while True:
                        opcao = opcoes.menuLogado()
                        if (opcao == 9):         
                            esc = opcoes.menuDeletarConta()
                            if(esc == 'Y' or esc == 'y'):
                                usuario.apagarUsuario(email)
                                print('\033[34m'+'Usuario apagado.'+'\033[0;0m')
                            else:
                                print('\033[32m'+'Operação cancelada.'+'\033[0;0m')
                        
                        elif (opcao == 1):
                            print('\n*** SALVAR TAREFA ***')
                            print('***********************')
                            tarefa = Tarefa()
                            tarefa.setTarefa(str(input('Nome da tarefa:')))
                            tarefa.setDescricao(str(input('Descrição:')))
                            tarefa.setHorarioInicio(str(input('Horario de inicio: ')))
                            tarefa.setHorarioFim(str(input('Horario de termino: ')))
                            tarefa.setIdUsuario(usuario.getIdUsuario())
                            tarefa.salvarTarefa()
                            print('\033[34m'+'Tarefa salva com sucesso.'+'\033[0;0m')
                    
                        elif (opcao == 2):
                            print('\n*** TAREFAS CRIADAS ***')
                            print('*************************')
                            
                            tarefa = Tarefa()
                            for tarefa in tarefa.listarTarefas():
                                if(tarefa[1] == usuario.getIdUsuario()):
                                    #print(tarefa)
                                    print('Tarefa:', tarefa[2])
                                    print(f'Descrição: {tarefa[3]}.')
                                    print(f'Inicio: {tarefa[4]}.')
                                    print(f'Fim: {tarefa[5]}.\n')
                        
                        elif (opcao == 3):
                            print('\n*** PESQUISA DE TAREFA ***')
                            print('****************************')

                        elif (opcao == 4):
                            print('\n*** ATUALIZAR UMA TAREFA ***')
                            print('******************************')
                        
                        elif (opcao == 5):
                            print('\n*** APAGAR UMA TAREFA ***')
                            print('***************************')
                            taf = str(input('Nome da tarefa: '))
                            
                            tarefa = Tarefa()
                            for tar in tarefa.listarTarefas():
                                if(tar[2] == taf):
                                    print()
                                    print(f'Tarefa: {tar[2]}')
                                    print(f'Descrição: {tar[3]}')
                                    print(f'Inicio: {tar[4]}.')
                                    print(f'Fim: {tar[5]}.\n')
                                    
                                    esc = opcoes.menuDeletarTarefa()             
                                    if(esc == 'Y' or esc == 'y'):
                                        tarefa.setTarefa(taf)
                                        tarefa.apagarTarefa()
                                        print('\033[34m'+'Tarefa excluida.'+'\033[0;0m')
                                    else:
                                        print('\033[31m'+'Operação cancelada!!'+'\033[0;0m')
                        elif (opcao == 0):
                            print('Uma pena você ter que ir. Espero sua volta em breve.')
                            break
                else:
                    print('\033[31m'+'Usuario invalido!!'+'\033[0;0m')    
                continue
    elif (opcao == 0):
        
        print('Uma pena você ter que ir. Espero sua volta em breve.')
        break    
    