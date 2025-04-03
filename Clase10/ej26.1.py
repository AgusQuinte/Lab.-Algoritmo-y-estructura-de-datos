import funciones 

pizza = funciones.hacer_pizza(16, 'pepperoni')
pizza2 = funciones.hacer_pizza(12, 'champiñones', 'pimientos verdes', 'queso extra')

perfil_usuario = funciones.construir_perfil('albert', 'einstein',
                                  ubicacion='princeton',
                                  campo='física')
print(f"EL usuario: {perfil_usuario}")