# Receba um número inteiro. Calcule e mostre a série de Fibonacci até
# o seu N'nésimo termo.

N = int(input("Insira um número inteiro: "))
a1 = 0
a2 = 1
i = 1

while i <= N:
    print(f"{a1} + {a2} = {a1 + a2}.")
    a3 = a1
    a1 = a2
    a2 = a3 + a1
    i += 1
print(f"O {N}° da sequência de Fibonaci é: {a2}")