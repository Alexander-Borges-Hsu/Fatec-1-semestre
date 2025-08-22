valor_X = float(input(f"Insira um valor que será armazenado em X e posteriormente invertido com Y: "))
valor_Y = float(input(f"insira um valor para Y que será invertido com X: "))

valor_Z = valor_X

valor_X = valor_Y

valor_Y = valor_Z

print(f"Novo valor X: {valor_X}, novo valor Y: {valor_Y}.")
