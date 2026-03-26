"""
>
<
>=
<=
==
!=
!

A condição inserida no print é verificada e um 
valor booleano (true ou false) é exibido.

ex: 

print(10<5) 
False

"""

"""
print(10<5) #False
print(10>=10) #True
print("a" == "b") #False
print("a" == "a") #True
"""

"""
login = "vinny_mariano@hotmail.com"
senha = "123456"
entrada_login = input("Digite o usuário:\n")
entrada_senha =  input("Digite a senha:\n")

if (login == entrada_login and entrada_senha == senha):
    print(f"Bem vindo {login}, acesso liberado!")
else:
    print("Acesso recusado")

"""

# or

"""
print(10<5 or 10>5)
print(10<5 and 10>5)
"""

camiseta = 580.50
calca = 690.90
saldo = 500
credito = 1000.00

opcao_compra = int (input(" 1. Camiseta\n 2. Calça\n"))
forma_de_pagamento = int (input(" 1. Débito\n 2. Crédito\n"))

if(opcao_compra == 1):
    if(saldo >= camiseta or credito >= camiseta):
        print("Parabéns pela compra!!!")
elif(opcao_compra == 2):
    if(saldo >= calca or credito>=calca):
        print("Parabéns pela compra")
