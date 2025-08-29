# Receba os valores de 2 catetos de um triângulo retângulo. Calcule e mostre a hipotenusa
cateto_1 = float(input("Digite o valor do primeiro cateto: "))
cateto_2 = float(input("Digite o valor do segundo cateto: "))

hipotenusa = (cateto_1 ** 2 + cateto_2 ** 2) ** 0.5

print(f"O valor da hipotenusa é {hipotenusa}.")