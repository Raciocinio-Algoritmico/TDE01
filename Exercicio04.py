PI = 3.1415
raio = float(input("Digite o raio do círculo: "))

area = PI * (raio ** 2)

print("A área do círculo é " + str(area))

#Imprimindo com duas casas decimais
print("A área do círculo é {:.2f}".format(area))