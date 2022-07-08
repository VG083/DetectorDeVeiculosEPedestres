import cv2

from lib.interface import menu

def analisarImagem(leitura):
    '''
    """
    -> Essa função faz a análise de uma imagem para detectar carros
    :param leitura: Recebe o arquivo que deve ser lido
    '''
    # Importando a imagem de teste
    arquivoImagem = cv2.imread(leitura)
    # Importando o xml contendo o classificador de veiculos pré treinado
    arquivoClassificador = 'packages\cascatas\cVeiculos.xml'

    # Transformando a imagem em preto e branco na grayscale para utilizar o haar cascade
    pretoBranco = cv2.cvtColor(arquivoImagem, cv2.COLOR_BGR2GRAY)

    # Criando o classificador que vai reconhecer veiculos
    rastrearCarros = cv2.CascadeClassifier(arquivoClassificador)

    # Detectando carros com o detectMultiScale do cv2
    # É criado um lista que armazena outra lista contendo as coordenadas dos carros
    carros = rastrearCarros.detectMultiScale(pretoBranco)

    # Printa no terminal as coordenadas onde há carros dentro da imagem armazenada na lista de carros
    # [x, y, width, height]
    print(carros)

    # Desenhando um retangulo vermelho ao redor dos carros (2:57:00)
    # Para cada x,y,w,h em cada indice de carros
    for (x, y, w, h) in carros:
        cv2.rectangle(arquivoImagem, (x, y), (x+w, y+h), (0, 0, 225), 2)

    # Criando um display para exibir a imagem em uma janela
    cv2.imshow('Detector de Veiculos e Pedestres', arquivoImagem)

    # A função imshow durará só um frame
    # Então com essa função o programa só irá fechar apertando alguma tecla
    cv2.waitKey()

    print('Código executado com sucesso')


def analisarVideo(leitura):
    '''
    """
    -> Essa função faz a análise de um vídeo para detectar carros e pedestres
    :param leitura: Recebe o arquivo que deve ser lido
    '''
    # Importando o video que será analisado
    arquivoVideo = cv2.VideoCapture(leitura)
    # Importando os .xml contendo o classificador de veiculos e pedestres pré treinados
    arquivoClassificadorCarros = 'packages\cascatas\cVeiculos.xml'
    arquivoClassificadorPedestres = 'packages\cascatas\cPedestres.xml'

    # Criando o classificador que vai reconhecer veiculos e pedestres
    rastrearCarros = cv2.CascadeClassifier(arquivoClassificadorCarros)
    rastrearPedestres = cv2.CascadeClassifier(arquivoClassificadorPedestres)

    # Um loop para o programa rodar até os carros pararem
    while True:
        # Faz a leitura de quadros no arquivoVideo retornando uma tupla com um valor booleano e um frame do video
        (lidoComSucesso, frame) = arquivoVideo.read()

        # Roda o programa se o video tiver sido lido com sucesso
        if lidoComSucesso:
            # Converte o frame do video para preto e branco na escala preto e branco
            pretoBranco = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
        # Quebra o loop caso o vídeotena acabado
        else:
            break

        # Detectando carros e pedestres com o detectMultiScale do cv2
        # É criado um lista que armazena outra lista contendo as coordenadas dos carros/pedestres
        carros = rastrearCarros.detectMultiScale(pretoBranco)
        pedestres = rastrearPedestres.detectMultiScale(pretoBranco)

        # Printa no terminal as coordenadas onde há carros e pedestres dentro da imagem armazenada na lista de carros/pedestres
        # [x, y, width, height]
        
        # Desenhando um retangulo vermelho ao redor dos carros
        # Para cada x,y,w,h em cada indice de carros
        for (x, y, w, h) in carros:
            cv2.rectangle(frame, (x, y), (x+w, y+h), (0, 0, 225), 2)
        
        # Desenhando um retangulo amarelo ao redor dos pedestres
        # Para cada x,y,w,h em cada indice de pedestres
        for (x, y, w, h) in pedestres:
            cv2.rectangle(frame, (x, y), (x+w, y+h), (0, 225, 225), 2)

        # Criando um display para exibir o video em uma janela
        cv2.imshow('Detector de Veiculos e Pedestres', frame)

        # A função imshow durará só um frame
        # Então com essa função o programa só irá fechar apertando alguma tecla
        # Se a tecla apertada for 'q' o opencv irá fechar a janela
        key = cv2.waitKey(1)

        if key==81 or key==113:
            break
    
    cv2.destroyAllWindows()

    print('Código executado com sucesso')


def analisarExemplos():
    '''
    """
    -> Essa função faz um menu que auxilia o usuário a carregar o programa utilizando um dos arquivos presente no packages do programa
    '''
    resposta = menu(['Analisar a primeira imagem do banco de exemplos', 'Analisar a segunda imagem do banco de exemplos', 'Analisar a terceira imagem do banco de exemplos', 'Analisar o primeiro vídeo do banco de exemplos', 'Analisar o segundo vídeo do banco de exemplos'])
    if resposta == 1:
        analisarImagem('packages\galeria\imagem1.jpg')
    elif resposta == 2:
        analisarImagem('packages\galeria\imagem2.jpg')
    elif resposta == 3:
        analisarImagem('packages\galeria\imagem3.jpg')
    elif resposta == 4:
        analisarVideo('packages\galeria\gravacao1.mp4')
    elif resposta == 5:
        analisarVideo('packages\galeria\gravacao2.mp4')
    else:
        print('\033[31mERRO, DIGITE UMA OPÇÃO VÁLIDA\033[m')