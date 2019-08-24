from datetime import datetime
class Modelo_Incidencia:
    def __init__(self, operador,puesto,administrador,camara,turno,incidente,descripcion,area):
        self.operador=operador
        self.puesto=puesto
        self.administrador=administrador
        self.camara=camara
        self.turno=turno
        self.incidente=incidente
        self.descripcion=descripcion
        self.area=area
        self.fecha=datetime.now().strftime("%d/%m/%Y %H:%M:%S")