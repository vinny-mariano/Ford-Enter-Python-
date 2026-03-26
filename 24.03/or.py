"""
1) Uso de OR

Crie um programa em Python que peça a idade de uma pessoa e se ela possui autorização dos responsáveis 
(responda com "sim" ou "não"). 

O programa deve permitir a entrada no evento caso a pessoa tenha 18 anos ou mais ou tenha autorização. 
Caso contrário, deve informar que a entrada não é permitida.
"""

idade = int(input("Digite sua idade"))
autorizada = int(input("Você tem autorização dos seus reponsáveis?\n" \
                       "1. Sim\n" \
                       "0. Não\n"))

if(idade>=18):
    print("Sua entrada foi autorizada")
elif(idade<18 or autorizada == 1):
    print("Sua entrada está autorizada")
elif(idade<18 or autorizada == 0):
    print("Sua entrada não está autorizada")
else:
    print("Entrada inválida")
