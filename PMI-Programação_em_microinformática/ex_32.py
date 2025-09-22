# Receba um número inteiro, calcule e mostre seu fatorial

N = int(input("Insira um número inteiro: "))
Na = N
i = N - 1

while i > 1:
    N *= i
    i -= 1

print(f"O fatorial de {Na} é {N}.")
