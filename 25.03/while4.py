"""
4.Elabore
um algoritmo que receba um número, conte quantos dígitos ele possui e exiba o
resultado. Por exemplo, se o número for 201, a saída deve ser 3.
"""

n = int(input("Informe um numero inteiro e seus dígitos serão contados:\n"))
i=0

while(n < 0):
    n = int(input("Informe um numero inteiro e seus dígitos serão contados:\n"))
while(n != 0):
    decompor = int(n/10)
    i+=1
    n = decompor 

print(f"O número que você digitou tem {i} dígitos")