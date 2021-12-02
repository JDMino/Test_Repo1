numero = int(input("Escriba un número positivo por favor: "))
while numero < 0:
    print("Ha escrito un número negativo")
    numero = int(input("Escriba un número positivo: "))
print("Correcto")