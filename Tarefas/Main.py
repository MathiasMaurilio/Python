import FileManagement
import os

def cls():
    os.system('cls' if os.name == 'nt' else 'clear')

nome_do_arquivo = "Tarefas.txt"
resposta = input("Abrir Lista?(s/n): ")

if resposta == 'S' or resposta == 's':
    while resposta != '0':
        conteudo_do_arquivo = FileManagement.abrindo_arquivo(nome_do_arquivo)
        if conteudo_do_arquivo == "":
            print("Arquivo de Tarefas Não Existe")
            resposta = input("Criar Novo Arquivo:")
            if resposta == 'S' or resposta == 's':
                FileManagement.salvando_arquivo(nome_do_arquivo, "")
                print("Arquivo Criado com Sucesso")
        else:
            contador = 1
            for lista in conteudo_do_arquivo:
                print(str(contador) + " - " + lista)
                contador += 1
        resposta = input("Comando: ")

        try:
            numero_para_remover = int(resposta)
            contador = 1
            for lista in conteudo_do_arquivo:
                if(numero_para_remover == contador):
                    tarefa_remover = lista
                contador += 1

            conteudo_do_arquivo.remove(tarefa_remover)
            FileManagement.salvar_sobre_arquivo_existente(nome_do_arquivo, conteudo_do_arquivo)
            cls()
        except ValueError:
            resposta.lower()
            if resposta == "novo":
                while resposta != "voltar":
                    print("Digite voltar para ver a lista")
                    resposta = input("Digite Uma Nova Tarefa: ")
                    if not resposta:
                        cls()
                        print("Erro: Nenhuma nova tarefa escrita")
                    elif resposta == "voltar":
                        cls()
                        break
                    else:
                        cls()
                        FileManagement.salvando_arquivo(nome_do_arquivo, resposta)
                        print("Tarefa Adicionada a Lista")
            elif resposta == "sair":
                break

elif resposta == 'N' or resposta == 'n':
    print("OK")