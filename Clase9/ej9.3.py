ingredientes = ""
while ingredientes != "salir":
    ingredientes = input( "Decime los ingredientes para la pizza (escribi ' salir ' para terminar)")
    print(f"voy a agregar {ingredientes} a la pizza")
    if ingredientes == "salir":
        print("Fin de la lista")
        break