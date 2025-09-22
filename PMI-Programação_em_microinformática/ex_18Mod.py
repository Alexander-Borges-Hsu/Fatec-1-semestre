# Receba dois valores inteiros. Calcule e mostre a diferença do maior pelo menor

def calcdiferenca():
    valor_1 = int(input("Insira um valor: "))
    valor_2 = int(input("Insira um segundo valor: "))

    if valor_1 > valor_2:
        diferenca = valor_1 - valor_2
        print(f"A diferença do {valor_1} para o {valor_2} é {diferenca}.")
    else:
        diferenca = valor_2 - valor_1
        print(f"A diferença do {valor_2} para o {valor_1} é {diferenca}.")

calcdiferenca()