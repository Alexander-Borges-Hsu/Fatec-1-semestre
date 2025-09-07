# Receba a data de nascimento e atual em ano, mês e dia. 
# Calcule e mostre a idade em ano, meses e dias, considerando os anos bissextos.

def anoBissexto(ano):
    return (ano % 4 == 0 and ano % 100 != 0)
def diasNoMes(mes, ano):
    if mes == 2:
        return 29 if anoBissexto(ano) else 28
    elif mes in [4, 6, 9, 11]:
        return 30
    else: 
        return 31

ano_atual = int(input("Insira o ano atual: "))
mes_atual = int(input("Insira o mês atual: "))
dia_atual = int(input("Insira o dia atual: "))

ano_nascimento = int(input("Insira o ano de nascimento: "))
mes_nascimento = int(input("Insira o mês de nascimento: "))
dia_nascimento = int(input("Insira o dia de nascimento: "))

anos = ano_atual - ano_nascimento
meses = mes_atual - mes_nascimento
dias = dia_atual - dia_nascimento

if dias < 0:
    meses -= 1
    mes_anterior = mes_atual - 1
    ano_ref = ano_atual
    if mes_anterior == 0:
        mes_anterior = 12
        ano_ref -= 1
    dias += diasNoMes(mes_anterior, ano_ref)

if meses < 0:
    anos -= 1
    meses += 12

print(f"A sua idade é {anos} anos, {meses} meses e {dias} dias.")