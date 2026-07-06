# Reto 1: **El Auditor de Interacciones**

## Objetivo

En este reto practicarás el uso de **listas anidadas**, el método **`append()`** y los **ciclos `for`** para analizar información de publicaciones en una red social.

---

## Contexto

Tienes la siguiente lista que representa las interacciones de tres publicaciones.

Cada sublista almacena la información en el siguiente orden:

- Índice `0`: Likes ❤️
- Índice `1`: Guardados 📌

```python
interacciones = [
    [50, 10],
    [1200, 300],
    [5, 1]
]
```

---

## Misión

### 1. Agregar una nueva publicación

Se ha publicado un nuevo post que obtuvo:

- **80 Likes**
- **15 Guardados**

Agrégalo al final de la lista utilizando el método **`append()`**.

> **Pista:** Debes agregar la lista completa:

```python
[80, 15]
```

---

### 2. Recorrer las publicaciones

Crea un ciclo **`for`** que recorra toda la lista de interacciones.

---

### 3. Hacker Challenge (Opcional) 

Durante el recorrido, verifica la cantidad de **likes** de cada publicación.

- Si un post tiene **más de 1000 likes**, imprime:

```text
¡Post Viral! 
```

- En caso contrario, imprime:

```text
Post con rendimiento normal
```

> **Pista:** Los likes se encuentran en el índice **0** de cada sublista.

---
# Reto 2: Gestión de Inventarios en Videojuegos (Listas + POO)

## 1. El Concepto: Coleccionando Objetos como en un Videojuego

En videojuegos como **Minecraft**, **World of Warcraft** o **The Legend of Zelda**, el personaje dispone de un **inventario** donde almacena todos los objetos que encuentra durante la aventura.

Para un programador, ese inventario puede representarse mediante una **lista** de Python. Sin embargo, una lista de textos como:

```python
["Espada", "Escudo", "Poción"]
```

resulta muy limitada.

En un videojuego real, una espada tiene información adicional como:

- Nombre
- Tipo
- Daño
- Peso
- Rareza
- Durabilidad

Por esta razón utilizamos **Programación Orientada a Objetos (POO)**.

Primero definimos un **molde** (una clase) que represente un objeto del juego y luego almacenamos esos objetos dentro de una lista.

---

# 2. Creando el Molde: La Clase `Item`

Cada objeto del inventario tendrá:

- Un nombre.
- Un tipo (Arma, Poción o Escudo).
- Un valor de poder que representa el daño o la curación que proporciona.

```python
class Item:

    def __init__(self, nombre, tipo, poder):
        self.nombre = nombre
        self.tipo = tipo      # "Arma", "Poción" o "Escudo"
        self.poder = poder    # Daño o curación
```

---

# 3. Creando el Inventario del Jugador

Ahora construiremos la mochila del jugador.

Observa que la lista no almacena textos ni números, sino **objetos de la clase `Item`**.

```python
# Mochila inicial del jugador

mochila = [
    Item("Espada de Hierro", "Arma", 45),
    Item("Poción de Vida", "Poción", 50),
    Item("Escudo de Madera", "Escudo", 20)
]

print(f"Mochila cargada. Tienes {len(mochila)} ítems en tu inventario.")
```

---

# 4. Operaciones con los Objetos de la Lista

Ahora utilizaremos los métodos de listas que ya conocemos (`append()`, índices y `for`), pero interactuando con los **atributos de cada objeto** mediante el operador punto (`.`).

---

## A. Acceder a un objeto específico

Si el jugador desea equipar el primer objeto del inventario:

```python
print(f"Has equipado: {mochila[0].nombre}")
print(f"Daño base: {mochila[0].poder}")
```

**Salida esperada**

```text
Has equipado: Espada de Hierro
Daño base: 45
```

---

## B. Modificar un objeto dentro de la lista

Un hechicero mejora la espada del jugador aumentando su poder en **15 puntos**.

```python
mochila[0].poder += 15

print(
    f"¡Tu {mochila[0].nombre} ha sido mejorada! Nuevo poder: {mochila[0].poder}"
)
```

**Salida**

```text
¡Tu Espada de Hierro ha sido mejorada! Nuevo poder: 60
```

---

## C. Agregar un nuevo objeto al inventario (`append()`)

El jugador derrota a un monstruo y obtiene un nuevo botín.

```python
botin = Item("Daga de Cristal", "Arma", 85)

mochila.append(botin)
```

Ahora el inventario contiene **4 objetos**.

---

# 5. Recorriendo el Inventario

Podemos mostrar el contenido completo de la mochila utilizando un ciclo `for`.

```python
print("\n---  INVENTARIO DEL JUGADOR ---")

for objeto in mochila:

    print(f"🔹 Ítem: {objeto.nombre}")
    print(f"   Tipo: {objeto.tipo}")
    print(f"   Poder/Efecto: {objeto.poder} pts")
    print("-" * 35)
```

---

#  Ejercicio Práctico: **El Filtro de Combate**

## Objetivo

Antes de enfrentarse al jefe final, el jugador desea visualizar únicamente las **armas** disponibles en su inventario.

---

## Instrucciones

1. Copia el código completo desarrollado anteriormente:
   - La clase `Item`.
   - La lista `mochila` con los **4 objetos** acumulados.

2. Crea un ciclo `for` que recorra toda la lista `mochila`.

3. Durante el recorrido, verifica el tipo de cada objeto.

---

## Misión de Combate 

Si el objeto actual es de tipo **"Arma"**, imprime el siguiente mensaje:

```text
¡LISTA PARA LUCHAR! Puedes usar tu {objeto.nombre} (Poder: {objeto.poder})
```

Si el objeto es una **Poción** o un **Escudo**, simplemente ignóralo (no imprimas ningún mensaje).

---
