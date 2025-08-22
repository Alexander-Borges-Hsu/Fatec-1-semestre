alimento_quilo = float(input("Insira a quantidade de alimento em Kg: "))
gramas_diarias = float(input("Insira a quantidade em gramas que será consumida por dia: "))

dias_consumo = alimento_quilo * 1000 / gramas_diarias

print(f"Sabendo que será consumido {gramas_diarias} gramas por dia, {alimento_quilo} quilos irão durar {dias_consumo} dias.")