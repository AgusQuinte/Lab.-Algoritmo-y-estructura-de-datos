pizza = ["muzzarela", "napolitana", "fugazeta"]
pizza_amigo = ["muzzarela", "napolitana", "fugazeta"]
for a in pizza:
    print ("Me gusta la pizza de:", (a))

print ("me encanta hecha al horno")
pizza.append("caprese")
pizza_amigo.append("peperoni")

print("Mis pizzas favoritas son")
for i in pizza:
    print(i)
print("Las pizzas favoritas de mi amigo son")
for i in pizza_amigo:
    print(i)