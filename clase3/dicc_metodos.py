producto = {
    "id": 1204,
    "nombre": "Audifonos Gamer",
    "precio": 89.99,
    "disponible": True
}

# el método .get() viene a solucionar el problema de KeyError, es decir, permite conultar de forma segura el dicc.
# Si la llave existe, te devuelve el valor
# Si no existe...
nombre_item = producto["nombre"]
print(nombre_item)

descuento = producto.get("descuento", 0.0)
print(descuento)

precio = producto.get("precio")
print(precio)

# Los métodos extractores
#.keys(): extrae todas las llaves existentes en el dicc (nombre de las propiedades)
#.values(): extrae todos los valores existentes en el dicc (los datos guardados)

propiedades = producto.keys()
print(propiedades)

datos = producto.values()
print(datos)