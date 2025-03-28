numero = 0
while numero != 201:

    numero = int(input("ingrese su edad: (ingrese 201 para finalizar) "))
    if numero < 3:
        print("Entrada gratis")
    elif numero >= 3 and numero <= 12:
        print("La entrada cuesta $10")
    else:
        print("La entrada esta $15")