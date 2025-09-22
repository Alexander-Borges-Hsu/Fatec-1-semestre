# Receba um número. Calcule e mostre a série 1 + 1/2 + 1/3 + ... 1/N.

N = float(input("Insira um número: "))
Na = N
i = float()

while N > 0:
    i += 1/N
    N -= 1

print(f"A série do número {Na} é {i:.2f}")