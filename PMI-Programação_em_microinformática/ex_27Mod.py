# Receba o número de voltas, a extensão do circuito (em metros) e o tempo de duração (minutos).
# Calcule e mostre a velocidade média em Km/h.

num_voltas = int(input("Insira o número de voltas: "))
extensao_circuito = int(input("Insira a extensão do circuito (em metros): "))
tempo_duracao = int(input("Insira o tempo de duração (em minutos): "))

def calcvelocidade():
    velocidade_media = (((num_voltas * extensao_circuito) / tempo_duracao) / 1000) * 60
    return velocidade_media

velocidade_media = calcvelocidade()

print(f"A velocidade média é {velocidade_media:.2f}km/h")