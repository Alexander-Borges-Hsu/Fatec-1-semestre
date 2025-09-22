# Receba o preço atual e a média mensal de um produto. Calcule e mostre o novo preço
# sabendo que:
# Venda Mensal       Preço atual        Preço Novo
# < 500              <30                +10%
# >= 500 e < 1000    >= 30 e < 80       +15%
# >= 1000            >= 80              -5%

# Observação: Para outras condições, preço novo será igual preço atual.

preco_atual = float(input("Insira o preço atual do produto: "))
venda_mensal = float(input("Insira a quantidade de venda mensal do produto: "))

def novopreco():
    if venda_mensal < 500 and preco_atual < 30:
        novo_preco = preco_atual * 1.1
    elif venda_mensal >= 500 and venda_mensal < 1000 and preco_atual >= 30 and preco_atual < 80:
        novo_preco = preco_atual * 1.15
    elif venda_mensal >= 1000 and preco_atual >= 80:
        novo_preco = preco_atual * 0.95
    else:
        novo_preco = preco_atual
    return novo_preco

novo_preco = novopreco()

print(f"O novo preço do produto é R${novo_preco:.2f}")