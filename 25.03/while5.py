"""
5.Desenvolva
um programa em Python que peça ao usuário para criar uma senha e, em seguida,
solicite que ele a digite novamente. Continue pedindo até que as duas senhas
correspondam.
"""
senha = input("Crie uma senha: \n")
confirma_senha = input("Confirme sua senha:\n")

while(confirma_senha != senha):
    confirma_senha = input("Tente novamente!\nInsira sua senha:\n")

print("Senha confirmada!")