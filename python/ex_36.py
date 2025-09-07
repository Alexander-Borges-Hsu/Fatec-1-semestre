# Receba um número N. Calcule e mostre a série 1 + 1/1! + 1/2! + ... + 1/N!

N = float(input("Inisra um número: "))
soma = 1
i = 1
fatorial = 1

while i <= N:

    fatorial *= i
    soma += 1/fatorial
    i += 1

print(f"A série com fatorial é: {soma:.2f}")