usuarios = ["juli", "barba", "admin", "agus", "lu"]

for usuario in usuarios:
    if usuario == "admin":
        print("Hola admin, ¿Desea un informe de estado?")
    else:
        print(f"Hola {usuario}, gracias por volver a iniciar sesion")
