def construir_perfil(nombre, apellido, **info_usuario):
    """Construye un diccionario con todo lo que sabemos sobre un usuario."""
    info_usuario['nombre'] = nombre
    info_usuario['apellido'] = apellido
    return info_usuario
perfil_usuario = construir_perfil("Agustin", "Quintela", deporte= "futbol", colegio="Huergo")

print(perfil_usuario)

