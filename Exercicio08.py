from math import ceil

PI = 3.1415
LITROS_POR_LATA = 5
CUSTO_LATA = 50.00
METROS_POR_LITRO = 3
METROS_POR_LATA = LITROS_POR_LATA * METROS_POR_LITRO

alturaCilindro = float(input("Digite a altura do cilindro em metros: "))
raioCilindro = float(input("Digite o raio do cilindro em metros: "))

areaBase = PI * (raioCilindro ** 2)
areaLateral = (2 * PI) * raioCilindro * alturaCilindro 
areaTotal = ((2 * areaBase) + areaLateral) 

#Pode-se utilizar a função ceil da biblioteca math para arrendodar para cima o valor decimal e convertê-lo para inteiro
qtdeDeLatas = ceil(areaTotal / METROS_POR_LATA)
valorTotal = qtdeDeLatas * CUSTO_LATA

print("São necessárias " + str(qtdeDeLatas) + " para pintar o cilindro.")
print("O custo total será de R$: {:.2f}".format(valorTotal))