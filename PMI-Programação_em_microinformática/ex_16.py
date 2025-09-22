# Receba a quantidade de horas trabalhadas, o valor por hora, o percentual de desconto e o número de dependentes. Calcule o salário
# que serão as horas trabalhadas x o valor por hora. Calcule o salário líquido (= Salário Bruto - desconto). A cada dependente será
# acrescido R$ 100 no salário líquido. Exiba o salário a receber.
horas_trabalhadas = int(input("Digite a quantidade de horas trabalhadas: "))
valor_hora = float(input("Digite o valor por hora: "))
percentual_desconto = float(input("Digite o percentual do desconto (somente números): "))
quantidade_dependentes = int(input("Digite a quantidade de dependentes: "))

salario_bruto = horas_trabalhadas * valor_hora
salario_liquido = salario_bruto * (1 - percentual_desconto / 100)

print(salario_liquido)

salario_liquido += 100 * quantidade_dependentes

print(f"O salario bruto é de R${salario_bruto:.2f}, com o reajuste será de R${salario_liquido:.2f}.")