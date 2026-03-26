dia = int (input("Informe o dia do seu nascimento:\n"))

mes = int (input("Digite o mês do seu nascimento (numericamente):\n" \
              "1. Janeiro\n" \
              "2. Fevereiro\n" \
              "3. Março\n" \
              "4. Abril\n" \
              "5. Maio\n" \
              "6. Junho\n" \
              "7. Julho\n" \
              "8. Agosto\n" \
              "9. Setembro\n" \
              "10. Outubro\n" \
              "11. Novembro\n" \
              "12. Dezembro\n"))
              
if(dia >= 21 or dia <= 20 and mes == 3 or mes == 4):
        print("Seu signo é ÁRIES")
elif(dia >= 21 or dia <= 20 and mes == 5 or mes == 4):
        print("Seu signo é TOURO")
elif(dia >= 21 or dia <= 20 and mes == 5 or mes == 6):
        print("Seu signo é GEMEOS")
elif(dia >= 21 or dia <= 22 and mes == 6 or mes == 7):
        print("Seu signo é CÂNCER")
elif(dia >= 23 or dia <= 22 and mes == 7 or mes == 8):
        print("Seu signo é LEÃO")
elif(dia >= 23 or dia <= 22 and mes == 8 or mes == 9):
        print("Seu signo é VIRGEM")
elif(dia >= 23 or dia <= 22 and mes == 9 or mes == 10):
        print("Seu signo é LIBRA")
elif(dia >= 23 or dia <= 21 and mes == 10 or mes == 11):
        print("Seu signo é ESCORPIÃO")
elif(dia >= 22 or dia <= 21 and mes == 11 or mes == 12):
        print("Seu signo é SARGITÁRIO")
elif(dia >= 22 or dia <= 20 and mes == 12 or mes == 1):
        print("Seu signo é CAPRICÓRNIO")
elif(dia >= 21 or dia <= 19 and mes == 1 or mes == 2):
        print("Seu signo é AQUÁRIO")
elif(dia >= 19 or dia <= 20 and mes == 2 or mes == 3):
        print("Seu signo é PEIXES")
else:
    print("Entrada inválida!")