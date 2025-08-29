# Receba dois valores reais. Calcule e mostre o maior deles.
valor_1 = int(input("Insira um valor: "))
valor_2 = int(input("Insira um segundo valor: "))

if valor_1 == valor_2:
    print("Os valores são iguais.")
elif valor_1 > valor_2:
    print(f"O maior valor inserido é o {valor_1}.")
else: 
    print(f"O maior valor inserido é o {valor_2}.")