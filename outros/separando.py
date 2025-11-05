import cv2
import os

from shutil import move

classes = ['vazia', 'bispo_branco', 'cavalo_branco', 'dama_branca', 'peao_branco', 'rei_branco', 'torre_branca',
           'bispo_preto', 'cavalo_preto', 'dama_preta', 'peao_preto', 'rei_preto', 'torre_preta']
fonte = 'imagens/separado'
destino = 'imagens/treino'

imagens = os.listdir(fonte)
for i in range(len(imagens)):
    atual = cv2.imread(f'{fonte}/{imagens[i]}')
    cv2.imshow("a", atual)
    tecla = cv2.waitKey(0)

    caminho = 'vazia'
    if tecla == ord('1'):
        tecla = cv2.waitKey(0)

        if tecla == ord('r'):
            caminho = 'rei_preto'
        elif tecla == ord('c'):
            caminho = 'cavalo_preto'
        elif tecla == ord('b'):
            caminho = 'bispo_preto'
        elif tecla == ord('d'):
            caminho = 'dama_preta'
        elif tecla == ord('p'):
            caminho = 'peao_preto'
        elif tecla == ord('t'):
            caminho = 'torre_preta'

    elif tecla == ord('2'):
        tecla = cv2.waitKey(0)

        if tecla == ord('r'):
            caminho = 'rei_branco'
        elif tecla == ord('c'):
            caminho = 'cavalo_branco'
        elif tecla == ord('b'):
            caminho = 'bispo_branco'
        elif tecla == ord('d'):
            caminho = 'dama_branca'
        elif tecla == ord('p'):
            caminho = 'peao_branco'
        elif tecla == ord('t'):
            caminho = 'torre_branca'

    move(f'{fonte}/{imagens[i]}', f'{destino}/{caminho}')
    cv2.destroyAllWindows()
