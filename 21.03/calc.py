#calculadore geral, executa todas as operações

#nota1 = float(input("\nDigite o primeiro numero: \n"))
#nota2 = float(input("\nDigite o segundo numero: \n"))



"""
há duas formas de fazer os cáculos 
Utilizando a formatação para fazer referência à variavel
"""
"""
print("\n")
print(f"Soma: {nota1} + {nota2} = {(nota1+nota2)}")
print("\n")
print(f"Subtracao: {nota1} - {nota2} = {(nota1-nota2)}")
print("\n")
print(f"Divisão: {nota1} / {nota2} = {(nota1/nota2)}")
print("\n")
print(f"Multiplicação: {nota1} * {nota2} = {(nota1*nota2)}")
print("\n")
print(f"Exponenciação: {nota1} ** {nota2} = {(nota1**nota2)}")
print("\n")
print(f"Resto: {nota1} % {nota2} = {(nota1%nota2)}")
print("\n")

"""
"""
ou fazendo calculos dentro da função print, desde que o seu tipo
tenha sido especificado antes, neste exemplo essa especificação
se da pelo float antes da função input
"""
"""
print("\n")
print(nota1+nota2)
print("\n")
print(nota1-nota2)
print("\n")
print(nota1/nota2)
print("\n")
print(nota1*nota2)
print("\n")
print(nota1**nota2)
print("\n")
print(nota1%nota2)

"""
"""
if (nota1 + nota2 >= 6):
    print("Aprovado")
elif (nota1 + nota2 >3):
     print("Em recuperação")
else:
    print("Reprovado")
"""

"""
< menor
> maior
= igual
== comparacao
! Não(inverte o valor)
!= diferente(verifica diferença)
<= menor e igual
>= maior e igual
"""


opcao = int(input("=== Digite o numero da opcao desejada ===\n" \
                  "1. Adição\n" \
                  "2. Subtração\n" \
                  "3. DivisãoN" \
                  "4. Multiplicação\n" \
                  "5. Restante da divisão\n" \
                  "6. Expoente"))

if (opcao == 1):
    nota1 = float(input("\nDigite o primeiro numero: \n"))
    nota2 = float(input("\nDigite o segundo numero: \n"))
    print(f"Soma: {nota1} + {nota2} = {(nota1+nota2)}")

elif(opcao == 2):
    nota1 = float(input("\nDigite o primeiro numero: \n"))
    nota2 = float(input("\nDigite o segundo numero: \n"))
    print(f"Subtração: {nota1} - {nota2} = {(nota1-nota2)}")

elif(opcao == 3):
    nota1 = float(input("\nDigite o primeiro numero: \n"))
    nota2 = float(input("\nDigite o segundo numero: \n"))
    print(f"Divisão: {nota1} / {nota2} = {(nota1/nota2)}")

elif(opcao == 4):
    nota1 = float(input("\nDigite o primeiro numero: \n"))
    nota2 = float(input("\nDigite o segundo numero: \n"))
    print(f"Multiplicação: {nota1} * {nota2} = {(nota1*nota2)}")

elif(opcao == 5):
    nota1 = float(input("\nDigite o primeiro numero: \n"))
    nota2 = float(input("\nDigite o segundo numero: \n"))
    print(f"Restante da divisão: {nota1} % {nota2} = {(nota1%nota2)}")

elif(opcao == 6):
    nota1 = float(input("\nDigite o primeiro numero: \n"))
    nota2 = float(input("\nDigite o segundo numero: \n"))
    print(f"Expoente: {nota1} ** {nota2} = {(nota1**nota2)}")

else:
    print("Opção inválida!!!")

