salario = float(input("Digite o salário do funcionário: "))

salarioMinimo = 1212
quantidadeDeSalariosMinimos = salario / salarioMinimo

#Caso queira deixar apenas o número inteiro basta fazer o castin (converter) o resultado para int
quantidadeDeSalariosMinimosInt = int(salario / salarioMinimo)

print("O funcionário ganha " + str(quantidadeDeSalariosMinimos) + " salários-mínimos.")

#Como imprimir o valor com duas casas decimais
print("O funcionário ganha {:.2f}".format(quantidadeDeSalariosMinimos) + " salários-mínimos.")

#Imprimindo o valor inteiro (sem casas decimais)
print("O funcionário ganha " + str(quantidadeDeSalariosMinimosInt) + " salários-mínimos.")