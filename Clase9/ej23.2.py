
def hacer_album(artista, titulo, cantidad= None):
    musica = {}
    musica["artista"] = artista
    musica["titulo"] = titulo
    if cantidad:
        musica["cantidad"] = cantidad
    return musica
album1 = hacer_album("Queen", "Raimbow")
album2 = hacer_album("Fito Paez", "Cuidado")
album3 = hacer_album("Luck ra", "Que me falte todo")
album4 = hacer_album("Callekeros", "Prohibido", 20)

print(album1)
print(album2)
print(album3)
print(album4)
