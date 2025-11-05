import cv2
import os

from random import choice

pasta = 'test'
destino = 'imagens/separado'
imagens = [i for i in os.listdir(pasta)]

dim = (512, 512)
tam = int(dim[0]/8)
c = int(input("número: "))

img = cv2.imread(f'{pasta}/{choice(imagens)}')
resized = cv2.resize(img, dim)
cinza = cv2.cvtColor(resized, cv2.COLOR_BGR2GRAY)

# cv2.imshow("a", resized)
# cv2.waitKey(0)

for i in range(8):
    for j in range(8):
        borda = cv2.rectangle(cinza.copy(), (j*tam, i*tam), ((j+1)*tam, (i+1)*tam), (0, 0,  255), 2)
        celula = cinza[i*tam:(i+1)*tam, j*tam:(j+1)*tam]

        cv2.imshow("a", borda)
        tecla = cv2.waitKey(0)

        if tecla == ord('s'):
            cv2.imwrite(f'{destino}/img{c}.png', celula)
            c += 1
