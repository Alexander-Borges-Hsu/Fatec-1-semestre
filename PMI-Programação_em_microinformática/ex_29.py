# Receba o tipo de investimento (1 = poupança e 2 = renda fixa) e o valor do investimento.
# Calcule e mostre o valor corrigido em 30 dias, sabendo que a poupança = 3% e a renda fixa = 5%.
# Demais tipos serão desconsiderados.
# Eu quis deixar o código robusto então deixei a possibilidade do usuário escolher a quantidade de mês que deixará o dinheiro rendendo.

tipo_poupanca = int(input("Escolha seu tipo de investimento, 1 para poupança, 2 para renda fixa: "))
valor_investimento = float(input("Informe o valor total a ser investido: "))
mes_investimento = float(input("Insira o tempo em mês que deixará o dinheiro rendendo: "))

if tipo_poupanca == 1:
    previsao = valor_investimento * (1 + 0.03) ** mes_investimento
    print(f"Os seus R${valor_investimento} irão se transformar em R${previsao:.2f} em {mes_investimento} meses com a poupança.")
elif tipo_poupanca == 2:
    previsao = valor_investimento * (1 + 0.05) ** mes_investimento
    print(f"Os seus R${valor_investimento} irão se transformar em R${previsao:.2f} em {mes_investimento} meses com a renda fixa.")
else:
    print("Selecione um investimento válido.")