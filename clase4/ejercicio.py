class Carta:
    def __init__(self, nombre, poder):
        self.nombre = nombre
        self.poder = poder
    
    def __str__(self):
        return f"{self.nombre} (Poder): {self.poder}"

    def __eq__(self, otro):
        return (
            self.nombre == otro.nombre and
            self.poder == otro.poder
        )

    def __hash__(self):
        return hash((self.nombre, self.poder))

carta1 = Carta("Dragon magico", 95)
carta2 = Carta("Mago supreno", 88)

#print(carta1)
#print(carta2)

# crear una coleccion vacía
coleccion = set()

coleccion.add(carta1)
coleccion.add(carta2)

print("Antes de agregar tercera carta....")
for carta in coleccion:
    print(carta)

carta3 = Carta("Dragon magico", 95)
print("\nDespues de agregar tercera carta....")
coleccion.add(carta3)

for carta in coleccion:
    print(carta)