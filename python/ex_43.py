# Calcule e mostre quantos anos serão necessários para que Ana seja maior que
# Maria sabendo que Ana tem 1,10m e cresce 3cm ao ano e Maria tem 1,5m
# e cresce 2cm ao ano.

Ana = 1.1
Maria = 1.5

anos = 0

while Ana < Maria:
    Ana += 0.03
    Maria += 0.02

    anos += 1

print(f"Ana irá demorar {anos} anos para passar Maria, em {anos} anos, Ana terá {Ana:.2f} metros e Maria terá {Maria:.2f} metros.")