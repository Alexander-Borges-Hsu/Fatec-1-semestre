# Receba o número de voltas, a extensão do circuito (em metros) e o tempo de duração (minutos).
# Calcule e mostre a velocidade média em Km/h.

num_voltas = int(input("Insira o número de voltas: "))
extensao_circuito = int(input("Insira a extensão do circuito (em metros): "))
tempo_duracao = int(input("Insira o tempo de duração (em minutos): "))

velocidade_media = (((num_voltas * extensao_circuito) / tempo_duracao) / 1000) * 60

print(f"A velocidade média mínima para a conclusão do circuito em {tempo_duracao} minutos é de {velocidade_media:.2f}Km/h.")