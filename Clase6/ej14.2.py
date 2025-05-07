usuarios = ["juli", "barba", "admin", "agus", "lu"]
if usuarios: 
    for usuario in usuarios:
        if usuario == "admin":
            print("Hola admin, ¿Desea un informe de estado?")

        else:
            print(f"Hola {usuario}, gracias por volver a iniciar sesion")
else: 
    print("¡Necesitamos encontrar algunos usuarios!")

