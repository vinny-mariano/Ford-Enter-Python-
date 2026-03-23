nota1 = float(input("Digite a primeira nota: "))
nota2 = float(input("Digite a segunda nota: "))
nota3 = float(input("Digite a terceira nota: "))

media = (nota1+nota2+nota3)/3

print(f"A media é: {media}")

if (media >= 7):
    print("O aluno está: Aprovado")

elif (media >= 5):
    print("O aluno está: Em recuperação")

else:
    print("O aluno está: Reprovado")