pedidos_sandwiches = ["Hamburguesa", "Pastron", "Bondiola", "Tostado", "Pastron", "Pastron"]
print("La sandwichera se quedo sin pastron")

while "Pastron" in pedidos_sandwiches:
    pedidos_sandwiches.remove("Pastron")

print("Los pedidos de sandwiches sin pastron son:", *pedidos_sandwiches)