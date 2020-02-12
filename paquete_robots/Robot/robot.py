from paquete_robots.Enumeraciones.enumeraciones import *

# Robot class
class Robot:
    
    id = ""
    estado_robot.ENCENDIDO
    nivel_bateria.APAGADO
    modo_vision.DIURNA
    coordenadaX = 0
    coordenadaY = 0

    def __init__(self,id,estado_robot,nivel_bateria,coordenadaX,coordenadaY):
        self.id = id
        self.estado_robot = estado_robot
        self.nivel_bateria = nivel_bateria
        self.coordenadaX = coordenadaX
        self.coordenadaY = coordenadaY
        print("EL ROBOT ESTA VIVOOO!!!!")
    
    def encender(self):
        self.estado_robot.ENCENDIDO

    
    def apagar(self):
        self.estado_robot.APAGADO
# ------------- /Robot class