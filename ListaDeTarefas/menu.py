# coding=<utf-8>


class Menu:


    def menuInicial(self):
        print('\n\n*** GERENCIADOR DE TAREFAS ***')
        print('******************************')
        print('Esolha uma das opções: ')
        print('1 - Me cadastrar.')
        print('2 - Usuarios cadastrados.')
        print('3 - Entrar.')
        print('0 - Sair.')
        opcao = int(input('Opção: '))
        return opcao


    def menuLogado(self):
        print('\n\n*** BEM VINDO ***')
        print('*****************')
        print('Esolha uma das opções: ')
        print('0 - Sair.')
        print('1 - Criar uma tarefa.')
        print('2 - Listar todas as terefas.')
        print('3 - Pesquisar por uma tarefa.')
        print('4 - Modificar uma tarefa.')
        print('5 - Apagar uma tarefa.')
        print('9 - Apagar conta.')
        opcao = int(input('Opção: '))
        return opcao


    def menuDeletarConta(self):
        print('Tem certeza que deseja apagar sua conta?')
        print('Y = Sim')
        print('N = Não')
        esc = str(input('Escolha: '))
        return esc