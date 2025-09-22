# Receba dois valores inteiros e diferentes. Mostre seus valores em ordem crescente.

valor_1 = int(input("Insira um valor: "))
valor_2 = int(input("Insira um segundo valor: "))

if valor_1 == valor_2:
    print("Os valores são iguais.")
elif valor_1 > valor_2:
    print(valor_2, "|", valor_1)
else:
    print(valor_1, "|", valor_2)