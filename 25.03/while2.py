"""
qt_nota = 0
nota = 0
soma = 0
media = 0

qt_nota = int(input("Informe a quantidade de notas a serem consideradas para a média"))

while(qt_nota <= 0):
    qt_nota = int(input("Erro: Informe a quantidade de notas a serem consideradas para a média"))

for i in range(qt_nota):
    nota = float(input(f"Digite a {i+1}ª nota"))
    while(nota < 0 or nota > 10):
        nota = float(input(f"Errp: Digite a {i+1}ª nota"))
        soma = soma + nota
            

media = soma / qt_nota

print(f"A média á {media}")

"""

notas = 0
contagem = 0
nota = 0

while nota != -1:
    nota = float(input("Digite uma nota (Digite -1 para sair):"))
    contagem = contagem +1
    notas = notas + nota
media = notas/nota
print(f"A média final é {media}")