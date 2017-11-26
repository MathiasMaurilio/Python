import os

def abrindo_arquivo(caminho_para_arquivo):
    try:
        arquivo = open(caminho_para_arquivo, 'r')
        texto = arquivo.readlines()
    except FileNotFoundError:
        return ""
    arquivo.close()
    for arquivo_limpo in texto:
        local = texto.index(arquivo_limpo)
        if "\n" in arquivo_limpo:
            texto[local] = arquivo_limpo.replace("\n", '')
    return texto

def salvando_arquivo(caminho_para_arquivo, conteudo):
    try:
        arquivo = open(caminho_para_arquivo, 'r+')
        texto = arquivo.readlines()
        arquivo.writelines(conteudo + "\n")
    except FileNotFoundError:
        arquivo = open(caminho_para_arquivo, 'w+')
        arquivo.writelines(conteudo)

    arquivo.close()

def salvar_sobre_arquivo_existente(caminho_para_arquivo, conteudo):
    arquivo = open(caminho_para_arquivo, 'w')
    arquivo.writelines(conteudo + "\n")
    arquivo.close()