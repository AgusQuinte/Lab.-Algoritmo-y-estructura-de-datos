
def hacer_album(artista, titulo, cantidad= None):
    musica = {}
    musica["artista"] = artista
    musica["titulo"] = titulo
    if cantidad:
        musica["cantidad"] = cantidad
    return musica

while True: 
    artist = input("Ingrese nombre del artista: ")
    titul = input("Ingresa titulo del album: ")
    si_no = input("Quiere salir? si/no: ")
    album = hacer_album(artist, titul)
    print(album)
    if si_no == "si":
        break
    else: 
        continue
