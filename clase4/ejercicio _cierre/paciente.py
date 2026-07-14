# aqui definimos el objeto que representa a un paciente

class Paciente:
    def __init__(self, historia_clinica, nombre, edad):
        self.historia_clinica = historia_clinica
        self.nombre = nombre
        self.edad = edad
    
    def __str__(self):
        return (
            f"Historia Clínica: {self.historia_clinica} |"
            f"Nombre: {self.nombre} |"
            f"Edad: {self.edad}"
        )

    def __eq__(self, otro):
        return self.historia_clinica == otro.historia_clinica

    def __hash__(self):
        return hash(self.historia_clinica)