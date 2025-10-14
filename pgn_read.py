import chess.pgn as pgn


arquivo = open("jogos/raw/lichess_db_standard_rated_2013-01.pgn")
jogo = pgn.read_game(arquivo)

vitoria_brancas = list()
vitoria_pretas = list()
empates = list()

print("lendo")
while jogo:
    if jogo.headers["Termination"] == "Time forfeit":
        jogo = pgn.read_game(arquivo)
        continue

    if jogo.headers["Result"] == "1-0" and len(vitoria_brancas) < 1000:
        vitoria_brancas.append(str(jogo))
    elif jogo.headers["Result"] == "0-1" and len(vitoria_pretas) < 1000:
        vitoria_pretas.append(str(jogo))
    elif jogo.headers["Result"] == "1/2-1/2" and len(empates) < 1000:
        empates.append(str(jogo))

    if len(vitoria_brancas) >= 1000 and len(vitoria_pretas) >= 1000 and len(empates) >= 1000:
        break

    jogo = pgn.read_game(arquivo)

print("escrevendo")
numero = 0
for i in vitoria_brancas:
    with open(f"jogos/vitoria_brancas/branca_{numero}.pgn", 'w') as file:
        file.write(i)

    numero += 1

numero = 0
for i in vitoria_pretas:
    with open(f"jogos/vitoria_pretas/preta_{numero}.pgn", 'w') as file:
        file.write(i)

    numero += 1

numero = 0
for i in empates:
    with open(f"jogos/empates/empate_{numero}.pgn", 'w') as file:
        file.write(i)

    numero += 1

arquivo.close()
