class Estudiante:
    def __init__(self, codigo, nombre):
        self.codigo = codigo
        self.nombre = nombre
    
    def __eq__(self, value):
        if self.codigo == value.codigo:
            return True
        return False


def buscar(objetivo, lista):
    posicion = -1
    for elemento in lista:
        posicion+=1
        if elemento == objetivo:
            return posicion
            
    
    return -1

objetivo = Estudiante(3, "Pedro")

e1 = Estudiante(1, "Ana")
e2 = Estudiante(2, "Juan")
e3 = Estudiante(3, "Maria")
e4 = Estudiante(4, "Francisco")

estudiantes = [e1, e2, e3, e4]

resultado = buscar(objetivo, estudiantes)
if resultado > -1:
    print(f"El estudiante con código {objetivo.codigo} existe en la posición {resultado}")
else:
    estudiantes.append(objetivo)
    print("Estudiante agregado exitosamente!")

