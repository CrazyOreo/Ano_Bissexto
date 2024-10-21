# Faça um Programa que peça um número correspondente a um determinado ano e em seguida informe se este ano é ou não bissexto.
ano_bisexto = float(input("Qual ano deseja saber?"))


if ano_bisexto % 4 == 0:
    resto = ano_bisexto % 100

    if ano_bisexto % 100 != 0 or ano_bisexto % 400 == 0:
        print("Seu ano e bissexto")
    
    else:
        print("Seu ano não é bissexto")

else:
    print("Seu ano não é bissexto")

# Ass: Crazy Oreo/Pedro Macegosa