# Receba o salário de um funcionário e mostre o novo salário com reajuste de 15%
# Eu quis deixar o código mais robusto então fiz a possibilidade do usuário escolher o reajuste
porcentagem = float(input("Insira a porcentagem de alteração do salário (somente números): "))
salario = float(input(f"Insira o atual salário que sofrerá uma alteração de {porcentagem}%: "))
novo_salario = salario * (1 + porcentagem / 100)

print(f"O salário agora tem o valor de R${novo_salario:.2f}.")