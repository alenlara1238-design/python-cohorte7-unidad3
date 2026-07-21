"""
numeros = [32,45,76,2345,565,231,454,565]

objetivo = 232
encontrado = False

for numero in numeros:
    if numero == objetivo:
        encontrado = True
        break

print(f"El numero fue encontrado? {encontrado}")
"""

def buscar(objetivo, lista):
    posicion = -1
    for numero in lista:
        posicion+=1
        if numero == objetivo:
            return posicion
            
    
    return -1

numeros = [32,45,76,2345,565,231,454,565]

resultado = buscar(1000, numeros)

if resultado == -1:
    print("El numero no está en la lista")
else:
    print(f"el número a buscar está en la lista  en la posición:{resultado}")