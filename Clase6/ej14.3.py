usuarios_actuales = ["julian", "pedro", "roman", "isabel", "monica"]
usuarios_nuevos = ["julian", "Alvaro", "Monica", "ramiro", "jOSe"]

for minus in range(5):
    usuarios_nuevos[minus] = usuarios_nuevos[minus].lower()

for usuario in usuarios_actuales:
        if usuario in usuarios_nuevos:
            print(f"{usuario} Ya esta en uso, debe usar otro nombre de usuario")
        else: 
             
             print(f"Se puede usar este usuario: {usuario}")

