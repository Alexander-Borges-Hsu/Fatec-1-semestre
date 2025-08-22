horas_trabalhadas = int(input("Digite a quantidade de horas trabalhadas: "))
valor_hora = float(input("Digite o valor por hora: "))
percentual_desconto = float(input("Digite o percentual do desconto (somente números): "))
quantidade_dependentes = int(input("Digite a quantidade de dependentes: "))

salario_bruto = horas_trabalhadas * valor_hora
salario_liquido = salario_bruto * (1 - percentual_desconto / 100)

print(salario_liquido)

salario_liquido += 100 * quantidade_dependentes

print(f"O salario bruto é de R${salario_bruto}, com o reajuste será de R${salario_liquido}.")