# Clase: Introducción a los Diccionarios en Python

## 1. El Problema: ¿Qué vienen a solucionar?

Para entender por qué existen los **diccionarios**, primero debemos analizar las limitaciones de las **listas** cuando trabajamos con datos del mundo real.

Imagina que queremos almacenar la información del perfil de un usuario de Instagram: su nombre de usuario, la cantidad de seguidores y si su cuenta está verificada.

Con los conocimientos que tenemos sobre listas, podríamos hacerlo así:

```python
# Datos: Usuario, Seguidores, ¿Verificado?
perfil = ["@danipro", 1550, True]
```

A simple vista parece una buena solución, pero aquí empiezan los problemas.

### Problema 1: Debemos recordar las posiciones

Si queremos imprimir el número de seguidores, debemos recordar que ese dato se encuentra en la posición **1** de la lista.

```python
print(perfil[1])
```

Al leer el código, el número `1` no nos dice qué representa ese dato. Debemos memorizar que corresponde a los seguidores.

### Problema 2: Los índices pueden cambiar

Supongamos que más adelante decidimos almacenar también la edad del usuario al principio de la lista.

```python
perfil = [25, "@danipro", 1550, True]
```

Ahora el nombre de usuario ya no está en la posición `0`, sino en la `1`.

Los seguidores ya no están en la posición `1`, sino en la `2`.

Todo el código que utilizaba esos índices dejará de funcionar correctamente.

Este tipo de cambios hacen que el programa sea más difícil de mantener.

---

## La solución

Los seres humanos pensamos en conceptos, no en posiciones.

Cuando buscamos información de una persona pensamos en:

- Usuario
- Seguidores
- Edad
- Correo electrónico

No pensamos en:

- Posición 0
- Posición 1
- Posición 2

Para solucionar este problema, Python incorpora una estructura de datos llamada **diccionario**.

En un diccionario ya no accedemos a la información mediante un número de posición (índice), sino mediante una **clave** o **etiqueta** que describe el dato.

Por ejemplo:

- `"usuario"`
- `"seguidores"`
- `"edad"`
- `"verificado"`

Esto hace que el código sea mucho más fácil de leer, entender y mantener.

## 2. ¿Qué es un Diccionario y cuándo usarlo?

Un **diccionario** es una estructura de datos que almacena información mediante parejas de **Llave - Valor** (**Key - Value**).

Cada dato tiene una **llave** (también llamada **clave**) que lo identifica de forma única, y un **valor** asociado.

La gran ventaja de los diccionarios es que ya no necesitamos recordar posiciones numéricas como ocurre con las listas. En su lugar, utilizamos nombres descriptivos para acceder a la información.

### Una analogía sencilla

Piensa en un diccionario de idiomas tradicional.

Cuando deseas conocer el significado de la palabra **"Dog"**, no buscas en la página número 327 ni recuerdas una posición específica.

Simplemente buscas la palabra:

- **Llave:** `"Dog"`
- **Valor:** `"Perro"`

Lo importante es la **palabra** (la llave), no la posición donde se encuentra.

Los diccionarios de Python funcionan exactamente con esa misma idea.

Cada llave permite encontrar rápidamente el valor que tiene asociado.

### ¿Cuándo conviene usar un diccionario?

Imagina que estás programando un videojuego y necesitas almacenar la información de un personaje.

Una primera idea podría ser utilizar una lista:

```python
# Usando una lista... ¿cuál dato era cuál?
personaje_lista = ["Aragorn", "Guerrero", 85, True]
```

A simple vista parece funcionar, pero presenta un problema importante.

La lista **no describe qué representa cada dato**. Para saber que el `85` corresponde a los puntos de vida y que `True` indica que el personaje está vivo, debemos recordar el orden exacto de los elementos.

| Índice | Dato       | Significado    |
| -----: | ---------- | -------------- |
|      0 | "Aragorn"  | Nombre         |
|      1 | "Guerrero" | Clase          |
|      2 | 85         | Puntos de vida |
|      3 | True       | Está vivo      |

Si en algún momento agregamos un nuevo dato o cambiamos el orden de la lista, todos los índices cambian y el código puede dejar de funcionar.

Aquí es donde los diccionarios muestran su verdadera utilidad.

---

## El superpoder de las etiquetas (Clave - Valor)

En un diccionario no necesitamos recordar posiciones numéricas.

Cada dato se almacena utilizando una **clave** (una etiqueta) que describe claramente qué representa el valor asociado.

De esta manera, en lugar de pensar:

- El dato de la posición `2`

Pensamos:

- La **vida** del personaje.

Esto hace que el código sea mucho más intuitivo y fácil de mantener.

```python
# Usando un diccionario: claridad absoluta
personaje = {
    "nombre": "Aragorn",
    "clase": "Guerrero",
    "vida": 85,
    "esta_vivo": True
}
```

Ahora cada dato tiene un nombre descriptivo:

- `"nombre"` → `"Aragorn"`
- `"clase"` → `"Guerrero"`
- `"vida"` → `85`
- `"esta_vivo"` → `True`

Ya no importa el orden en que estén almacenados los datos. Siempre podremos acceder a ellos utilizando su **clave**, lo que hace que el código sea más legible, más seguro y mucho más sencillo de mantener.

## 4. ¿Cuándo es el momento ideal para usar un diccionario?

Como regla general, piensa en utilizar un **diccionario** siempre que se cumplan estas tres condiciones.

### 1. Estás representando un objeto del mundo real

Los diccionarios son ideales para almacenar información de entidades que poseen diferentes características o propiedades.

Por ejemplo:

- Un automóvil (marca, modelo, año, color).
- Un usuario de una aplicación (nombre, correo, contraseña, edad).
- Un producto (nombre, precio, stock, categoría).
- Un estudiante (nombre, código, promedio, carrera).

Cada propiedad puede convertirse en una **clave** dentro del diccionario.

---

### 2. Los datos son de distintos tipos

En una lista normalmente almacenamos elementos similares.

Por ejemplo:

```python
notas = [4.5, 3.8, 5.0, 4.2]
```

Todos los elementos representan el mismo tipo de información: notas numéricas.

En cambio, un diccionario puede almacenar distintos tipos de datos al mismo tiempo.

```python
producto = {
    "nombre": "Teclado",
    "precio": 120000,
    "disponible": True,
    "colores": ["Negro", "Blanco"]
}
```

Observa que en un mismo diccionario encontramos:

- Texto (`str`)
- Números (`int` o `float`)
- Valores booleanos (`bool`)
- Listas (`list`)

Todo perfectamente organizado mediante claves.

---

### 3. Lo importante es el nombre del dato, no su posición

Con una lista debemos recordar en qué posición se encuentra cada elemento.

Con un diccionario únicamente necesitamos conocer el nombre de la clave.

En otras palabras, no pensamos:

> "Quiero el dato de la posición 2."

Pensamos:

> "Quiero el precio del producto."

Esta forma de trabajar hace que el código sea mucho más fácil de leer y mantener.

---

## Comparación práctica

Observa la diferencia entre acceder a la información utilizando una lista y utilizando un diccionario.

### Utilizando una lista

```python
print(f"El personaje tiene {personaje_lista[2]} puntos de vida.")
```

Al leer el código surge una pregunta inmediata:

**¿Qué representa el índice `2`?**

Para responderla debemos revisar cómo fue construida la lista.

---

### Utilizando un diccionario

```python
print(f"El personaje tiene {personaje['vida']} puntos de vida.")
```

Ahora el código prácticamente se explica por sí solo.

La clave `"vida"` deja claro qué información estamos obteniendo.

---

Las **listas** son ideales cuando únicamente necesitamos almacenar una colección de elementos ordenados.

Los **diccionarios** son la mejor opción cuando queremos representar objetos del mundo real con diferentes características identificadas por un nombre.

Una forma sencilla de recordarlo es la siguiente:

- **Lista:** una fila de datos donde importa la posición.
- **Diccionario:** un formulario donde cada dato tiene una etiqueta.


## Minireto en clase: **Ficha de Personaje**

Es momento de practicar la creación y modificación de diccionarios.

### Instrucciones

Realiza las siguientes actividades de forma individual.

1. Crea un diccionario llamado `personaje` que represente a un guerrero de un videojuego.

   El diccionario debe contener las siguientes claves:

   - `nombre`
   - `clase`
   - `vida`

   **Ejemplo de valores:**

   - Nombre: cualquier nombre que desees.
   - Clase: `"Mago"`, `"Guerrero"`, `"Arquero"`, etc.
   - Vida: un número entero, por ejemplo `100`.

2. El personaje sube de nivel.

   Modifica el valor de la clave `vida` para que ahora sea `120`.

3. El personaje encuentra un objeto.

   Agrega una nueva clave llamada `arma` cuyo valor sea `"Bastón de Fuego"`.

4. Imprime el diccionario completo para comprobar que todos los cambios se realizaron correctamente.

---
## Ejercicio de práctica
```python
# 📝 COPIA ESTE DICCIONARIO INICIAL EN TU EDITOR:
personaje_reto = {
    "nombre": "Ragnar",
    "clase": "Guerrero",
    "vida": 150,
    "habilidades": ["Golpe Heroico", "Torbellino"],
    "oro": 50
}

# === TU MISIÓN ===
# 1. El guerrero visita al maestro de armas y aprende una nueva habilidad: "Grito de Guerra".
#    Agrégala al final de su lista de habilidades usando .append().
#
# 2. Un monstruo lo ataca por sorpresa. Muestra en pantalla el segundo ataque 
#    de su lista de habilidades (índice 1) con el formato: "⚔️ Ragnar usa: [Habilidad]".
#
# 3. Imprime el diccionario completo modificado para verificar los cambios.
```

## Reto final
### Actualizador de precios
```python
# 📝 DICCIONARIO INICIAL:
carrito_compras = {
    "Laptop": 800,
    "Mouse": 25,
    "Monitor": 250,
    "Teclado": 45
}

# === MISIÓN ===
# 1. La tienda tiene un error de inflación. Usa un ciclo 'for' con el método .items() 
#    para recorrer el carrito de compras.
#
# 2. Dentro del ciclo, imprime un mensaje para cada producto que diga:
#    "El artículo [Nombre] cuesta $[Precio]".
#
# 3. HACKER CHALLENGE (Opcional): El cliente intenta buscar si en su carrito 
#    tiene un artículo llamado "Tarjeta Gráfica". Usa el método .get() para buscarlo. 
#    Si no existe, muestra el mensaje: "❌ Tarjeta Gráfica no está en el carrito".
```