edad = int(input("Ingrese su edad: "))

if edad < 2:
    print("Es un bebe")
elif edad >= 2 and edad < 4:
    print("Es un nene/a chiquito/a") 
elif edad >= 4 and edad < 13:
    print("Es un nene/a") 
elif edad >= 13 and edad < 20:
    print("Es un/a adolecente") 
elif edad >= 20 and edad < 65:
    print("Es un/a adulto/a")
else:
    print("Es un/a adulto/a mayor")