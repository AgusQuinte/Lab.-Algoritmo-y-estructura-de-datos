estadisticas = { }
while True:
    usuario = input("Cual es tu nombre?: ")
    destino = input("Cual seria tu destino de vacaciones soñado?: ")
    estadisticas[usuario] = destino
    si_no = input("Hay mas usuarios? (si/no): ")
    if si_no == "no":
        break 
    else: 
        continue

print("La encuenta quedo asi: ")
for usuario, destino in estadisticas.items():
    print(f"A {usuario} le gustaria viajar a {destino}")