class Sensor:
    def __init__(self, codigo, temp, humedad, co2):
        self.codigo = codigo
        self.temperatura = temp
        self.humedad = humedad
        self.co2 = co2
    
    def obtener_lectura(self):
        return (
            self.temperatura,
            self.humedad,
            self.co2
        )

    def obtener_resumen(self):
        return (
            self.codigo,
            self.temperatura,
            self.humedad,
            self.co2
        )
    
    def obtener_estado(self):
        temperatura_alta = self.temperatura > 35
        humedad_baja = self.humedad < 40
        co2_alto = self.co2 > 900

        return (
            temperatura_alta,
            humedad_baja,
            co2_alto
        )
