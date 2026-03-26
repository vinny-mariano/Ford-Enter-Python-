"""
3.Desenvolva um programa que calcule a média de
alunos por turma. Para isso, siga os passos abaixo:
Solicite
ao usuário a quantidade de turmas;
Para
cada turma, peça que o usuário informe a quantidade de alunos;
Certifique-se
de que o número de alunos por turma não ultrapasse 40;
Ao
final, exiba a média de alunos por turma
"""
turmas = 0
alunos = 0
i = 0

turmas = int (input("Digite a quantidade de turmas\n"))
while(turmas < 0):
    turmas = int (input("\nQuantidade inválida!\n Digite a quantidade de turmas: \n"))

while(i < turmas):
    i=i+1
    alunos = int (input("quantos alunos tem na turma?: "))

media = alunos / turmas
print(f"A dédia de alunos é: {media}")