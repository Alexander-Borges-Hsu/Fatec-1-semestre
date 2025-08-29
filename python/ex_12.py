# Receba o ano de nascimento e o ano atual. Calcule e mostre a sua idade e quantos anos terá daqui a 17 anos
# Eu quis deixar o código robusto, então dei a possibilidade do usuário escolher o ano em que ele quer prever a sua idade
ano_nascimento = int(input("Insira o seu ano de nascimento: "))
ano_atual = int(input("Insira o ano atual: "))
ano_futuro = int(input("Insira o ano futuro que desejará calcular sua idade: "))

idade = ano_atual - ano_nascimento

idade_futura = idade + ano_futuro - ano_atual

print(f"Sua idade atual é {idade} anos, e sua idade em {ano_futuro} será {idade_futura} anos.")