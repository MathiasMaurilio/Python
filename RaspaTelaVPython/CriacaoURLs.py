import os.path
import DownloadClass

def verificar_se_arquivo_existe(caminho_arquivo, numero_arquivo):
    tipo_de_Imagem = ".jpg", ".gif", ".png", ".bmp", ".jpeg", ".webm"
    my_str_do_numero = str(numero_arquivo)
    resultado = False

    if not (caminho_arquivo[len(caminho_arquivo) - 1] == "\\"):
        caminho_arquivo = caminho_arquivo + "\\"

    for tipo in tipo_de_Imagem:
        str_caminho = caminho_arquivo + my_str_do_numero + tipo
        if os.path.exists(str_caminho):
            return True
        if(tipo == ".webm"):
            if os.path.exists(caminho_arquivo + "webm\\" + my_str_do_numero + tipo):
                return True
    return resultado

def procurar_arquivo_online(url):
    tipo_de_Imagem = ".jpg", ".gif", ".png", ".bmp", ".jpeg", ".webm"
    for tipo in tipo_de_Imagem:
        arquivo_online = DownloadClass.verificando_arquivo_online(url + tipo)
        if(arquivo_online[0]):
            return True, url + tipo
    return False, ""