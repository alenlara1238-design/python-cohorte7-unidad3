from sistema_hospitalario import SistemaHospitalario

sistema = SistemaHospitalario()

while True:
    print("=======SISTEMA HOSPITALARIO======")
    print("1. Registrar pacinete")
    print("2. Listar pacientes")
    print("3 Salir")

    opcion = input("seleccione una opcion:")

    if opcion == "1":
        historia = input("Historia clinica: ")
        nombre = input("nombre: ")
        edad = int(input("Edad: "))

        sistema.registrar_paciente(historia, nombre, edad)

    elif opcion == "2":
        sistema.listar_pacientes()
    
    elif opcion == "3":
        print("Hasta pronto...")
        break

    else: 
        print("\n opcion no valida")