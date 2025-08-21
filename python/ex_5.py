coeficiente_A = float(input("Insira o coeficiente A da fórmula: "))
coeficiente_B = float(input("Insira o coeficiente B da fórmula: "))
coeficiente_C = float(input("Insira o coeficiente C da fórmula: "))

delta = coeficiente_B ** 2 - 4 * coeficiente_C * coeficiente_A

raiz_1 = (- coeficiente_B + delta ** 0.5) / 2 * coeficiente_A
raiz_2 = (- coeficiente_B - delta ** 0.5) / 2 * coeficiente_A

print(f"A raíz 1 é {raiz_1} e a raíz 2 é {raiz_2}")


