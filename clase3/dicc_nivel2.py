personaje = {
    "nombre": "Eldrin",
    "clase": "Mago",
    "vida": 100,
    "hechizos": ["teletransportacion", "bola de fuego", "invisibilidad"],
    "inventario": ["poción de vida", "espada", "veneno"]
}

# Acceder a un elemento en especifico
print(f"El tercer hechizo del mago {personaje['nombre']} es {personaje["hechizos"][2]}")

#Agregar elementos a la lista: Linterna magica
personaje["inventario"].append("linterna magica")

print(f"inventario actualizado: {personaje["inventario"]}")

# el personaje utilizó la posicón
personaje["inventario"].pop(0)
print(f"inventario actualizado: {personaje["inventario"]}")
