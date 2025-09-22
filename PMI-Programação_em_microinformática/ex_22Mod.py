# Receba dois valores inteiros e diferentes. Mostre seus valores em ordem crescente.

valor_1 = int(input("Digite um valor inteiro: "))
valor_2 = int(input("Digite um segundo valor inteiro: "))

def verifica():
    if valor_1 > valor_2:
        print(valor_2, valor_1, sep = " | ")
    else:
        print(valor_1, valor_2, sep = " | ")

verifica()