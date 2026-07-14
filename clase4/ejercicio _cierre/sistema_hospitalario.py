# aqui se administr la colección de pacientes
from paciente import Paciente

class SistemaHospitalario:
    
    def __init__(self):
        self.pacientes = set()
    
    def registrar_paciente(self, historia, nombre, edad):
        paciente = Paciente(historia, nombre, edad)

        #esta es la cantidad de pacientes antes de agregar el nuevo
        cantidad_antes = len(self.pacientes)

        # aquí agregamos el nuevo paciente
        self.pacientes.add(paciente)

        if len(self.pacientes) > cantidad_antes:
            print("\n Paciente registrado exitosamente")
        else:
            print("\nYa existe un paciente con esa historia clinica")


    def listar_pacientes(self):
        if len(self.pacientes) == 0:
            print("\nNo hay pacientes registrados")
            return
        
        print("\n====PACIENTES REGISTRADOS====")

        for paciente in self.pacientes:
            print(paciente)
            print("---------------------")