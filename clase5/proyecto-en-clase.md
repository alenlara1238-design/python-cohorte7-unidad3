# Proyecto: Sistema de Monitoreo de Sensores Ambientales

## Contexto

Una empresa ha instalado sensores ambientales en una planta de producción para monitorear constantemente las condiciones del entorno. Cada sensor realiza una medición que incluye tres datos fundamentales:

- Temperatura (°C)
- Humedad (%)
- Nivel de dióxido de carbono (CO₂ en ppm)

Cada medición representa una lectura única realizada en un instante específico. Una vez obtenida, esa información no debe modificarse, ya que corresponde a un registro de la realidad en un momento determinado.

Para representar este tipo de información utilizarás **tuplas**, ya que son estructuras de datos inmutables ideales para almacenar conjuntos de valores que pertenecen a una misma entidad y no deben cambiar.

---

## Estructura del proyecto

El proyecto estará compuesto por dos archivos:

- `Sensor.py`
- `main.py`

---

## Clase `Sensor`

La clase debe almacenar la siguiente información:

- Código del sensor
- Temperatura
- Humedad
- Nivel de CO₂

Estos datos serán recibidos mediante el constructor.

---

## Funcionalidades

La clase deberá implementar los siguientes métodos:

### 1. `obtener_lectura()`

Debe devolver una **tupla** con la siguiente información:

- Temperatura
- Humedad
- CO₂

---

### 2. `obtener_resumen()`

Debe devolver una **tupla** con toda la información del sensor en el siguiente orden:

- Código
- Temperatura
- Humedad
- CO₂

---

### 3. `obtener_estado()`

Debe analizar los valores registrados y devolver una **tupla** de valores booleanos indicando si existen alertas.

Las reglas son las siguientes:

- Temperatura alta cuando sea mayor a **35 °C**.
- Humedad baja cuando sea menor a **40 %**.
- CO₂ alto cuando sea mayor a **900 ppm**.

Cada posición de la tupla debe representar el estado de una de estas condiciones.

---

## Interfaz de usuario

El programa principal deberá mostrar un menú como el siguiente:

```text
========= SENSOR AMBIENTAL =========

1. Ver lectura del sensor
2. Ver resumen del sensor
3. Ver estado de alertas
4. Salir
```

Según la opción elegida por el usuario, el programa deberá invocar el método correspondiente de la clase `Sensor` y mostrar la información de manera clara y organizada.

---

## Restricciones

Para este proyecto **no está permitido**:

- Utilizar listas.
- Utilizar diccionarios.
- Modificar una tupla después de haber sido creada.
- Devolver listas desde los métodos de la clase.

---

## Recomendaciones

Durante el desarrollo intenta aprovechar las características propias de las tuplas:

- Acceder a sus elementos mediante índices.
- Desempaquetar las tuplas para obtener sus valores en variables independientes.
- Comprender por qué una tupla es la estructura adecuada para representar una lectura fija de un sensor.

---

## Al finalizar el proyecto deberías ser capaz de responder

1. ¿Por qué una lectura de un sensor se representa mejor con una tupla que con una lista?
2. ¿Qué ventajas ofrece la inmutabilidad de las tuplas en este contexto?
3. ¿En qué situaciones reales de la programación volverías a utilizar una tupla?