hora = int(input("Digite a hora: "))
minutos = int(input("Digite os minutos: "))
segundos = int(input("Digite os segundos: "))

horaEmMinutos = hora * 60
totalMinutos = horaEmMinutos + minutos

minutosEmSegundos = totalMinutos * 60
totalSegundos = minutosEmSegundos + segundos

print("Passaram " + str(totalMinutos) + " minutos desde o início do dia.")
print("Passaram " + str(totalSegundos) + " segundos desde o início do dia.")