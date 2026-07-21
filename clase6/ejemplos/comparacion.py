import time

# --- PREPARACIÓN DE DATOS ---
NUM_ELEMENTOS = 1_000_000
# El elemento a buscar estará al final para evaluar el peor caso de la lista
OBJETIVO = "elemento_999999"

print(" Creando estructuras de datos...")
# Lista desordenada
lista_datos = [f"elemento_{i}" for i in range(NUM_ELEMENTOS)]

# Diccionario (Hash Map)
diccionario_datos = {f"elemento_{i}": True for i in range(NUM_ELEMENTOS)}

print("✓ Estructuras creadas con éxito.\n")


# --- 1. BÚSQUEDA LINEAL EN LISTA DESORDENADA ---
inicio = time.perf_counter()

# Búsqueda en la lista (recorre uno por uno)
encontrado_lista = OBJETIVO in lista_datos

fin = time.perf_counter()
tiempo_lista = fin - inicio


# --- 2. BÚSQUEDA DIRECTA EN DICCIONARIO ---
inicio = time.perf_counter()

# Búsqueda en el diccionario (acceso por clave)
encontrado_dicc = OBJETIVO in diccionario_datos

fin = time.perf_counter()
tiempo_dicc = fin - inicio


# --- RESULTADOS ---
print("=" * 45)
print(f" RESULTADOS DE BÚSQUEDA ({NUM_ELEMENTOS:,} elementos)")
print("=" * 45)
print(f"Lista (Búsqueda Lineal):   {tiempo_lista:.6f} segundos")
print(f"Diccionario (Tabla Hash):  {tiempo_dicc:.6f} segundos")
print("-" * 45)

if tiempo_dicc > 0:
    diferencia = tiempo_lista / tiempo_dicc
    print(f"¡El diccionario fue {diferencia:,.0f} veces más rápido!")
