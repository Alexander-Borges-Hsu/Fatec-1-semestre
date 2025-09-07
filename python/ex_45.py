# Calcule e mostre a série 1 - 2/4 + 3/9 - 4/16 + 5/25 + ... + 15/225

dividendo = 1
divisor = 1

divisor_adiciona = 0
soma = 0

somar_subtrair= 1

while dividendo <= 15:  

    if somar_subtrair % 2 != 0:
        print(f"{soma:.2f} += {dividendo} / {divisor}")
        soma += dividendo / divisor
    else:
        print(f"{soma:.2f} -= {dividendo} / {divisor}")
        soma -= dividendo / divisor

    dividendo += 1
    divisor += 3 + divisor_adiciona
    divisor_adiciona += 2
    somar_subtrair += 1


print(f"O resultado dessa série é: {soma}")
