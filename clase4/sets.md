# SETS: Gestionar datos sin duplicados

> ## Objetivo de la clase
>
> En esta clase aprenderemos qué son los **Sets (Conjuntos)** en Python, qué problema resuelven y por qué son una estructura de datos fundamental cuando necesitamos **almacenar únicamente elementos únicos**, evitando información repetida.

---

# ¿Por qué existen los Sets?

En el desarrollo de software es muy común trabajar con **grandes cantidades de información**.

Imagina que tu aplicación recibe **miles o incluso millones de registros**.

¿Qué ocurriría si un mismo dato aparece varias veces?

Los datos duplicados pueden provocar:

- ❌ Resultados incorrectos.
- ❌ Mayor consumo de memoria.
- ❌ Procesamientos innecesarios.
- ❌ Errores de lógica en la aplicación.

> **Los Sets fueron creados precisamente para resolver este problema.**

---

# ¿Qué problema resuelven los Sets?

Supongamos que organizas un **evento de tecnología**.

Durante el día, las personas se registran mediante un formulario web y obtienes la siguiente lista de correos electrónicos:

```text
juan@gmail.com
ana@gmail.com
carlos@gmail.com
juan@gmail.com
pedro@gmail.com
ana@gmail.com
```

Observa que algunos participantes enviaron el formulario más de una vez.

Si deseas enviar un correo de confirmación, **no quieres enviar dos mensajes a la misma persona**.

>  **Necesitas conservar únicamente los registros únicos.**

Ese es uno de los principales problemas que resuelven los **Sets**.

---

# Casos reales donde se utilizan los Sets

## Registro de usuarios

Cuando una persona crea una cuenta, el sistema debe garantizar que el correo electrónico **no exista previamente**.

```text
usuario1@gmail.com
usuario2@gmail.com
usuario3@gmail.com
usuario1@gmail.com
```

>  El último registro debe rechazarse porque **ya existe**.

Los **Sets** permiten detectar rápidamente estos duplicados.

---

##  Sistema de acceso a edificios

Una empresa registra las tarjetas utilizadas para ingresar durante el día.

```text
A102
B305
A102
C210
B305
```

Aunque una persona entre varias veces, si el objetivo es conocer **qué empleados ingresaron hoy**, basta con almacenar **cada tarjeta una sola vez**.

---

##  Seguidores en una red social

Imagina una plataforma como Instagram.

Aunque un usuario presione varias veces el botón **"Seguir"**, únicamente debe aparecer **una vez** en la lista de seguidores.

> Los **Sets** garantizan automáticamente que no existan seguidores duplicados.

---

##  Catálogo de productos

Una tienda recibe productos provenientes de diferentes proveedores.

```text
Mouse
Teclado
Monitor
Mouse
Impresora
Monitor
```

Si únicamente deseas conocer **qué productos existen**, no tiene sentido almacenar nombres repetidos.

---

##  Videojuegos

En un videojuego el jugador puede desbloquear logros.

```text
Explorador
Cazador
Explorador
Constructor
```

Aunque el jugador obtenga nuevamente el mismo logro, este **solo debe almacenarse una vez**.

---

##  Plataformas de Streaming

Servicios como **Netflix**, **Spotify** o **YouTube** registran las categorías vistas por un usuario.

```text
Acción
Comedia
Acción
Drama
Drama
```

Si únicamente interesa conocer **qué géneros ha visto el usuario**, no es necesario guardar categorías repetidas.

---

## Motores de búsqueda

Los motores de búsqueda procesan millones de páginas web diariamente.

Durante ese proceso necesitan evitar almacenar **referencias duplicadas** al mismo recurso.

> Los **Sets** permiten identificar rápidamente elementos únicos mientras se procesan enormes cantidades de información.

---

##  Sistemas de Ciberseguridad

Un firewall puede registrar miles de direcciones IP sospechosas.

```text
192.168.10.4
10.0.0.5
192.168.10.4
172.20.1.8
10.0.0.5
```

El sistema solo necesita conservar **una copia de cada dirección IP** para construir una lista de bloqueo eficiente.

---

# ¿Por qué no usar simplemente una lista?

Una **lista** permite almacenar elementos repetidos.

```text
Python
Java
Python
Java
C#
Python
```

Y eso **no siempre es un problema**.

Existen muchos escenarios donde los datos repetidos son completamente válidos.

Por ejemplo:

-  Las notas obtenidas por un estudiante.
-  Las ventas realizadas durante el día.
-  Las temperaturas registradas cada hora.

En todos estos casos **tiene sentido que un valor aparezca varias veces**.

---

# Entonces... ¿Cuándo debo usar un Set?

> ✅ Cuando el objetivo sea representar una colección de **elementos únicos**.

A diferencia de una lista, un **Set** garantiza que:

- Cada elemento solo puede existir **una vez**.
- No importa cuántas veces intentes agregar el mismo valor.
- Los elementos duplicados **se eliminan automáticamente**.

# Operaciones básicas con Sets en Python

Ahora que conocemos **qué son los Sets** y **qué problema resuelven**, es momento de aprender a utilizarlos en Python.

---

# Crear un Set

Para crear un **Set** utilizamos **llaves (`{}`)**.

```python
cursos = {
    "Python",
    "Java",
    "JavaScript"
}

print(cursos)
```

**Posible salida**

```text
{'JavaScript', 'Python', 'Java'}
```

> **Importante**
>
> El orden de los elementos puede cambiar cada vez que ejecutes el programa.
>
> Los **Sets no mantienen un orden específico**.

---

# Agregar nuevos elementos

Para agregar un elemento utilizamos el método **`add()`**.

## Sintaxis

```python
set.add(elemento)
```

## Ejemplo

```python
cursos = {
    "Python",
    "Java"
}

cursos.add("Angular")

print(cursos)
```

**Posible salida**

```text
{'Angular', 'Java', 'Python'}
```

Ahora el conjunto contiene **tres cursos**.

---

# ¿Qué ocurre si agregamos un elemento repetido?

Supongamos que un usuario intenta registrar nuevamente el curso **Python**.

```python
cursos = {
    "Python",
    "Java"
}

cursos.add("Python")

print(cursos)
```

**Salida**

```text
{'Python', 'Java'}
```

Observa que **Python no aparece dos veces**.

Python simplemente **ignora el nuevo registro** porque ese elemento ya existe en el conjunto.

---

# Ejemplo del mundo real

Supongamos que una aplicación almacena los correos electrónicos registrados.

```python
correos = {
    "ana@gmail.com",
    "juan@gmail.com"
}

correos.add("ana@gmail.com")

print(correos)
```

**Resultado**

```text
{
    'juan@gmail.com',
    'ana@gmail.com'
}
```

Aunque el usuario intentó registrarse nuevamente, el conjunto sigue almacenando **un único correo electrónico**.

---

# Eliminar elementos

Para eliminar un elemento utilizamos el método **`remove()`**.

## Sintaxis

```python
set.remove(elemento)
```

## Ejemplo

```python
cursos = {
    "Python",
    "Java",
    "Angular"
}

cursos.remove("Java")

print(cursos)
```

**Salida**

```text
{'Angular', 'Python'}
```

El curso **Java** fue eliminado correctamente.

---

# ¿Qué ocurre si el elemento no existe?

```python
cursos = {
    "Python",
    "Java"
}

cursos.remove("C++")
```

**Resultado**

```text
KeyError
```

Python genera un error porque intenta eliminar un elemento que **no existe** en el conjunto.

> **Atención**
>
> El método **`remove()`** produce un **`KeyError`** cuando el elemento no está presente.

---

# Una alternativa más segura: `discard()`

Existe otro método llamado **`discard()`**.

```python
cursos = {
    "Python",
    "Java"
}

cursos.discard("C++")

print(cursos)
```

**Salida**

```text
{'Python', 'Java'}
```

En este caso **no ocurre ningún error**.

> **Buena práctica**
>
> En muchos programas reales se prefiere utilizar **`discard()`** cuando no se tiene la certeza de que el elemento esté presente en el conjunto.

---

# Verificar si un elemento existe

Una de las operaciones más rápidas de un **Set** consiste en comprobar si un elemento pertenece al conjunto.

Para ello utilizamos el operador **`in`**.

## Ejemplo

```python
cursos = {
    "Python",
    "Java",
    "Angular"
}

print("Python" in cursos)
```

**Salida**

```text
True
```

Otro ejemplo:

```python
print("C++" in cursos)
```

**Salida**

```text
False
```

> **Importante**
>
> La búsqueda de elementos en un **Set** es muy eficiente, razón por la cual esta estructura es ampliamente utilizada en aplicaciones reales.

---

# Ejemplo del mundo real

Antes de registrar un nuevo correo electrónico podemos comprobar si ya existe.

```python
correos = {
    "ana@gmail.com",
    "juan@gmail.com"
}

correo = "ana@gmail.com"

if correo in correos:
    print("Este correo ya está registrado.")
else:
    correos.add(correo)
```

**Salida**

```text
Este correo ya está registrado.
```

Esta operación es muy común en:

- Sistemas de autenticación.
- Plataformas web.
- Bases de datos.
- Sistemas de registro de usuarios.

---

# Recorrer un Set

Al igual que las listas, un **Set** puede recorrerse mediante un ciclo **`for`**.

## Ejemplo

```python
cursos = {
    "Python",
    "Java",
    "Angular"
}

for curso in cursos:
    print(curso)
```

**Posible salida**

```text
Java
Angular
Python
```

Sin embargo, en otra ejecución podrías obtener:

```text
Python
Java
Angular
```

o incluso:

```text
Angular
Python
Java
```

---

# ¿Por qué cambia el orden?

> **Importante**
>
> Los **Sets no almacenan sus elementos en un orden fijo**.
>
> Por esta razón, el orden de impresión puede variar entre diferentes ejecuciones del programa.

---

# ¿Cuándo no conviene utilizar un Set?

Si tu aplicación necesita:

- Mantener el orden en que se agregan los elementos.
- Acceder a un elemento mediante una posición (`[0]`, `[1]`, etc.).
- Permitir valores repetidos.

Entonces una **lista (`list`)** será una mejor alternativa.

---

# Resumen de las operaciones aprendidas

| Operación | Método | Descripción |
|-----------|---------|-------------|
| Crear un Set | `{}` | Crea un conjunto de elementos únicos. |
| Agregar | `add()` | Inserta un nuevo elemento si no existe. |
| Eliminar | `remove()` | Elimina un elemento. Produce error si no existe. |
| Eliminar de forma segura | `discard()` | Elimina un elemento sin generar error si no existe. |
| Verificar existencia | `in` | Comprueba si un elemento pertenece al conjunto. |
| Recorrer | `for` | Permite iterar sobre todos los elementos del Set. |

---

