# Receba um valor inteiro. Verifique e mostre se é divisível por 2 e 3.

valor_1 = int(input("Insira um valor inteiro: "))

def verifica():
    if valor_1 % 2 == 0 and valor_1 % 3 == 0:
        print("O valor inserido é divisível por 2 e 3.")
    elif valor_1 % 2 == 0:
        print("O valor inserido é divisível apenas por 2.")
    elif valor_1 % 3 == 0:
        print("O valor inserido é divisível apenas por 3.")
    else:
        print("O valor inserido não é divisível nem por 2 nem por 3.")

verifica()