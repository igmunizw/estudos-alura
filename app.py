import os

restaurantes = [{'nome': 'Praça', 'categoria': 'Japonesa', 'ativo': False}, {'nome': 'Pizza Suprema', 'categoria': 'Pizza', 'ativo': True}, {'nome': 'Cantina', 'categoria': 'Mexicana', 'ativo': False}]

def exibir_nome_do_programa():
    print(""""

░██████╗░█████╗░██████╗░░█████╗░██████╗░  ██╗░░░░░░█████╗░  ███████╗██╗░░░░░███████╗
██╔════╝██╔══██╗██╔══██╗██╔══██╗██╔══██╗  ██║░░░░░██╔══██╗  ██╔════╝██║░░░░░██╔════╝
╚█████╗░███████║██████╦╝██║░░██║██████╔╝  ██║░░░░░███████║  █████╗░░██║░░░░░█████╗░░
░╚═══██╗██╔══██║██╔══██╗██║░░██║██╔══██╗  ██║░░░░░██╔══██║  ██╔══╝░░██║░░░░░██╔══╝░░
██████╔╝██║░░██║██████╦╝╚█████╔╝██║░░██║  ███████╗██║░░██║  ███████╗███████╗███████╗
╚═════╝░╚═╝░░╚═╝╚═════╝░░╚════╝░╚═╝░░╚═╝  ╚══════╝╚═╝░░╚═╝  ╚══════╝╚══════╝╚══════╝""")

def exibir_opcoes():
    print('1. Cadastrar restaurante')
    print('2. Listar restaurantes')
    print('3. Alternar estado do restaurante')
    print('4. Sair')

def finalizar_app():
    exibir_subtitulo('Finalizando o App')


def voltar_ao_menu_principal():
    input('Digite uma tecla para voltar ao menu principal...')
    main()

def opcao_invalida():
    print('Opção inválida. \n')

    voltar_ao_menu_principal()

def exibir_subtitulo(texto):
    os.system('clear')
    linha = '-' * (len(texto) + 4)
    print(linha)
    print(texto)
    print(linha)
    
def cadastrar_novo_restaurante():
    """ Essa função é responsável por cadastrar um novo restaurante
    
    Inputs:
    - Nome do restaurante
    - Categoria do restaurante
    
    Outputs:
    - Adiciona um novo restaurante à lista de restaurantes"""

    exibir_subtitulo('Cadastro de novos restaurantes')
    nome_do_restaurante = input('Digite o nome do restaurante que deseja cadastrar: ')
    categoria_do_restaurante = input('Digite a categoria do restaurante: ')
    print('Cadastro de novos restaurantes\n')
    dados_do_restaurante = {'nome': nome_do_restaurante, 'categoria': categoria_do_restaurante, 'ativo': False}
    restaurantes.append(dados_do_restaurante)
    print(f'O restaurante "{nome_do_restaurante}" foi cadastrado com sucesso!\n')

    voltar_ao_menu_principal()

def alternar_estado_do_restaurante():
    exibir_subtitulo('Alternando estado do restaurante')
    nome_restaurante = input('Digite o nome do restaurante que deseja ativar/desativar: ')
    restaurante_encontrado = False
    for restaurante in restaurantes:
        if nome_restaurante == restaurante['nome']:
            restaurante_encontrado = True
            restaurante['ativo'] = not restaurante['ativo']
            mensagem = f'O restaurante "{nome_restaurante}" foi ativado com sucesso' if restaurante['ativo'] else f'O restaurante "{nome_restaurante}" foi desativado com sucesso'
            print(mensagem)
    if not restaurante_encontrado:
        print(f'Não foi encontrado um restaurante com o nome "{nome_restaurante}"\n')

    voltar_ao_menu_principal()

def listar_restaurantes():
    exibir_subtitulo('Listando restaurantes')

    print(f'{"Nome do restaurante".ljust(20)} | {"Categoria".ljust(20)} | Estado')
    for restaurante in restaurantes:
        nome_restaurante = restaurante['nome']
        categoria_restaurante = restaurante['categoria']
        ativo = 'ativado'if restaurante['ativo'] else 'desativado'
        print(f'- {nome_restaurante.ljust(20)}: | {categoria_restaurante.ljust(20)} | {ativo}')
    print('\n')

    voltar_ao_menu_principal()

def escolher_opcao():
    try:
        opcao_escolhida = int(input('Escolha uma opção: '))

        if opcao_escolhida == 1:
            print('Cadastrar restaurante')
            cadastrar_novo_restaurante()
        elif opcao_escolhida == 2:
            listar_restaurantes()
        elif opcao_escolhida == 3:
            alternar_estado_do_restaurante()
        elif opcao_escolhida == 4:
            finalizar_app()
        else:
            opcao_invalida()
    except ValueError:
        opcao_invalida()


def main():
    os.system('clear')
    exibir_nome_do_programa()
    exibir_opcoes()
    escolher_opcao()

if __name__ == "__main__":
    main()