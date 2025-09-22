# Receba dois números inteiros. Verifique e mostre se o maior número é múltiplo do menor.

valor_1 = int(input("Insira um valor: "))
valor_2 = int(input("Insira um segundo valor: "))

def multiplicidade():
    if valor_1 > valor_2:
        if valor_1 % valor_2 == 0:
            print(f"O número {valor_1} é múltiplo de {valor_2}.")
        else:
            print(f"O número {valor_1} não é múltiplo de {valor_2}.")
    elif valor_2 % valor_1 == 0:
        print(f"O número {valor_2} é múltiplo de {valor_1}.")
    else:
        print(f"O número {valor_2} não é múltiplo de {valor_1}")

multiplicidade()