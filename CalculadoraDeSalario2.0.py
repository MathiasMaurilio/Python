sph = input("Digite Quanto Ganha Por Hora: ")
nhm = input("Digite Quantas Horas Voce Trabalhou no Mes: ")
stm = sph * nhm
idr = (11/100.0) * stm
ins = (8/100.0) * stm
sdt = (5/100.0) * stm
slr = stm - (idr + ins + sdt)

print "+ Salario Bruto: %sRS" % (stm)
print '- IR (11p): %sRS' % (idr)
print "- INSS (8p): %sRS" % (ins)
print "- Sindicato (5p): %sRS" % (sdt)
print "= Salario Liquido: %sRS" % (slr)
