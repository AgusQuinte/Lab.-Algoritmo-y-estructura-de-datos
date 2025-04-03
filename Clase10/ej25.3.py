def hacer_auto(fabricante, modelo, **diseños_auto):
    """informacion de un auto"""
    diseños_auto["Fabricante"] = fabricante
    diseños_auto["Modelo"] = modelo
    return diseños_auto
auto = hacer_auto('toyota', 'corolla', color='gris', airbags=True)

print(auto)