import pyautogui as ag
import cv2
import numpy as np
import chess.engine

from util import parse_fen
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
        _, tabuleiro = captura_imagem(pontos)

        cv2.imshow("capturado", tabuleiro)
        tecla = cv2.waitKey(0)

        if tecla == ord('q'):
            break
        else:
            cv2.destroyWindow("capturado")
            pontos = []

cv2.destroyAllWindows()

# loop classificação e tomada de decisão
_, imagem = captura_imagem(pontos)
engine = chess.engine.SimpleEngine.popen_uci("stockfish.exe")
while True:
    cv2.imshow("Tabuleiro", imagem)
    tecla = cv2.waitKey(100)

    if tecla == ord('q'):
        cinza, imagem = captura_imagem(pontos)
        celulas = separar_celulas(cinza, jogando_brancas)
        classificacao = classificar(modelo, celulas)
        fen = parse_fen(classificacao, jogando_brancas)
        tabuleiro = chess.Board(fen)
        movimento = engine.play(tabuleiro, chess.engine.Limit(time=1))

        cv2.putText(imagem, f"movimento: {movimento.move}", (0, 30), cv2.FONT_HERSHEY_SIMPLEX, 1, (0, 0, 255), 2)
        print(fen)
