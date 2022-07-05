def receberOpcao(msg):
    while True:
        try: 
            n = int(input(msg))
        except (ValueError, TypeError):
            print('\033[31mERRO, DIGITE UM ARQUIVO/CAMINHO VÁLIDO\033[m')
            continue
        except (KeyboardInterrupt):
            print('\033[31mERRO, ENTRADA DE DADOS INTERROMPIDA PELO USUÁRIO\033[m')
            return 0
        else:
            return n


def linha(tam = 42):
    return '-'*tam


def cabecalho(msg):
    print(linha())
    print(msg.center(42))
    print(linha())


def menu(lista):
    cabecalho('MENU PRINCIPAL')
    contador = 1
    for item in lista:
        print(f'\033[33m{contador}\033[m - \033[34m{item}\033[m')
        contador += 1
    print(linha())
    opcao = receberOpcao('\033[33mSua opção: \033[m')
    return opcao


def comoUtilizar():
    print('Este programa é capaz de analisar um vídeo ou foto ou vídeo e reconhecer um carro ou um pedestre passando pela imagem. Os carros serão destacados por um quadrado vermelho e os pedestres por um quadrado amarelo.')
    print('\nPasso a passo:')
    print('1. Escolher no Menu Principal se deseja analisar uma imagem ou um vídeo')
    print('2. Escrever o nome do arquivo (com sua extensão) e apertar Enter')
    print('\nIMPORTANTE: O arquivo deve estar na mesma pasta que o arquivo principal.py')
    