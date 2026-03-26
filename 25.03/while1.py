"""

1.Crie
um programa que solicite ao usuário uma nota entre zero e dez. Se o valor
informado for inválido, exiba uma mensagem de erro e continue solicitando uma
nota válida até que o usuário a forneça.

"""

nota = int(input("Digite uma nota entre 0 e 10:"))

while(nota < 0 or nota > 10):
    print("Erro:\n " \
          "Informe uma nota válida:\n")
    nota = int(input("\nDigite uma nota entre 0 e 10: \n"))