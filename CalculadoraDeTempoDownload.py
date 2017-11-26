velocidade = int(input("Velocidade do Download: "))
tipoTamanho = input("Tipo do Tamanho (GB, MB, KB)")
if tipoTamanho == 'GB' or tipoTamanho == 'gb' or tipoTamanho == 'gB' or tipoTamanho == 'Gb':
    tamanho = float(input("Tamanho do Arquivo em: "))
    tamanho = (tamanho * 1024) * 1024
    tamanho = int(tamanho)
elif tipoTamanho == 'MB' or tipoTamanho == 'mb' or tipoTamanho == 'mB' or tipoTamanho == 'Mb':
    tamanho = float(input("Tamanho do Arquivo em: "))
    tamanho = tamanho * 1024
    tamanho = int(tamanho)
else:
    tamanho = int(input("Tamanho do Arquivo em: "))

tipodoTempo = input("Tipo do Tempo \n(h = Hora, m = Minuto, s = Segundo): ")
if tipodoTempo == 'h' or tipodoTempo == 'H':
    tempo = float(((tamanho / velocidade) / 60) / 60)
    print("Falta %f Hora(s)" %tempo)
elif tipodoTempo == 'm' or tipodoTempo == 'M':
    tempo = float((tamanho / velocidade) / 60)
    print("Falta %f Minuto(s)" %tempo)
elif tipodoTempo == 's' or tipodoTempo == 'S':
    tempo = float(tamanho / velocidade)
    print("Falta %f Segundo(s)" %tempo)
