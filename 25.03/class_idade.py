idade = int(input("Digite sua idade (numericamente): "))

if(idade <= 12):
    print("Você é criança")
elif(idade <= 17 and idade >= 13): 
    print("Você não é adolescente")
elif(idade <= 25 and idade >= 18): 
    print("Você é um jovem adulto")
elif(idade <= 35 and idade >= 26): 
    print("Você é um adulto")
elif(idade <= 60 and idade >= 36): 
    print("Você é um adulto sênior")
elif(idade >= 61): 
    print("Você é idoso")
else: 
    print("Entrada inválida!")