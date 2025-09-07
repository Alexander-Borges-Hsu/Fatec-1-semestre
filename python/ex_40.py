# Receba 2 números inteiros. Verifique e mostre todos os números primos entre eles.

def primo(N):
    if N < 2:
        return False
    for i in range(2, N):
        if N % i == 0:   
            return False
    return True

N1 = int(input("Insira um número: "))
N2 = int(input("Insira um segundo número: "))

if N1 > N2:
    N1, N2 = N2, N1

i = 1

for num in range(N1 + 1, N2):
    if primo(num):
        print(f"O {i}° número primo entre os valores é: {num}")
        i += 1