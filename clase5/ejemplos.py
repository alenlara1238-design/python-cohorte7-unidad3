


carrito = [
    "mouse",
    "teclado"
]

carrito.append("monitor")

fecha_nacimiento = (15,8,1998)

persona = (
    "Carlos",
    25,
    "ingeniero"
)


numero = (5,)

for dato in persona:
    print(dato)

print(len(persona))

if "ingeniero" in persona:
    print("la persona es ingeniero(a)")

print(persona.count("Carlos"))

print(persona.index("ingeniero"))

# desempaquetado
coordenada = (4.65656, -56.334, "medellin")

latitud = coordenada[0]

print(latitud)


def obtener_usuario():
    return "ana", 24

nombre, edad = obtener_usuario()

print(edad)


frutas = ("manzana", "pera", "mango", "uva")
print(frutas)

print(frutas[0])
print(frutas[3])


print(f"cantidad de frutas: {len(frutas)}")

