#Calculadora

#Funções:

#Soma
def soma(a,b):
    return a+b
#Soma

#Subtração
def subtracao(a,b):
    return a-b
#Subtração

#Divisão
def divisao(a,b):
    return a/b
#Divisão

#Multiplicação
def multiplicacao(a,b):
    return a*b
#Multiplicação

opcao = int(input("Digite uma opção para selecionar o tipo de operação matemática:\n"
                  "1. Soma\n"
                  "2. Subtração\n"
                  "3. Divisão\n"
                  "4. Multiplicação\n"))

if (opcao in [1,2,3,4]):
    n1 = int(input("Digite o primeiro valor:"))
    n2 = int(input("Digite o segundo valor:"))
    if(opcao==1):
        print(soma(n1,n2))
    elif(opcao == 2):
        print(subtracao(n1,n2))
    elif(opcao == 3):
        print(divisao(n1,n2))
    elif(opcao == 4):
        print(multiplicacao(n1,n2))
else:
    print("Entrada inválida!!!")

    