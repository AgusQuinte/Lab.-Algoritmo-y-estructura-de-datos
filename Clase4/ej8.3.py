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
personas.append("Manuel")

print("La nueva lsitas de invitados: ")
print(f"\nMensaje para {personas[0]}: {mensaje[0]}") 
print(f"\nMensaje para {personas[1]}: {mensaje[1]}")
print(f"\nMensaje para {personas[2]}: {mensaje[2]}")
print(f"\nMensaje para {personas[3]}: {mensaje[0]}")
print(f"\nMensaje para {personas[4]}: {mensaje[1]}")