# ¿Por qué existen las tuplas en Python?

Cuando comenzamos a programar es común preguntarse por qué Python tiene **listas** y también **tuplas**, si ambas permiten almacenar varios datos en una sola variable.

La principal diferencia es que una **tupla es inmutable**, es decir, una vez creada **no puede modificarse**. Esta característica no es una limitación; por el contrario, es una ventaja en muchos escenarios de programación.

## Garantizar que los datos no cambien

En muchas aplicaciones existen datos que deben permanecer exactamente iguales durante toda la ejecución del programa.

Por ejemplo:

- Las coordenadas geográficas de una ciudad.
- Los días de la semana.
- Los meses del año.
- La resolución de una imagen.
- Las dimensiones de un objeto.

Si estos datos se almacenan en una tupla, ningún fragmento del programa podrá modificarlos accidentalmente.

```python
dias_semana = (
    "Lunes",
    "Martes",
    "Miércoles",
    "Jueves",
    "Viernes",
    "Sábado",
    "Domingo"
)
```

## Representar un único registro

Las tuplas son ideales para representar un conjunto de datos relacionados que describen un solo elemento.

Por ejemplo, un estudiante:

```python
estudiante = (
    1025,
    "Laura",
    20
)
```

Aquí la tupla representa un único registro compuesto por:

- Código
- Nombre
- Edad

Generalmente ese registro no cambia durante el procesamiento inmediato de una función.

## Devolver varios valores desde una función

Uno de los usos más comunes de las tuplas es permitir que una función retorne varios valores al mismo tiempo.

```python
def calcular(a, b):
    suma = a + b
    resta = a - b
    return suma, resta

resultado = calcular(8, 3)

print(resultado)
```

Salida:

```
(11, 5)
```

Python realmente está devolviendo una tupla.

También es posible desempaquetarla:

```python
suma, resta = calcular(8, 3)

print(suma)
print(resta)
```

## Mejor rendimiento

Las tuplas ocupan menos memoria que las listas y, en muchas operaciones, son ligeramente más rápidas porque Python sabe que su contenido nunca cambiará.

Aunque la diferencia suele ser pequeña, en programas que procesan millones de datos puede representar una ventaja importante.

## Uso como claves de diccionarios

Las listas no pueden utilizarse como claves en un diccionario porque son mutables.

Las tuplas sí pueden hacerlo.

```python
ciudades = {
    (8.75, -75.88): "Valledupar",
    (10.98, -74.80): "Santa Marta",
    (4.71, -74.07): "Bogotá"
}
```

Cada coordenada se representa mediante una tupla.

## Uso en el desarrollo de software

En aplicaciones reales las tuplas aparecen con mucha frecuencia:

- Coordenadas `(x, y)` en videojuegos.
- Coordenadas `(latitud, longitud)` en aplicaciones de mapas.
- Valores RGB `(255, 255, 255)` para representar colores.
- Dimensiones `(ancho, alto)` de imágenes o ventanas.
- Resultados devueltos por funciones.
- Registros temporales que no deben modificarse.

## ¿Cuándo usar una lista y cuándo una tupla?

Utiliza una **lista** cuando los datos cambiarán durante la ejecución del programa:

- Agregar elementos.
- Eliminar elementos.
- Modificar información.

Utiliza una **tupla** cuando los datos deben permanecer constantes o representan un conjunto fijo de valores relacionados.

### Comparación inmediata con listas
| Lista                        | Tupla                  |
| ---------------------------- | ---------------------- |
| Mutable                      | Inmutable              |
| []                           | ()                     |
| append()                     | No existe              |
| remove()                     | No existe              |
| pop()                        | No existe              |
| Ideal para datos que cambian | Ideal para datos fijos |


# Ejercicios Progresivos: Tuplas en Python

A continuación encontrarás una serie de ejercicios organizados de menor a mayor dificultad. El objetivo es familiarizarse con la creación, acceso y uso de las tuplas en situaciones similares a las que se presentan en programas reales.

---

# Ejercicio 1. Mi primera tupla

Crea una tupla llamada `frutas` que almacene las siguientes frutas:

- Manzana
- Pera
- Mango
- Uva

Después imprime la tupla completa.

**Salida esperada (similar):**

```
('Manzana', 'Pera', 'Mango', 'Uva')
```

---

# Ejercicio 2. Acceder a un elemento

Utiliza la tupla del ejercicio anterior e imprime únicamente:

- La primera fruta.
- La última fruta.

**Pista:** utiliza índices.

---

# Ejercicio 3. Contar elementos

Con la misma tupla responde:

- ¿Cuántas frutas contiene?
- Muestra ese número en pantalla.

**Salida esperada (similar):**

```
Cantidad de frutas: 4
```

---

# Ejercicio 4. Recorrer una tupla

Recorre la tupla utilizando un ciclo `for` e imprime cada fruta en una línea diferente.

**Salida esperada**

```
Manzana
Pera
Mango
Uva
```

---

# Ejercicio 5. Buscar un elemento

Crea una tupla con los siguientes cursos:

- Python
- Java
- JavaScript
- SQL
- Git

Pregunta al usuario qué curso desea buscar.

Si existe en la tupla muestra:

```
El curso está disponible.
```

En caso contrario:

```
El curso no existe.
```

---

# Ejercicio 6. Contar repeticiones

Crea la siguiente tupla:

```python
numeros = (4, 7, 8, 4, 9, 2, 4, 6, 7)
```

Muestra:

- Cuántas veces aparece el número 4.
- Cuántas veces aparece el número 7.

---

# Ejercicio 7. Encontrar la posición

Usando la siguiente tupla:

```python
lenguajes = (
    "Python",
    "Java",
    "C#",
    "JavaScript",
    "Go"
)
```

Encuentra la posición donde aparece `"JavaScript"`.

**Salida esperada**

```
JavaScript está en la posición 3
```

---

# Ejercicio 8. Desempaquetar una tupla

Crea la siguiente tupla:

```python
persona = (
    "Carlos",
    22,
    "Ingeniería"
)
```

Desempaqueta sus valores en tres variables:

- nombre
- edad
- carrera

Luego imprime:

```
Nombre: Carlos
Edad: 22
Carrera: Ingeniería
```

---

# Ejercicio 9. Función que devuelve una tupla

Escribe una función llamada `calcular()` que reciba dos números y retorne:

- La suma.
- La multiplicación.

Después llama la función y muestra ambos resultados.

Ejemplo:

```
Suma: 15
Multiplicación: 56
```

---

# Ejercicio 10. Coordenadas de un mapa

Representa las coordenadas de cinco ciudades mediante tuplas.

Ejemplo:

```python
ciudades = (
    ("Montería", 8.75, -75.88),
    ("Bogotá", 4.71, -74.07),
    ("Medellín", 6.24, -75.57),
    ("Cali", 3.45, -76.53),
    ("Barranquilla", 10.98, -74.80)
)
```

Recorre la estructura e imprime:

```
Ciudad: Montería
Latitud: 8.75
Longitud: -75.88

Ciudad: Bogotá
...
```

---

# Ejercicio 11. Registro de estudiantes

Crea una tupla que almacene cinco estudiantes.

Cada estudiante será otra tupla con:

- Código
- Nombre
- Nota final

Ejemplo:

```python
estudiantes = (
    (1001, "Laura", 4.8),
    (1002, "Carlos", 3.9),
    (1003, "Ana", 4.5),
    (1004, "Luis", 2.8),
    (1005, "Sara", 5.0)
)
```

Recorre todos los estudiantes e imprime únicamente aquellos cuya nota sea mayor o igual a 4.0.

---

# Ejercicio 12. Menú de restaurante

Representa el menú mediante una tupla.

Cada elemento contendrá:

- Nombre del plato.
- Precio.

Ejemplo:

```python
menu = (
    ("Hamburguesa", 22000),
    ("Pizza", 30000),
    ("Perro Caliente", 18000),
    ("Lasaña", 28000)
)
```

Recorre la tupla mostrando:

```
Hamburguesa - $22000
Pizza - $30000
...
```

---

# Ejercicio 13. Mini reto: Catálogo de videojuegos

Una tienda desea almacenar un catálogo fijo de videojuegos.

Cada videojuego tendrá:

- Nombre
- Plataforma
- Precio

Ejemplo:

```python
videojuegos = (
    ("Minecraft", "PC", 90000),
    ("EA Sports FC", "PS5", 280000),
    ("Forza Horizon", "Xbox", 240000),
    ("The Legend of Zelda", "Nintendo", 300000)
)
```

Realiza las siguientes tareas:

1. Mostrar todos los videojuegos.
2. Mostrar únicamente los nombres.
3. Calcular el precio total de todos los videojuegos.
4. Mostrar cuál videojuego tiene el precio más alto.
5. Contar cuántos videojuegos hay registrados.

---

# Desafío Final

Diseña un programa para gestionar un pequeño inventario de computadores utilizando únicamente tuplas.

Cada computador tendrá:

- Código
- Marca
- Procesador
- Memoria RAM
- Precio

El programa debe:

- Mostrar todos los computadores.
- Mostrar únicamente las marcas.
- Calcular el precio promedio.
- Encontrar el computador más costoso.
- Contar cuántos computadores tienen 16 GB o más de memoria RAM.

> **Restricción:** No se permite modificar las tuplas una vez creadas. Utiliza ciclos, condicionales y funciones para procesar la información.