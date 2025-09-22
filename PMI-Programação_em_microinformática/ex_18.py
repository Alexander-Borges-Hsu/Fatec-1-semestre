# Receba dois valores inteiros. Calcule e mostre a diferença do maior pelo menor
valor_1 = int(input("Insira o primeiro valor inteiro: "))
valor_2 = int(input("Insira o segundo valor inteiro: "))

if valor_1 == valor_2:
    print("Os valores são iguais, a diferença é 0.")
elif valor_1 > valor_2:
    diferenca = valor_1 - valor_2
    print(f"A diferença do maior para o menor é {diferenca}.")
else:
    diferenca = valor_2 - valor_1
    print(f"A diferença do maior para o menor é {diferenca}.")