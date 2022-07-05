from lib.interface import *
from lib.analise import *

print(linha())
print('DETECTOR DE VEÍCULOS E PEDESTRES'.center(42))

while True:
    resposta = menu(['Analisar Exemplos', 'Analisar Imagem', 'Analisar Vídeo', 'Como Utilizar o Programa', 'Fechar programa'])
    if resposta == 1:
        analisarExemplos()
    elif resposta == 2:
        cabecalho('Analisar Imagem')
        leitura = str(input('Digite o nome do arquivo: '))
        analisarImagem(leitura)
    elif resposta == 3:
        cabecalho('Analisar Vídeo')
        leitura = str(input('Digite o nome do arquivo: '))
        analisarVideo(leitura)
    elif resposta == 4:
        cabecalho('Como utilizar o programa')
        comoUtilizar()
    elif resposta == 5:
        cabecalho('Fechando programa')
        break
    else:
        print('\033[31mERRO, DIGITE UMA OPÇÃO VÁLIDA\033[m')
# analisarImagem('packages\galeria\imagem1.jpg')
# analisarVideo('packages\galeria\gravacao2.mp4')