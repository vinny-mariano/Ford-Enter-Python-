"""
2) Uso de OR

Crie um programa que receba a nota final de um aluno e sua frequência (em porcentagem). 
O aluno será considerado aprovado se tiver nota maior ou igual a 7 ou frequência maior ou igual a 75%. 
Caso contrário, deverá ser reprovado. O programa deve exibir uma mensagem informando a situação do aluno.
"""

nota = float(input("Informe sua nota final: \n"))
frequencia = float(input("Informe sua frequência(numericamente): \n"))

if(nota>=7 or frequencia >= 75):
    print("Você está aprovado")

else:
    print("Você está reprovado!")