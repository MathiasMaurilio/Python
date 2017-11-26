import urllib.request, urllib.parse, urllib.error

def download_arquivos(caminho_para_salvar, url):
    urlAlternativo = url
    while True:
        try:
            urlAlternativo = urlAlternativo[urlAlternativo.index("/") + 1:]
        except Exception:
            break
    if(caminho_para_salvar[len(caminho_para_salvar) - 1] == "\ "):
        caminho_para_salvar = caminho_para_salvar + urlAlternativo
    else:
        caminho_para_salvar = caminho_para_salvar + "\ " + urlAlternativo
    resposta = False
    try:
        arquivo = open(caminho_para_salvar)
        print("Arquivo Já Existe")
        resposta = False

    except Exception:
        f = urllib.request.urlopen(url)
        data = f.read()
        with open(caminho_para_salvar, "wb") as code:
            code.write(data)
        resposta = True
    return resposta

def verificando_arquivo_online(url):
    resposta = False
    try:
        urllib.request.urlopen(url).getcode()
        resposta = True
    except Exception:
        resposta = False
    return resposta, url

"""
urlArquivo = "http://www.statf.com/r101.9/redesign/areas/staticpages/img/linktous/logos/764x383.gif"
caminho = "E:\Downloads\ "
caminho += "fandango.gif"

if(verificando_arquivo_online(urlArquivo)):
    if(download_arquivos(caminho, urlArquivo)):
        print("Arquivo baixado com sucesso")
else:
    print("Arquivo OffLine")

url = input("Digite a Url: ")
caminho = input("Digite o caminho para salvar: ")
if(verificando_arquivo_online(url)):
    download_arquivos(caminho, url)
else:
    print("Arquivo OffLine ou Não Existe")
"""