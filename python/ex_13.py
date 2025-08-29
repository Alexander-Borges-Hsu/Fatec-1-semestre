# Receba a quantidade de alimento em quilos. Calcule e mostre quantos dias durará esse alimento sabendo que a pessoa consome 50g ao dia.
# Para deixar o código robusto eu dei a possibilidade do usuário escolher quantos gramas ele consumirá por dia
alimento_quilo = float(input("Insira a quantidade de alimento em Kg: "))
gramas_diarias = float(input("Insira a quantidade em gramas que será consumida por dia: "))

dias_consumo = alimento_quilo * 1000 / gramas_diarias

print(f"Sabendo que será consumido {gramas_diarias} gramas por dia, {alimento_quilo:.2f} quilos irão durar {dias_consumo} dias.")