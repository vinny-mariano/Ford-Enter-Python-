print("Digite dois números, vou descobrir qual o menor deles\n")
x1 = float (input("Digite o primeiro numero:\n"))
x2 = float (input("Digite o segundo numero:\n"))

if (x1 > x2):
    print(f"{x2} é o menor número")
elif (x2 > x1):
    print(f"{x1} é o menor número")
elif (x1 == x2):
    print(f"{x1} e {x2} são números iguais")
else:
    print("erro")