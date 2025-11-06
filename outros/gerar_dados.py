import cv2
import numpy as np
import os

from random import randint

c = 0
classes = os.listdir('../imagens/raw')
for i in classes:
    imagens = os.listdir(f'../imagens/raw/{i}')
    for j in imagens:
        imagem = cv2.imread(f'../imagens/raw/{i}/{j}')
        altura, largura = imagem.shape[:2]

        matriz_translacao = np.float32([[1, 0, randint(-5, 5)], [0, 1, randint(-5, 5)]])
        imagem_transladada = cv2.warpAffine(imagem, matriz_translacao, (largura, altura))

        centro = (largura // 2, altura // 2)
        matriz_rotacao = cv2.getRotationMatrix2D(centro, randint(-15, 15), 1.0)
        imagem_rotacionada = cv2.warpAffine(imagem_transladada, matriz_rotacao, (largura, altura))

        cv2.imwrite(f'../imagens/separar/{i}/img_{c}.png', imagem_rotacionada)
        c += 1
