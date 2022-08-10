precoProduto = float(input("Valor do produto: "))

valorComJuros = precoProduto + (precoProduto * 0.05)
parcelaComJuros = valorComJuros / 3

parcelaSemJuros = precoProduto / 2

valorAVista = precoProduto - (precoProduto * 0.05)

#Se você não tiver imprimido com formatação para 2 números decimais NÃO TEM PROBLEMA
#Imprima concatenando (juntando com o +) as strings e está ótimo
print("O valor total em 3x com juros fica R$ {:.2f}".format(valorComJuros) + " em parcelas de R$ {:.2f}".format(parcelaComJuros))
print("O valor sem juros das parcelas em 2x é de R$ {:.2f}".format(parcelaSemJuros))
print("O valor à vista com desconto é de R$ {:.2f}".format(valorAVista))