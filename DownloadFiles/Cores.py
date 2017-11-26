cores = ['Verde', 'Branco']
def func_entrada_de_cores():
    while True:
        cor = input(" Digite o nome de uma cor \n 0 para Sair \n Ou 'listar' para ver todas as cores: ")
        cor = str.upper(cor[0:1]) + str.lower(cor[1:])
        if(cor == '0'):
            break
        elif cor == 'Listar':
            for index_color in range(len(cores)):
                print(index_color+1,": " + cores[index_color])
        elif cor in cores:
            print("Essa cor já foi adicionada")
        else:
            print("Essa cor não esta contida!")
            while True:
                escolha = str.lower(input("Deseja adicioná-la [s\ n]"))
                if(escolha == 's'):
                    cores.append(cor)
                    print("Cor adicionada com sucesso")
                    break
                elif(escolha == 'n'):
                    break
                else:
                    print("Por favor entre com uma opção valida")
        print()

func_entrada_de_cores()