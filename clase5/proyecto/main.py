from sensor import Sensor

sensor = Sensor(
    "A-102",
    31,
    56,
    560
)

while True:
    menu =   """
    ========= SENSOR AMBIENTAL =========

    1. Ver lectura del sensor
    2. Ver resumen del sensor
    3. Ver estado de alertas
    4. Salir
        """
    print(menu)
    opcion = input("Seleccione una opcion: ")
    if opcion == "1":
        lectura = sensor.obtener_lectura()
        print("===Lectura del sensor===")
        print(f"Temperatura: {lectura[0]}")
        print(f"Humedad: {lectura[1]}")
        print(f"CO2: {lectura[2]}")
    
    elif opcion == "2":
        lectura = sensor.obtener_resumen()
        print("===resumen del sensor===")
        print(f"Código: {lectura[0]}")
        print(f"Temperatura: {lectura[1]}")
        print(f"Humedad: {lectura[2]}")
        print(f"CO2: {lectura[3]}")

    elif opcion == "3":
        lectura = sensor.obtener_estado()
        print("====Estado del sensor====")
        if lectura[0]:
            print("Temperatura Alta")
        else:
            print("Temperatura estable")
        
        if lectura[1]:
            print("Humedad Baja")
        else:
            print("Humedad Alta")
        
        if lectura[2]:
            print("CO2 Alto")
        else:
            print("CO2 Bajo")
    elif opcion == "4":
        print("\nHasta luego...")
        break

    else:
        print("Elija una opcion válida")