ciudades = {
    "caba": {
        "pais": "Argentina",
        "poblacion": "3 millones", 
        "dato": "Tiene el puerto de la plata"
    },
    "londres":  {
        "pais": "Inglaterra",
        "poblacion": "9 millones", 
        "dato": "Es una de las ciudades mas viejas"
    },
    "brazilia": {
        "pais": "Brasil",
        "poblacion": "2.8 millones",
        "dato": "Es la capital de brasil"
    }
}
for ciudad, dato in ciudades.items():
    
    print(f"La ciudad de {ciudad}, queda ubicada en {dato['pais']} con una poblacion estimada de {dato['poblacion']}. Un dato extravagante de esta ciudad es que {dato['dato']} \n")