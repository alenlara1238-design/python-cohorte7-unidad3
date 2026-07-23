productos = [
    {"nombre": "Mouse", "precio": 40, "stock": 25},
    {"nombre": "Teclado", "precio": 80, "stock": 15},
    {"nombre": "Monitor", "precio": 200, "stock": 10},
    {"nombre": "Impresora", "precio": 150, "stock": 5},
    {"nombre": "Auriculares", "precio": 60, "stock": 30},
    {"nombre": "Webcam", "precio": 70, "stock": 20},
    {"nombre": "Disco Duro", "precio": 100, "stock": 12}
]



def obtener_stock(producto):
    return producto["stock"]

def obtener_nombre(producto):
    return producto["nombre"]

productos_ordenados = sorted(
                            productos,
                            key =lambda producto: producto["stock"],
                            reverse=True)


for producto in productos_ordenados:
    print(producto)
