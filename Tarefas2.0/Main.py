import FileManagement
import os

def cls():
    os.system('cls' if os.name == 'nt' else 'clear')

nome_do_arquivo = "Tarefas.txt"
resposta = ""

while resposta != '0':

    conteudo_do_arquivo = FileManagement.abrindo_arquivo(nome_do_arquivo)
    if(conteudo_do_arquivo == ""):
        FileManagement.criar_arquivo(nome_do_arquivo, "")
    contador = 1
    for item_lista in conteudo_do_arquivo:
        if "\n" in item_lista:
            if item_lista.replace("\n", "") == "":
                contador -= 1
            else:
                print(str(contador) + " - " + item_lista.replace("\n", ""))
        else:
            print(str(contador) + " - " + item_lista)
        contador += 1
    resposta = input("Comando: ")

    if(resposta == '0'):
        break

    try:
        numero_da_lista = int(resposta)
        contador = 1
        for item_lista in conteudo_do_arquivo:
            if(numero_da_lista == contador):
                tarefa_para_remover = item_lista
            contador += 1

        conteudo_do_arquivo.remove(tarefa_para_remover)
        FileManagement.salvar_sobre_arquivo_existente(nome_do_arquivo, conteudo_do_arquivo)
    except ValueError:
        confiramacao = input("Adicionar Tarefa: (s/n)")
        confiramacao.lower()
        if(confiramacao == 's'):
            FileManagement.salvando_arquivo(nome_do_arquivo, resposta)
    cls()
