# Receba três valores obrigatóriamente em ordem crescente e um 4° valor não 
# necessariamente em ordem. Mostre os quatro números em ordem crescente.

valor_1 = float(input("Insira um valor: "))
valor_2 = float(input("Insira um segundo valor: "))
valor_3 = float(input("Insira um terceiro valor: "))
valor_4 = float(input("Insira um quarto valor (não necessariamente em ordem crescente): "))

if valor_4 < valor_1:
    print(f"{valor_4} | {valor_1} | {valor_2} | {valor_3}")
elif valor_4 < valor_2:
    print(f"{valor_1} | {valor_4} | {valor_2} | {valor_3}")
elif valor_4 < valor_3:
    print(f"{valor_1} | {valor_2} | {valor_4} | {valor_3}")
else:
    print(f"{valor_1} | {valor_2} | {valor_3} | {valor_4}") 