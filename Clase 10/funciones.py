def construir_perfil(nombre, apellido, **info_usuario):
    """Construye un diccionario con todo lo que sabemos sobre un usuario."""
    info_usuario['nombre'] = nombre
    info_usuario['apellido'] = apellido
    return info_usuario
    
        
def hacer_pizza(tamaño, *toppings):
    """Resumen de la pizza que vamos a hacer."""
    print(f"\nHaciendo una pizza de {tamaño} pulgadas con los siguientes toppings:")
    for topping in toppings:
        print(f"- {topping}")

