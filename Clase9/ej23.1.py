def ciudad_pais(ciudad, pais):
    lugar = f"{ciudad}, {pais}"
    return lugar.title()

lugar1 = ciudad_pais("brazilia", "brasil")
lugar2 = ciudad_pais("cABA", "argentina")
lugar3 = ciudad_pais("berlin","alemaña")

print(lugar1)
print(lugar2)
print(lugar3)