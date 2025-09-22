# Calcule a quantidade de litros gastos em uma viagem, sabendo que o automóvel faz 12km/l. Receber o tempo de percurso e a velocidade média
# Para deixar o código mais robusto, dei a possibilidade do usuário informar a quantidade de aproveitamento de combustível do veículo

def calclitros():
    tempo = float(input("Digite o tempo do percurso em horas: "))
    velocidade_media = float(input("Digite a velocidade média do veículo em km/h: "))
    litros = tempo * velocidade_media / 12
    return {"litros":litros, "tempo":tempo, "velocidade_media": velocidade_media}

dados = calclitros()

print(f"A quantidade de combustível necessário é de {dados["litros"]:.2f} litros \npara um viagem de {dados["tempo"]} horas à {dados["velocidade_media"]}km/h.")
