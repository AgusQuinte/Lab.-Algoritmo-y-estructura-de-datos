mensaje = ["Buenas noches, que lindo que estes acompanandome esta noche aca, estoy muy agradecido.", "Holaaa, gracias por venir, te extrañe un montoon", "Como estas? Todo bien? Hacia mucho tiempo no te veia por aca."]
personas = ["Juan", "Micaela", "jorge"]

faltas = personas.pop(1)
personas.insert(1, "Pedro")
print(f"Mensaje para {personas[0]}: {mensaje[0]}")
print(f"Mensaje para {personas[1]}: {mensaje[1]}")
print(f"Mensaje para {personas[2]}: {mensaje[2]}")

print(faltas,"No pudo venir")
print("Consegui una mesa mas grande, entran 3 personas mas. ")
personas.insert(0, "Michael")
personas.insert(2, "Gabriela")


print("La nueva lsitas de invitados: ")
print(f"\nMensaje para {personas[0]}: {mensaje[0]}") 
print(f"\nMensaje para {personas[1]}: {mensaje[1]}")
print(f"\nMensaje para {personas[2]}: {mensaje[2]}")
print(f"\nMensaje para {personas[3]}: {mensaje[0]}")
print(f"\nMensaje para {personas[4]}: {mensaje[1]}")

print("Lamento anunciarles que solo podre invitar a 2 personas esta noche-.")
print (*personas)
for i in range (3):
    adios = personas.pop(0)
    print( f"Surgio un inconveniente a ultimo momento, lamnento que no pueda venir esta noche {adios}")

print(f"{personas[0]}, vos seguis invitado para esta noche")
print(f"{personas[1]}, vos seguis invitado para esta noche")
del personas[1]
del personas[0]
print(*personas)