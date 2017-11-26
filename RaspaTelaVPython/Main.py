import CriacaoURLs
import DownloadClass
import DownloadClassV2
import FileDialog
import os

# endereco = input("Endereço do Arquivo: ")
endereco = FileDialog.abrindo_arquivo()

arq = open(endereco, 'r', encoding='utf-8-sig')
texto = arq.readlines()
arq.close()

url = texto[0]
caminho_arquivo = texto[1]
inicio = int(texto[2])
fim = int(texto[3])

url = url.rstrip()
caminho_arquivo = caminho_arquivo.rstrip()

def cls():
    os.system('cls' if os.name == 'nt' else 'clear')

def verificar_conexao():
    loop = True
    primeira = True
    url_teste = "https://www.gstatic.com/images/branding/googlelogo/2x/googlelogo_color_284x96dp.png"
    while(loop):
        resultado_verificacao = DownloadClass.verificando_arquivo_online(url_teste)
        if(resultado_verificacao):
            break
        else:
            if(primeira):
                primeira = False
                print("Sem Conexao a Internet")

if not url or not caminho_arquivo or fim <= inicio:
    print("Url Vazio")
else:
    cls()
    total_de_arquivos = fim - inicio
    numero_de_arquivos_baixados = 0;
    numero_do_arquivo = inicio
    while(numero_do_arquivo < fim):
        numero_de_arquivos_baixados += 1
        verificar_conexao()
        arquivo_existe = CriacaoURLs.verificar_se_arquivo_existe(caminho_arquivo, numero_do_arquivo)
        cls()
        print("%d" % numero_do_arquivo)
        print("%d de %%d Arquivos Baixados" % numero_de_arquivos_baixados % total_de_arquivos)
        if(arquivo_existe):
            status_arquivo = " Arquivo Ja Existe"
            print("Arquivo %d Ja Existe" % numero_do_arquivo)
        else:
            if not (url[len(url) - 1] == "/"):
                url = url + "/"
            arquivo_online = CriacaoURLs.procurar_arquivo_online(url + str(numero_do_arquivo))
            if(arquivo_online[0]):
                arquivo_baixado = DownloadClass.download_arquivos(caminho_arquivo, arquivo_online[1])
                if(arquivo_baixado):
                    FileDialog.salvando_arquivo(caminho_arquivo + "V2ArquivosBaixados.txt", str(numero_do_arquivo) + "\n", url)
                    status_arquivo = " Arquivo Baixado"
                else:
                    status_arquivo = " Arquivo Nao Baixado"
            else:
                print("Arquivo %d NaoEncontrado" %numero_do_arquivo)
                status_arquivo = " Arquivo Nao Encontrado"
                FileDialog.salvando_arquivo(caminho_arquivo + "V2NaoEncontrado.txt", str(numero_do_arquivo) + "\n", url)
        FileDialog.salvando_arquivo(caminho_arquivo + "V2Relatorio.txt", str(numero_do_arquivo) + status_arquivo + "\n", url)
        numero_do_arquivo += 1

""""
url = input("Url Arquivo: ")
caminho = input("Caminho para Salvar: ")
resultado_verificaco_online = DownloadClass.verificando_arquivo_online(url)
if(resultado_verificaco_online[0]):
     DownloadClass.download_arquivos(caminho, resultado_verificaco_online[1])
else:
     print("Arquivo Offline ou Não Existe")
"""
