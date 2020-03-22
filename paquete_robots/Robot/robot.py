from paquete_robots.Enumeraciones.enumeraciones import *

# Robot class
class Robot:
    
    id = ""
    mi_estado_robot = estado_robot.APAGADO
    mi_nivel_bateria = nivel_bateria.ALTO
    mi_modo_vision = modo_vision.DIURNA
    coordenadaX = 0
    coordenadaY = 0

    def __init__(self,id,mi_estado_robot,mi_nivel_bateria,coordenadaX,coordenadaY):
        self.id = id
        self.mi_estado_robot = mi_estado_robot
        self.mi_nivel_bateria = mi_nivel_bateria
        self.coordenadaX = coordenadaX
        self.coordenadaY = coordenadaY
    
    def __str__(self):
        return "id: {}, estado del robot: {}, nivel de bateria: {}, X: {}, Y: {}".format(str(self.id),str(self.mi_estado_robot.name),str(self.mi_nivel_bateria.name),str(self.coordenadaX),str(self.coordenadaY))
    
    def encender(self):
        self.mi_estado_robot = estado_robot.ENCENDIDO

    
    def apagar(self):
        self.mi_estado_robot = estado_robot.APAGADO
# ------------- /Robot class