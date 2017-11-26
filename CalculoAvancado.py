import math

n1 = input("Digite um Numero inteiro 1/2: ")
n2 = input("Digite um Numero inteiro 2/2: ")
n3 = input("Digite um Numero Real: ")

cp = n1*2 * (n2/2)
cs = (n1 * 3) + n3
ct = (n3 ** 3)

print "O Dobro de %s + metade de %s = %s"  % (n1, n2, cp)
print "A Soma do Triplo de %s com %s = %s" % (n1, n3, cs)
print "%s Elevado ao Cubo = %s"            % (n3, ct)
