import Download

url = input("Digite a Url: ")
caminho = input("Digite o caminho para salvar: ")
resultado_da_veridicacao = Download.verificando_arquivo_online(url)
if(resultado_da_veridicacao[0]):
    Download.download_arquivos(caminho, resultado_da_veridicacao[1])
else:
    print("Arquivo OffLine ou Não Existe")


nomes = ['mathias', 'da', 'silva', 'maurilio']
if('testando' or 'mathias' == nomes):
    print("Acertou Miseravi")
else:
    print("ta serto")

string = "Ola para você"
print(string)
lista = string.split(" ") #Serve para separar uma string em varias partes
string = lista[0] + " " + lista[2]
print(string)
string = string.replace(" ", " para ") #substitui uma parte da string
print(string)


tel = {
    30132: "Pericles",
    30142: "Menelau",
    30154: "Atreu",
    31000: "Tieste"
}
print(tel)
ola = tel.popitem() #Retorna um item aleatorio valor do dicionario e o apaga
print(ola[1])

