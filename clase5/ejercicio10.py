ciudades = (
    ("Montería",    8.75, -75.88),
    ("Bogotá",      4.71, -74.07),
    ("Medellín",    6.24, -75.57),
    ("Cali",        3.45, -76.53),
    ("Barranquilla",10.98, -74.80)
)

for tupla in ciudades:
    print(f"Ciudad: {tupla[0]}")
    print(f"Latitud: {tupla[1]}")
    print(f"Longitud: {tupla[2]}\n\n")
