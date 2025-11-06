import pyautogui as ag
import cv2
import numpy as np

from cnn import build_model, classificar, classes
from processamento_imagem import captura_imagem, separar_celulas

modelo = build_model()
modelo.load_weights("deteccao.weights.h5")

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
            pontos = []

cv2.destroyAllWindows()

# loop classificação e tomada de decisão
imagem = captura_imagem(pontos)
tabuleiro = np.zeros((8, 8))
while True:
    cv2.imshow("Tabuleiro", imagem)
    tecla = cv2.waitKey(100)

    if tecla == ord('q'):
        imagem = captura_imagem(pontos)
        celulas = separar_celulas(imagem)
        for pos, img in celulas:
            tabuleiro[pos] = classificar(modelo, img)

        print(tabuleiro)
