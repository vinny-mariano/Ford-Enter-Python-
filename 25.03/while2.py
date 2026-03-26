qt_nota = 0
nota_n = 0
soma = 0
media = 0

qt_nota = int(input("Informe a quantidade de notas a serem consideradas para a média"))

while(qt_nota <= 0):
    qt_nota = int(input("Informe a quantidade de notas a serem consideradas para a média"))


while(nota < 0 or > 10):
    for i in range(qt_nota):
        nota_n = float(input(f"Digite a {i+1}ª nota"))
        soma = nota_n + nota_n
        media = soma / qt_nota

print(f"A média á {media}")