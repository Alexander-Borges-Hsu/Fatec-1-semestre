# Receba os valores em x e y. Efetue a troca de seus valores e mostre seus conteúdos.
valor_X = float(input(f"Insira um valor que será armazenado em X e posteriormente invertido com Y: "))
valor_Y = float(input(f"insira um valor para Y que será invertido com X: "))

if valor_X >= valor_Y or valor_X <= valor_Y:
    valor_X, valor_Y = valor_Y, valor_X

print(f"Novo valor X: {valor_X}, novo valor Y: {valor_Y}.")
