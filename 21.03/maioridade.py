#Toda variável em python deve ser minúscula

#input é equivalente ao scanf, coleta informação do usuário

nome = input("Digite seu nome: ")

"""
 Os inputs sempre são coletados como string, 
 para solicitar uma informação em um tipo especifico
 deve-se colocar antes da função o tipo da variável
"""

#Ao passar parâmetros pela função ela os exibe
#print(nome + " " + idade)

idade = int(input("Digite sua idade: "))



if (idade >= 18):
    print("Você é maior de idade")

else:
    print("Você não é maior de idade")
