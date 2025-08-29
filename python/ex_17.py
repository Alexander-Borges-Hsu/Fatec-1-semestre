# Calcule a quantidade de litros gastos em uma viagem, sabendo que o automóvel faz 12km/l. Receber o tempo de percurso e a velocidade média
# Para deixar o código mais robusto, dei a possibilidade do usuário informar a quantidade de aproveitamento de combustível do veículo
tempo_percurso = float(input("Digite o tempo do percurso em horas: "))
velocidade_media = float(input("Digite a velocidade média do veículo em Km/h: "))
aproveitamento_combustivel = float(input("Digite o aproveitamento do combustivel em km/L: "))

combustivel_necessario = (tempo_percurso * velocidade_media) / aproveitamento_combustivel

print(f"Com o carro a uma velocidade média de {velocidade_media:.2f}Km/h e um tempo de {tempo_percurso}h, será necessário {combustivel_necessario:.2f} litros de combustivel.")