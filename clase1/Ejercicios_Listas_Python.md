# Ejercicios de Listas en Python

## 🟢 Nivel 1: Calentamiento (Operaciones Básicas)

### Ejercicio 1: El nuevo seguidor

``` python
seguidores = ["@carlos_dev", "@maria.code", "@ale_jandro"]
```

**Misión:** Alguien llamado `@luna_azul` acaba de darle al botón
**Seguir**. Escribe el código para añadirla al final de la lista e
imprime el resultado.

### Ejercicio 2: El post patrocinado

``` python
feed = ["foto_mascota", "meme_python", "video_viaje"]
```

**Misión:** Inserta `"PUBLICIDAD_CURSO"` en el índice 1.

## 🟡 Nivel 2: Modificación y Navegación

### Ejercicio 3

``` python
amigos = ["Ana", "Pedro", "Luiss", "Elena"]
```

Cambia `"Luiss"` por `"Luis"` usando únicamente su índice.

### Ejercicio 4

``` python
notificaciones = ["like", "comentario", "compartir", "mencion", "follow"]
```

Guarda la última notificación en `ultima_alerta` usando índices
negativos e imprímela.

## 🟠 Nivel 3: Ciclo for

### Ejercicio 5

``` python
likes_por_foto = [45,120,8,300,52]
```

Imprime: `Esta publicación recibió X likes`.

### Ejercicio 6

``` python
feed_usuario = ["foto_bici","LINK_ESTAFA","video_comedia","LINK_ESTAFA"]
```

Si el elemento es `"LINK_ESTAFA"` imprime `⚠️ Contenido bloqueado`; de
lo contrario imprime `Mostrando: [post]`.

Guía: 1. `for post in feed_usuario:` 2. `if post == "LINK_ESTAFA":` 3.
Completa el `else`.

## 🔴 Nivel 4: Integración

``` python
cola_reproduccion = ["Song A","Song B","Song C"]
```

1.  Agrega `"Song D"` al final.
2.  Inserta `"Firts Song"` al inicio.
3.  Elimina la primera canción con `.pop(0)`.
4.  Muestra `len()` y luego imprime cada canción con:

`Siguiente en fila: [Nombre de la canción]`

Guía: - `.append("Song D")` - `.insert(0,"Firts Song")` - `.pop(0)` -
`for cancion in cola_reproduccion:`
