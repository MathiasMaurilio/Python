import urllib.error
import webbrowser

url = 'http://www.statf.com/r101.9/redesign/areas/staticpages/img/linktous/logos/764x383.gif'
"""
print("Baixando o Arquivo")
urllib.request.urlretrieve(url, "E:\Downloads\ fandango.gif")
"""

webbrowser.open(url) #Abri um url no navegador padrão
input()

try:
    arquivo = open("E:\Downloads\ fandango.gif")
    print("Arquivo Existe")

except Exception:
    pass
    print("Arquivo Não Existe")
    print("Usando o urllib2")
    f = urllib.request.urlopen(url)
    data = f.read()
    with open("E:\Downloads\ fandango.gif", "wb") as code:
        code.write(data)

try:
    urllib.request.urlopen("http://pythonclub.com.br/images/test-ff-sel-clicar-no-link").getcode()
    print("Deu Certo")
except Exception:
    print("Arquivo Offline")

codigo =  ["mathias", "maurilio", "vitor", "pedro"]
print(codigo[1])
nome = input("Qual o seu Nome: ")
if(nome not in codigo):
    codigo.append(nome)
else:
    print("Esse nome já existe na lista")
print(codigo)
if(input("Apagar nome da Lista?: ") == 'sim'):
    numero_na_lista = int(input("Escolha o index: "))
    print(type(numero_na_lista))
    del(codigo[numero_na_lista])

#for idx, item in enumerate(codigo):
#    print(codigo)

segundo_numero = []
for numero_index in range(len(codigo)):
    print(codigo[numero_index])
    segundo_numero += [numero_index,]

#for numero_index in range(len(codigo)):
#    print(codigo[numero_index], " Loop 2")
#    codigo.pop(numero_index)
nome_apagar = input("Escolha o nome que ira apagar: ")
if(codigo.count(nome_apagar) >= 2):
    print("dois Nomes Iguais")
segundo_numero = segundo_numero[::-1]

print("Usando Enumerate")
for k,v in enumerate(codigo):
    print(v)

for numero_index in range(len(segundo_numero)):
    print("Numero Index: ", segundo_numero[numero_index])
    if(str(codigo[segundo_numero[numero_index]]) == nome_apagar):
        codigo.pop(segundo_numero[numero_index])

#codigo.shor() #Serve para ordenar a lista de forma Ascendente

#numero = len(codigo)
#while(numero > 0):
#    del (codigo[int(numero) - 1])
#    numero -= 1

print(codigo, " Restante")
print("numeros", segundo_numero)
