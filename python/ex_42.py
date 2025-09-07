# Calcule e mostre a série 1 + 2/3 + 3/5 + ... + 50/99.

dividendo = 1
divisor = 1
soma = 1

while dividendo < 50:
    dividendo += 1
    divisor += 2

    soma += dividendo / divisor

print(f"A soma da série é: {soma}.")