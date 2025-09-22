# Receba três coeficientes A, B, C de uma equação do 2° grau. Verifique e mostre a existência de
# raízes reais e se caso exista, calcule e mostre.
coeficiente_A = float(input("Digite o coeficiente A da fórmula: "))
coeficiente_B = float(input("Digite o coeficiente B da fórmula: "))
coeficiente_C = float(input("Digite o coeficiente C da fórmula: "))

def bhaskara():
    delta = (coeficiente_B) ** 2 - 4 * coeficiente_A * coeficiente_C

    if delta < 0:
        print("Não existe raizes reais.")
    else:
        raiz_1 = (-(coeficiente_B) + delta ** 0.5) / (2 * coeficiente_A)
        raiz_2 = (-(coeficiente_B) - delta ** 0.5) / (2 * coeficiente_A)
        print(f"Raíz 1: {raiz_1}, raíz 2: {raiz_2}.")

bhaskara()