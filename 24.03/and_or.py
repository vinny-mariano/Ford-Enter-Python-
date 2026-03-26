"""
3) Uso de AND

Crie um programa que peça o nome de usuário e a senha. 
O sistema deve permitir o acesso apenas se o usuário for "admin" e a senha for "1234". 
Caso contrário, deve exibir uma mensagem de acesso negado.
"""

usuario = input("Digite o usuário:\n")
senha = input("Digite a senha:\n")

if(usuario == "admin" and senha == "1234"):
    print(f"Seja bem vindo {usuario}!")
else:
    print("usuário ou senha incorretos")


