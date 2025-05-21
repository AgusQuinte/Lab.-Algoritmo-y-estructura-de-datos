from random import randint

class Die():
    
    def __init__(self, numero):
        self.numero = numero

    def roll_die(self, sides=6):
        self.sides = sides
        self.numero = randint(1, self.sides)
        return self.numero
for cara in range(10):
    dado1 = Die(6)
    print(f"Dado 1, tiro {cara+1} es {dado1.roll_die()}")

for cara in range (10):
    dado2 = Die(10)
    print(f"Dado 2, tiro {cara+1} es {dado2.roll_die(10)}")

for cara in range (10):
    dado3 = Die(20)
    print(f"Dado 3, tiro {cara+1} es {dado3.roll_die(20)}")