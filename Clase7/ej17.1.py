persona_1 = {
    "nombre": "Ramiro",
    "apellido": "Fernandez",
    "ciudad": "CABA"
}

persona_2 = {
    "nombre": "Jose",
    "apellido": "Hernesto",
    "ciudad": "Rosario"
}

persona_3 = {
    "nombre": "Lucas",
    "apellido": "Barba",
    "ciudad": "Cordoba"
}

gente = [persona_1, persona_2, persona_3]

for key in gente:
    print(f"El nombre de mi amgigo es {key['nombre']} y su apellido {key['apellido']}. El vive en {key['ciudad']}")