classes = ['vazia', 'bispo_branco', 'cavalo_branco', 'dama_branca', 'peao_branco', 'rei_branco', 'torre_branca',
           'bispo_preto', 'cavalo_preto', 'dama_preta', 'peao_preto', 'rei_preto', 'torre_preta']

classes_fen = ['v', 'B', 'N', 'Q', 'P', 'K', 'R', 'b', 'n', 'q', 'p', 'k', 'r']

# monta o código fen do tabuleiro classificado pela CNN
def parse_fen(tabuleiro, branco):
    fen = ''
    aux = ''
    linhas = list()
    for i in range(8):
        vazios = 0
        for j in range(8):
            simbolo = classes_fen[tabuleiro[i*8 + j]]

            if simbolo != 'v':
                if vazios > 0:
                    aux += str(vazios)
                    vazios = 0

                aux += simbolo
            else:
                vazios += 1

        if vazios > 0:
            aux += str(vazios)

        linhas.append(aux)
        aux = ''

    linhas.reverse()
    for i in range(len(linhas)):
        fen += linhas[i]

        if i != len(linhas) - 1:
            fen += '/'

    fen += f' {'w' if branco else 'b'} KQkq'
    return fen
