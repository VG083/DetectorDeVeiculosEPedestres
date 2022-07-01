import cv2

# Importando o video de teste
arquivoVideo = cv2.VideoCapture('pedestres360p60seg.mp4')
# Importando os .xml contendo o classificador de veiculos e pedestres pré treinados
arquivoClassificadorCarros = 'baseVeiculos.xml'
arquivoClassificadorPedestres = 'basePedestres.xml'

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
    
    # Desenhando um retangulo vermelho ao redor dos carros (2:57:00)
    # Para cada x,y,w,h em cada indice de carros
    for (x, y, w, h) in carros:
        cv2.rectangle(frame, (x, y), (x+w, y+h), (0, 0, 225), 2)
    
    # Desenhando um retangulo amarelo ao redor dos pedestres (2:57:00)
    # Para cada x,y,w,h em cada indice de pedestres
    for (x, y, w, h) in pedestres:
        cv2.rectangle(frame, (x, y), (x+w, y+h), (0, 225, 225), 2)

    # Criando um display para exibir o video em uma janela
    cv2.imshow('Detector de Veiculos e Pedestres', frame)

    # A função imshow durará só um frame
    # Então com essa função o programa só irá fechar apertando alguma tecla
    cv2.waitKey(1)

print('Código executado com sucesso')