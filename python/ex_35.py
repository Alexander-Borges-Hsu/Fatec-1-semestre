# Receba 2 números inteiros, verifique qual o maior entre eles. 
# Calcule e mostre o resultado da somatória dos números ímpares entre esses valores.

N1 = int(input("Insira um número: "))
N2 = int(input("Insira um segundo número: "))
soma = 0

if N1 > N2:
    N1 , N2 = N2, N1

i = N1
 
while i < N2:
    if i % 2 != 0:
        soma += i
    i += 1
print(f"A soma dos números ímpares entre {N1} e {N2} é {soma}.")