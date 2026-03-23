estCivil = input("Insira seu estado civil utilizando uma das letras a seguir:\n" \
                 "C - Casado\n" \
                 "S - Solteiro\n" \
                 "D - Divorciado\n" \
                 "V - Viúvo\n" \
                 "O - Outros\n")

if (estCivil == "C" or estCivil == "c"):
    print("Você é Casado(a)")
elif (estCivil == "S" or estCivil == "s"):
    print("Você é Solteiro(a)")
elif (estCivil == "D" or estCivil == "d"):
    print("Você é Divorciado(a)")
elif (estCivil == "V" or estCivil == "v"):
    print("Você é Viúvo(a)")
elif (estCivil == "O" or estCivil == "o"):
    print("Seu estado civil é outro")
else:
    print("Entrada inválida")


#ou podemos utilizar a função .upper() e .lower() 
# que transforma o que está no input em letras 
# maúsculas ou minúsculas
"""
exemplo: x input("Insira Uma letra") .upper()
"""
