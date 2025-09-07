# Calcule a quantidade de grão contidos em um tabuleiro de xadrez onde:
# Casa: 1   2   3   4 ...   64
# Qtde: 1   2   4   8 ...   N

quantidade = 1
i = 1

while i <= 64:
    print(f"Casa: {i}.\nQuantidade: {quantidade}.\n")
    quantidade *= 2
    i += 1