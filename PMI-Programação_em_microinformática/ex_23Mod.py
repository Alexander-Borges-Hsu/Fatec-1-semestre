# Receba três valores obrigatóriamente em ordem crescente e um 4° valor não 
# necessariamente em ordem. Mostre os quatro números em ordem crescente.

valor_1 = float(input("Insira um valor: "))
valor_2 = float(input("Insira um segundo valor maior que o valor anterior: "))
valor_3 = float(input("Insira um terceiro valor maior que o valor anterior: "))
valor_4 = float(input("Insira um quarto valor (não necessariamente em ordem crescente): "))

def ordenar():
    if valor_4 < valor_1:
        print(valor_4, valor_1, valor_2, valor_3, sep = " | ")
    elif valor_4 < valor_2:
        print(valor_1, valor_4, valor_2, valor_3, sep = " | ")
    elif valor_4 < valor_3:
        print(valor_1, valor_2, valor_4, valor_3, sep = " | ")
    else:
        print(valor_1, valor_2, valor_3, valor_4, sep = " | ")

ordenar()