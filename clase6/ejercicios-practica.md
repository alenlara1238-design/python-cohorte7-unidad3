# Ejercicio 1. Primera búsqueda lineal

## Objetivo

Recorrer una lista hasta encontrar un elemento.

## Enunciado

Se tiene la siguiente lista de números:

```python
numeros = [12, 8, 45, 21, 30, 18, 50]
```

Desarrolle un programa que:

- Solicite al usuario un número.
- Recorra la lista elemento por elemento.
- Si el número existe, muestre el mensaje:

```text
Número encontrado.
```

- Si el número no existe, muestre:

```text
Número no encontrado.
```

### Restricciones

- No utilizar el operador `in`.
- Utilizar un ciclo.
- No crear funciones.

---

# Ejercicio 2. Encontrar la posición

## Objetivo

Comprender que una búsqueda también puede devolver la ubicación del elemento.

## Enunciado

Utilice la siguiente lista:

```python
ciudades = [
    "Bogotá",
    "Medellín",
    "Cali",
    "Cartagena",
    "Barranquilla"
]
```

Desarrolle un programa que:

- Solicite una ciudad.
- Busque la ciudad recorriendo la lista.
- Si existe, muestre:

```text
La ciudad fue encontrada en la posición X.
```

- Si no existe, muestre:

```text
La ciudad no está registrada.
```

### Restricciones

- No utilizar `.index()`.
- No utilizar `in`.

---

# Ejercicio 3. Crear una función de búsqueda

## Objetivo

Modularizar una búsqueda.

## Enunciado

Cree una función llamada:

```python
buscar_producto(lista, nombre)
```

La función debe recorrer la lista y retornar:

- `True` si el producto existe.
- `False` en caso contrario.

Utilice la función con la siguiente lista:

```python
productos = [
    "Mouse",
    "Monitor",
    "Teclado",
    "Webcam",
    "Audífonos"
]
```

---

# Ejercicio 4. Buscar un objeto

## Objetivo

Aplicar una búsqueda sobre una colección de objetos.

## Enunciado

Cree la clase `Libro` con los siguientes atributos:

- Código
- Título
- Autor

Construya una colección con varios libros.

Después:

- Solicite un código al usuario.
- Encuentre el libro correspondiente.
- Si existe, muestre toda su información.
- Si no existe, informe que no fue encontrado.

---

# Ejercicio 5. Búsqueda en un diccionario

## Objetivo

Consultar información utilizando claves.

## Enunciado

Se tiene el siguiente diccionario:

```python
productos = {
    "P001": "Mouse",
    "P002": "Monitor",
    "P003": "Teclado",
    "P004": "Impresora"
}
```

Desarrolle un programa que:

- Solicite un código.
- Si el código existe, muestre el nombre del producto.
- Si no existe, informe que el código no está registrado.

### Restricciones

- Utilice únicamente las operaciones propias del diccionario.

---

# Ejercicio 6. Verificación con sets

## Objetivo

Comprobar la existencia de un elemento.

## Enunciado

Un sistema almacena los siguientes correos electrónicos registrados:

```python
correos = {
    "ana@gmail.com",
    "juan@gmail.com",
    "carlos@gmail.com",
    "maria@gmail.com"
}
```

Desarrolle un programa que:

- Solicite un correo electrónico.
- Indique si el correo ya se encuentra registrado.

### Restricciones

- No recorrer manualmente la colección.

---

# Ejercicio 7. Comparando estructuras

## Objetivo

Analizar diferentes formas de consultar información.

## Enunciado

Un sistema maneja la siguiente información.

### Estudiantes

```python
estudiantes = [
    "Ana",
    "Carlos",
    "Laura",
    "Pedro"
]
```

### Notas

```python
notas = {
    "Ana": 4.5,
    "Carlos": 3.8,
    "Laura": 4.9,
    "Pedro": 4.0
}
```

### Club

```python
club = {
    "Ana",
    "Pedro"
}
```

Realice las siguientes operaciones:

- Verifique si **Laura** existe como estudiante.
- Consulte la nota de **Carlos**.
- Verifique si **Ana** pertenece al club.

### Preguntas de reflexión

Al finalizar, responda:

1. ¿Qué diferencias encontró entre las formas de realizar cada consulta?
2. ¿Cuál considera más apropiada para cada caso? Justifique su respuesta.

---

# Ejercicio 8. Inventario de productos

## Objetivo

Aplicar búsquedas utilizando Programación Orientada a Objetos.

## Enunciado

Desarrolle la clase `Producto` con los siguientes atributos:

- Código
- Nombre
- Precio

Posteriormente cree la clase `Inventario`.

Esta clase deberá almacenar los productos y ofrecer un método que permita localizar un producto a partir de su código.

Si el producto existe, el método deberá retornar el objeto correspondiente.

Si no existe, deberá retornar `None`.

---

# Ejercicio 9. Comparación práctica

## Objetivo

Comprender de forma intuitiva la eficiencia de distintas formas de consultar información.

## Enunciado

Construya una colección con al menos **100 productos**.

Posteriormente organice la misma información de otra manera para poder realizar consultas utilizando el código del producto.

Realice las siguientes búsquedas:

- Primer producto.
- Producto ubicado aproximadamente en la mitad.
- Último producto.
- Un producto inexistente.

### Preguntas de reflexión

Responda:

1. ¿Cuál búsqueda requirió revisar más elementos?
2. ¿Qué diferencias observó entre ambas formas de realizar las consultas?
3. ¿Cuál utilizaría para buscar productos por código? Explique.

> **Nota:** No es necesario medir tiempos de ejecución; basta con analizar cuántos elementos es necesario revisar en cada caso.

---

# Ejercicio 10. Sistema de Gestión de Biblioteca

## Objetivo

Integrar diferentes formas de almacenar y consultar información dentro de un mismo sistema.

## Enunciado

Desarrolle un sistema para administrar una biblioteca.

### Clase `Libro`

Debe contener los siguientes atributos:

- Código
- Título
- Autor
- Categoría

### Clase `Biblioteca`

Debe administrar la información necesaria para el funcionamiento del sistema.

### Funcionalidades

El sistema debe permitir:

- Agregar un libro.
- Buscar un libro por código.
- Consultar un libro mediante su código.
- Verificar si una categoría existe.
- Mostrar todos los libros registrados.

### Preguntas de reflexión

Al finalizar el desarrollo, responda:

1. ¿Qué diferencias encontró entre las distintas formas de buscar un libro?
2. ¿Por qué resulta útil validar si una categoría existe?
3. ¿En qué situaciones utilizaría una colección secuencial para almacenar información?
4. ¿Qué ventajas ofrece cada forma de organizar los datos dentro del sistema?