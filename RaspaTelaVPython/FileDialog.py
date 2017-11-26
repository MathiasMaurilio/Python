import tkinter as tk

def abrindo_arquivo():
    from tkinter import filedialog
    root = tk.Tk()
    root.withdraw()
    return filedialog.askopenfilename()

def salvando_arquivo(caminho_para_salvar, conteudo, url):
    try:
        arquivo = open(caminho_para_salvar, 'r+')
        texto = arquivo.readlines()
        arquivo.writelines(conteudo)
    except FileNotFoundError:
        arquivo = open(caminho_para_salvar, 'w+')
        arquivo.writelines(url + "\n" + conteudo)
    arquivo.close()