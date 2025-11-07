import pyautogui as ag
import cv2
import numpy as np

from util import classes, parse_fen
from cnn import build_model, classificar
from processamento_imagem import captura_imagem, separar_celulas

modelo = build_model()
modelo.load_weights("deteccao.weights.h5")

jogando_brancas = True if (input("você está jogando com as brancas?[s/n]: ")).lower() == 's' else False

# loop de calibrar tabuleiro
pontos = []
tabuleiro = []
while True:
    cv2.imshow("a", np.zeros((300,  300)))
    tecla = cv2.waitKey(100)

    if tecla == ord('q'):
        pontos.append(ag.position())

    if len(pontos) == 2:
        tabuleiro = captura_imagem(pontos)

        cv2.imshow("capturado", tabuleiro)
        tecla = cv2.waitKey(0)

        if tecla == ord('q'):
            break
        else:
            cv2.destroyWindow("capturado")
            pontos = []

cv2.destroyAllWindows()

# loop classificação e tomada de decisão
imagem = captura_imagem(pontos)
tabuleiro = list()
while True:
    cv2.imshow("Tabuleiro", imagem)
    tecla = cv2.waitKey(100)

    if tecla == ord('q'):
        imagem = captura_imagem(pontos)
        celulas = separar_celulas(imagem, jogando_brancas)
        tabuleiro = classificar(modelo, celulas)

        print(parse_fen(tabuleiro, jogando_brancas))
