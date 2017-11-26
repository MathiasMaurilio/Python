# -*- coding: cp1252 -*-
atr = input("Digite Sua Altura: ")
sex = raw_input("Informe Seu Sexo(M/F): ")

if sex == 'M' or sex == 'm':
    psi = (72.7*atr) - 58

elif sex == 'F' or sex == 'f':
    psi = (62.1*atr) - 44.7

else:
    print ("Sera nescessario que entre com alguma das opcoes")

psa = input("Digite Seu Peso Atual: ")

print ("Seu Peso Ideal é %s" % psi)

if psa < psi:
    print ("Voce Esta Apaixo do Seu Peso Ideal")

elif psa == psi:
    print ("Voce Esta no Seu Peso Ideal")

else:
    print ("Voce Esta Acima do Peso")
