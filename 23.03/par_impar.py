x = int(input("Digite um número inteiro\n"))

if(x%2 == 0):
    print("O número é par")
elif(x%2 == 1):
    print("O número é ímpar")
elif(x < 0):
    print("Entrada inválida")
else:
    print("erro")