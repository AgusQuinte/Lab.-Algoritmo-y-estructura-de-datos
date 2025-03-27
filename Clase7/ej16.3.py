lenguajes_favoritos = {''
    'Juan': 'python',
    'Sara': 'c', 
    'Eduardo': 'rust',
    'Agustina': 'c#'
    }
personas = ["juan", "ramiro", "jose", "eduardo", "gonzalo"]

for nombre in lenguajes_favoritos:
    if nombre.lower() in personas:
        print(f"{nombre} gracias por responder la encuesta")
    else:
        print(f"{nombre} Puede responder aqui...")