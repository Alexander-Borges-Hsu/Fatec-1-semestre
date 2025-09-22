# Receba a quantidade de horas trabalhadas, o valor por hora, o percentual de desconto e o número de dependentes. Calcule o salário
# que serão as horas trabalhadas x o valor por hora. Calcule o salário líquido (= Salário Bruto - desconto). A cada dependente será
# acrescido R$ 100 no salário líquido. Exiba o salário a receber.
def calcsal():
    quant_h = float(input("Digite a quantidade de horas trabalhadas: "))
    valor_h = float(input("Digite o valor a ser recebido por hora: "))
    percen_desc = float(input("Digite o percentual do desconto (somente números): "))
    num_depen = int(input("Digite a quantidade de dependentes: "))

    salario_bruto = quant_h * valor_h
    salario_liquido = salario_bruto * (1 - percen_desc / 100)
    salario_liquido += 100 * num_depen
    return salario_liquido

salario_liquido = calcsal()

print(f"O salário líquido do funcionário é de R${salario_liquido:.2f}.")