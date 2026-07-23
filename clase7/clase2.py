class Estudiante:
    def __init__(self, nombre, edad, promedio):
        self.nombre = nombre
        self.edad = edad
        self.promedio = promedio


estudiantes = [
    {"nombre": "Juan", "edad": 20, "promedio": 8.5},
    {"nombre": "María", "edad": 22, "promedio": 9.2},
    {"nombre": "Pedro", "edad": 19, "promedio": 7.8},
    {"nombre": "Ana", "edad": 21, "promedio": 9.0},
    {"nombre": "Luis", "edad": 23, "promedio": 8.0},
    {"nombre": "Sofía", "edad": 20, "promedio": 9.5},
    {"nombre": "Carlos", "edad": 22, "promedio": 7.5},
    {"nombre": "Laura", "edad": 19, "promedio": 8.8},
    {"nombre": "Diego", "edad": 21, "promedio": 9.1},
    {"nombre": "Valentina", "edad": 23, "promedio": 8.3},
    {"nombre": "Andrés", "edad": 20, "promedio": 7.9},
    {"nombre": "Camila", "edad": 22, "promedio": 9.4},
    {"nombre": "Javier", "edad": 19, "promedio": 8.2},
    {"nombre": "Isabella", "edad": 21, "promedio": 9.3},
    {"nombre": "Sebastián", "edad": 23, "promedio": 7.7},
    {"nombre": "Gabriela", "edad": 20, "promedio": 8.6},
    {"nombre": "Mateo", "edad": 22, "promedio": 9.0},
    {"nombre": "Daniela", "edad": 19, "promedio": 8.1},
    {"nombre": "Alejandro", "edad": 21, "promedio": 9.2},
    {"nombre": "Natalia", "edad": 23, "promedio": 7.6}
]

def mostrar_estudiantes(lista):
    print("\n-------------------------------------------")
    print(f'{"Nombre":<15} {"Edad":<8} {"Promedio"}')
    print("---------------------------------------------")
    for estudiante in lista:
        print(f'{estudiante["nombre"]:<15} {estudiante["edad"]:<8} {estudiante["promedio"]}')

    print("----------------------------------------------")

mostrar_estudiantes(estudiantes)


while True:
    print("\n===============Menu===============")
    print("1. Mostrar estudiantes")
    print("2. Ordenaar por nombre")
    print("3. Ordenar por edad")
    print("4. Ordenar por promedio")
    print("5. Mostrar mejores 3 promedios") #investigar como de una lista dada, imprimir solo los 3 primeros elementos
    print("6. Salir")

    opcion = input("\nSeleccione la opcion: ")
    if opcion == "1":
        mostrar_estudiantes(estudiantes)

    elif opcion == "2":
        resultado = sorted(
            estudiantes,
            key=lambda estudiante: estudiante["nombre"]
        )
        mostrar_estudiantes(resultado)

    elif opcion =="3":
        resultado = sorted(
            estudiantes,
            key=lambda estudiante: estudiante["edad"]
        )
        mostrar_estudiantes(resultado)
    elif opcion == "6":
        print("saliendo...")
        break
