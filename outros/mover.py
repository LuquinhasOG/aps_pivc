import os
import shutil
import random

origem = '../imagens/teste'
destinos = ['../imagens/treino', '../imagens/validacao', '../imagens/teste']
percentuais = [0.7, 0.15, 0.15]

for classe in os.listdir(origem):
    caminho_classe = os.path.join(origem, classe)
    if not os.path.isdir(caminho_classe):
        continue

    imagens = os.listdir(caminho_classe)
    random.shuffle(imagens)

    total = len(imagens)
    qtd_treino = int(percentuais[0] * total)
    qtd_validacao = int(percentuais[1] * total)
    qtd_teste = total - qtd_treino - qtd_validacao

    divisao = {
        '../imagens/treino': imagens[:qtd_treino],
        '../imagens/validacao': imagens[qtd_treino:qtd_treino + qtd_validacao],
        '../imagens/teste': imagens[qtd_treino + qtd_validacao:]
    }

    for destino, lista in divisao.items():
        for img in lista:
            origem_path = os.path.join(caminho_classe, img)
            destino_path = os.path.join(destino, classe, img)
            shutil.move(origem_path, destino_path)  # Use move() se quiser remover da origem

print("Divisão concluída com sucesso!")
