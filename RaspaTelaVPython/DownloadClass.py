import urllib.request, urllib.parse, urllib.error

def download_arquivos(caminho_para_salvar, url):
    url_alternativo = url
    while True:
        try:
            url_alternativo = url_alternativo[url_alternativo.index("/") + 1:]
        except Exception:
            break
    if(caminho_para_salvar[len(caminho_para_salvar) - 1] == "\\"):
        caminho_para_salvar = caminho_para_salvar + url_alternativo
    else:
        caminho_para_salvar = caminho_para_salvar + '\\' + url_alternativo

    resposta = False

    try:
        arquivo = open(caminho_para_salvar)
        print("Arquivo Existe")
        resposta = False

    except Exception:
        f = urllib.request.urlopen(url)
        data = f.read()
        with open(caminho_para_salvar, "wb") as code:
            code.write(data)
        resposta = True
    return  resposta

def verificando_arquivo_online(url):
    resposta = False
    try:
        urllib.request.urlopen(url).getcode()
        resposta = True
    except Exception:
        resposta = False
    return resposta, url