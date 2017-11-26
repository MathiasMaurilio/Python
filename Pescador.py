pdp = int(input("Entre Com Rendimento do Dia: "))
if pdp <= 50:
    print ("Q Excedidos = 0")
    print ("Multa = 0")
elif pdp > 50:
    pde = pdp - 50
    pdm = float((pdp - 50) * 4)
    print ("Q Excedidos = %d " %pde)
    print ("Multa = %d RS" %pdm)
