deposito = float(input("Insira o valor do depósito: "))
tempo_mes = float(input("Insira o tempo em mês que deixará rendendo: "))
rendimento_mes = float(input("Insira o valor da porcentagem (somente números): "))
rendimento_mes = rendimento_mes / 100 
previsao = deposito * (1 + rendimento_mes) ** tempo_mes

print(f"Os seus R${deposito} irão virar R${previsao:.2f} em {tempo_mes} meses.")