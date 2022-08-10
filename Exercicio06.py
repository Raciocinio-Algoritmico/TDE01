from math import hypot

catetoOposto = float(input("Digite o valor do cateto oposto: "))
catetoAdjacente = float(input("Digite o valor do cateto adjacente: "))

#fórmula simples sem utilizar biblioteca
hipotenusa = (catetoOposto ** 2 + catetoAdjacente ** 2) ** (0.5)

#Utilizando função hypot (calcula hipotenusa) da biblioteca math
hipotenusaHypot = hypot(catetoOposto, catetoAdjacente)

print("A hipotenusa do triângulo é {:.2}".format(hipotenusa))
print("A hipotenusa do triângulo é {:.2}".format(hipotenusaHypot))