# Receba um número. Calcule e mostre os resultados da tabuada desse número.

N = float(input("Insira um número: "))
i = 0

while i < 10:
    i += 1
    print(f"{N} x {i} = {N * i:.2f}")

