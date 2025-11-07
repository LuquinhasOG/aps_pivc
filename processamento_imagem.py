import numpy as np
import pyautogui as ag
import cv2

# configurações
# diz se o jogador está jogando com as brancas ou não
# importante para definir a posição das peças, pois o chess.com gira o tabuleiro de acordo com sua cor
nova_resolucao = (512, 512)  # prints serão redimensionadas para esta resolução
tam_casa = nova_resolucao[0] // 8  # comprimento de uma casa no tabuleiro


def captura_imagem(pontos):
    imagem = ag.screenshot()
    imagem = cv2.cvtColor(np.array(imagem), cv2.COLOR_RGB2BGR)
    imagem = imagem[pontos[0][1]:pontos[1][1], pontos[0][0]:pontos[1][0]]
    grayscale = cv2.cvtColor(imagem, cv2.COLOR_BGR2GRAY)  # converte para tons de cinza
    resized = cv2.resize(grayscale, nova_resolucao, interpolation=cv2.INTER_AREA)  # redimensiona

    return [resized, imagem]


# separa as peças e define sua posição
def separar_celulas(imagem, jogando_brancas):
    casas_separadas = list()
    for i in range(8):
        for j in range(8):
            if jogando_brancas:
                celula = np.array(imagem[(7 - i) * tam_casa:(8 - i) * tam_casa, j * tam_casa:(j + 1) * tam_casa])
            else:
                celula = np.array(imagem[i * tam_casa:(i + 1) * tam_casa, (7 - j) * tam_casa:(8 - j) * tam_casa])

            casas_separadas.append(celula.reshape((64, 64, 1)))  # o primeiro elemento da tupla é a posição e o segundo a imagem

    return np.array(casas_separadas)


# if __name__ == "__main__":
#     classes = ['vazia', 'bispo_branco', 'cavalo_branco', 'dama_branca', 'peao_branco', 'rei_branco', 'torre_branca',
#                'bispo_preto', 'cavalo_preto', 'dama_preta', 'peao_preto', 'rei_preto', 'torre_preta']
#
#     modelo = build_model()
#     modelo.load_weights("deteccao.weights.h5")
#
#     imagem = captura_imagem()
#     celulas = separar_celulas(imagem)
#
#     for pos, img in celulas:
#         b = img
#         img = img.reshape((64, 64, 1))
#         img = np.expand_dims(img, axis=0)
#         print(f"pos: {pos}, ped: {classes[np.argmax(modelo.predict(img))]}")
