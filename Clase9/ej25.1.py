def armar_sandwich(*ingredientes):
    print("El sandwich debe tener los siguientes ingredientes: ")

    for ingrediente in ingredientes:
        print(f" {ingrediente}")

armar_sandwich("jamon", "Queso", "tomate")
armar_sandwich("Rucula", "Queso", "tomate")
armar_sandwich("Salame", "Lechuga", "tomate")