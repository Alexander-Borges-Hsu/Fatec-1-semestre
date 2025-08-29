# Receba quatro notas bimestrais de um aluno. Calcule e mostre a média aritmética.
# Mostre a mensagem de acordo com a média:
# Se a média for >= 6,0 exibir "APROVADO";
# Se a média for >= 3,0 E < 6,0 exibir "EXAME";
# Se a média for < 3,0 exibir "RETIDO";

nota_1 = float(input("Insira a primeira nota do aluno: "))
nota_2 = float(input("Insira a segunda nota do aluno: "))
nota_3 = float(input("Insira a terceira nota do aluno: "))
nota_4 = float(input("Insira a quarta nota do aluno: "))

media = (nota_1 + nota_2 + nota_3 + nota_4) / 4

print(f"A média aritmética do aluno é {media:.2f}")

if media >= 6.0:
    print("APROVADO")
elif media < 3.0:
    print("RETIDO")
else:
    print("EXAME")