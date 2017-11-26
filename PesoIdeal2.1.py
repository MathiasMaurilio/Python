altura = int(input("Digite Sua Altura: "))
sexo = input("Informe seu Sexo(M/F): ")

if sexo == 'M' or sexo == 'm':
	peso_ideal = (72.7 * (altura * 2)) - 58
elif sexo == 'F' or sexo == 'F':
	peso_ideal = (62.1 * (altura* 2)) - 44.7
else:
	print("Sera nescessario que entre com alguma das opcoes")

peso_pessoa = int(input("Digite seu Peso Atual: "))
print("Seu Peso Ideal é %s" %peso_ideal)

if peso_pessoa < peso_ideal:
	print("Você esta abaixo do peso ideal")
elif peso_pessoa == peso_ideal:
	print("Você esta no seu peso ideal")
else:
	print("Você esta acima do Peso")