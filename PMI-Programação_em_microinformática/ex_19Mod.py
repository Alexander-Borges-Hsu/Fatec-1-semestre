# Receba dois valores reais. Calcule e mostre o maior deles.
valor_1 = float(input("Digite um valor: "))
valor_2 = float(input("Digite um segundo valor: "))

def maiorvalor():
    if valor_1 > valor_2:
        print(f"O maior valor inserido é o {valor_1}.")
    else:
        print(f"O maior valor inserido é o {valor_2}.")

maiorvalor()