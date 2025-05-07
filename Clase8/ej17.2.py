perro = {
    "animal": "perro",
    "tipo_animal": "canino",
    "nombre_dueño": "juan"
}
gato = {
    "animal": "gato",
    "tipo_animal": "felino",
    "nombre_dueño": "daniel"
}
loro = {
    "animal": "loro",
    "tipo_animal": "ave",
    "nombre_dueño": "ramona" 
}

mascotas = [perro, loro, gato]

for mascota in mascotas:
    print(f"El {mascota['animal']} es un {mascota['tipo_animal']} y su dueño se llama {mascota['nombre_dueño']}")