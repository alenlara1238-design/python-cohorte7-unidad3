cursos = (
    "Python",
    "Java",
    "Javacript",
    "SQL",
    "git"
)

respuesta = input("Qué curso desea buscar?: ")

if respuesta in cursos:
    print("El curso está disponible.")
else:
    print("El curso no existe.")

    