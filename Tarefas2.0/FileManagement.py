import os

def abrindo_arquivo(caminho_para_arquivo):
    try:
        arquivo = open(caminho_para_arquivo, 'r')
        texto = arquivo.readlines()
    except FileNotFoundError:
        return ""
    arquivo.close()
    return texto

def salvando_arquivo(caminho_para_arquivo, conteudo):
    try:
        arquivo = open(caminho_para_arquivo, 'r+')
        texto = arquivo.readlines()
        arquivo.writelines(conteudo + "\n")
    except FileNotFoundError:
        arquivo = open(caminho_para_arquivo, 'w+')
        arquivo.writelines(conteudo + "\n")

    arquivo.close()

def salvar_sobre_arquivo_existente(caminho_para_arquivo, conteudo):
    arquivo = open(caminho_para_arquivo, 'w')
    arquivo.writelines(conteudo)
    arquivo.close()

def criar_arquivo(caminho_para_arquivo, conteudo):
    arquivo = open(caminho_para_arquivo, 'w+')
    arquivo.writelines(conteudo)
    arquivo.close()
