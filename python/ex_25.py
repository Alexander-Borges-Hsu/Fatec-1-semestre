# Receba a hora de início e de final de um jogo (HH,MM). Calcular o tempo do jogo em 
# horas e minutos, sabendo que o tempo máximo é menor que 24 horas e pode começar num dia 
# e terminar no outro.

hora_ini = int(input("Insira o horário de início do jogo: "))
minuto_ini = int(input("Insira o minuto de início do jogo: "))

hora_fim = int(input("Insira o horário de término do jogo: "))
minuto_fim = int(input("Insira o minuto de término do jogo: "))

if hora_ini > hora_fim:
    hora_total = 24 - hora_ini + hora_fim
else:
    hora_total = hora_fim - hora_ini

if minuto_ini > minuto_fim:
    minuto_total = 60 - minuto_ini + minuto_fim
else:
    minuto_total = minuto_fim - minuto_ini

print(f"O jogo terá a duração de: {hora_total}h{minuto_total}m.")