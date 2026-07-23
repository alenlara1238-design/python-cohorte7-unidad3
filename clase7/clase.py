class Estudiante:
    def __init__(self, nombre, promedio):
        self.nombre = nombre
        self.promedio = promedio



estudiantes = [
    Estudiante("Ana", 4.5),
    Estudiante("Pedro", 3.2),
    Estudiante("Luis", 4.9)
]

estudiantes_ordenados = sorted(
    estudiantes,
    key = lambda estudiante: estudiante.promedio,
    reverse=True
)

for estudiante in estudiantes_ordenados:
    print(f"{estudiante.nombre}: {estudiante.promedio}")
    