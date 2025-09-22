# Receba o valor de um depósito em poupança. Calcule e mostre o valor após 1 mês de aplicação sabendo que rende 1,3% a. m
# Eu quis deixar o código robusto então deixei a possibilidade do usuário escolher a quantidade de mês e o rendimento
deposito = float(input("Insira o valor do depósito: "))
tempo_mes = float(input("Insira o tempo em mês que deixará rendendo: "))
rendimento_mes = float(input("Insira o valor da porcentagem do rendimento (somente números): "))
rendimento_mes = rendimento_mes / 100 
previsao = deposito * (1 + rendimento_mes) ** tempo_mes

print(f"Os seus R${deposito} irão virar R${previsao:.2f} em {tempo_mes} meses.")