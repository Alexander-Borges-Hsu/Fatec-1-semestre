# Receba 2 ângulos de um triângulo. Calcule e mostre o valor do 3° ângulo
angulo_1 = float(input("Digite o valor de algum ângulo do triângulo: "))
angulo_2 = float(input("Digite o valor do segundo ângulo do triângulo: "))

angulo_3 = 180 - angulo_1 - angulo_2

print(f"O valor do terceiro ângulo é de {angulo_3}°.")