# Mostre todas as possibilidades de 2 dados de forma que a soma tenha como resultado 7.
N1 = 1
N2 = 6

i = 1

while i <= 6:
    print(f"{i}° possibilidade: {N1} + {N2} = {N1 + N2}.")    
    N1 += 1
    N2 -= 1
    i += 1
    