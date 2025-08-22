tempo_percurso = float(input("Digite o tempo do percurso em horas: "))
velocidade_media = float(input("Digite a velocidade média do veículo em Km/h: "))
aproveitamento_combustivel = float(input("Digite o aproveitamento do combustivel em km/L: "))

combustivel_necessario = (tempo_percurso * velocidade_media) / aproveitamento_combustivel

print(f"Com o carro a uma velocidade média de {velocidade_media}Km/h e um tempo de {tempo_percurso}h, será necessário {combustivel_necessario} litros de combustivel.")