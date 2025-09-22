# Receba quatro notas bimestrais de um aluno. Calcule e mostre a média aritmética.
# Mostre a mensagem de acordo com a média:
# Se a média for >= 6,0 exibir "APROVADO";
# Se a média for >= 3,0 E < 6,0 exibir "EXAME";
# Se a média for < 3,0 exibir "RETIDO";

nota_1 = float(input("Digite a primeira nota: "))
nota_2 = float(input("Digite a segunda nota: "))
nota_3 = float(input("Digite a terceira nota: "))
nota_4 = float(input("Digite a quarta nota: "))

def calcmedia():
    media = (nota_1 + nota_2 + nota_3 + nota_4) / 4
    print (f"A média do aluno é {media:.2f}")
    return media

media = calcmedia()

def situacao(media):
    if media > 5.9:
        print("Aluno aprovado!")
    elif media < 3:
        print("Aluno retido!")
    else:
        print("Aluno em exame!")

situacao(media)