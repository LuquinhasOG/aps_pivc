import numpy as np

# from cnn import build_model

import cv2
import numpy as np

# configurações
# diz se o jogador está jogando com as brancas ou não
# importante para definir a posição das peças, pois o chess.com gira o tabuleiro de acordo com sua cor
jogando_brancas = True
nova_resolucao = (512, 512)  # prints serão redimensionadas para esta resolução
tam_casa = nova_resolucao[0] // 8  # comprimento de uma casa no tabuleiro


def captura_imagem():
    imagem = cv2.imread("imagem_teste.png")  # lê a imagem
    grayscale = cv2.cvtColor(imagem, cv2.COLOR_BGR2GRAY)  # converte para tons de cinza
    resized = cv2.resize(grayscale, nova_resolucao, interpolation=cv2.INTER_AREA)  # redimensiona
    _, binaria = cv2.threshold(resized, 120, 255, cv2.THRESH_BINARY)  # transforma em imagem binária
    binaria = cv2.bitwise_not(binaria)  # invertendo a cores

    # contorno branco = peça branca
    # contorno preenchido de branco = peça preta
    return binaria


# separa as peças e define sua posição
def separar_celulas(imagem):
    casas_separadas = list()
    for i in range(8):
        for j in range(8):
            if jogando_brancas:
                celula = imagem[(7 - i) * tam_casa:(8 - i) * tam_casa, j * tam_casa:(j + 1) * tam_casa]
            else:
                celula = imagem[i * tam_casa:(i + 1) * tam_casa, j * tam_casa:(j + 1) * tam_casa]

            casas_separadas.append(((i, j), celula))  # o primeiro elemento da tupla é a posição e o segundo a imagem

    return casas_separadas


for i in separar_celulas(captura_imagem()):
    cv2.imshow("a", i[1])
    cv2.waitKey(0)
    cv2.destroyAllWindows()


# if __name__ == "__main__":
    # classes = ['vazia', 'bispo_branco', 'cavalo_branco', 'dama_branca', 'peao_branco', 'rei_branco', 'torre_branca',
    #            'bispo_preto', 'cavalo_preto', 'dama_preta', 'peao_preto', 'rei_preto', 'torre_preta']
    #
    # modelo = build_model()
    # modelo.load_weights("deteccao.weights.h5")
    #
    # imagem = captura_imagem()
    # celulas = separar_celulas(imagem)
    #
    # for pos, img in celulas:
    #     b = img
    #     img = img.reshape((50, 50, 1))
    #     img = np.expand_dims(img, axis=0)
    #     print(f"pos: {pos}, ped: {classes[np.argmax(modelo.predict(img))]}")
    #     cv2.imshow("peça", b)
    #     cv2.waitKey(0)
    #     cv2.destroyAllWindows()
