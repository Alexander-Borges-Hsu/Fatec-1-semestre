# Receba 100 números inteiros reais. Verifique e mostre o maior e o menor valor.
# Obs.: somente valores positivos.

numeros = []

menor = int(input("Insira o 1° valor positivo: "))
maior = 1

i = 0
while i < 99:
    numeros.append(int(input(f"Insira o {i + 2}° valor positivo: ")))
    if maior < numeros[i]:
        maior = numeros[i]
    if menor > numeros[i]:
        menor = numeros[i]
    i += 1
print(f"O maior número inserido foi: {maior}, o menor número inserido foi: {menor}.")