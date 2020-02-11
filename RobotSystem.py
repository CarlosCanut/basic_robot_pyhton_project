# ------------------------------------------------
# RobotSystem.py
# Description: Project for testing heredity with python
# Author: Carlos Canut
# ------------------------------------------------

# State of the robot
class estado_robot():
    ENCENDIDO = 1
    APAGADO = 2

# vision mode
class modo_vision():
    NOCTURNA = 1
    DIURNA = 2

# Battery level
class nivel_bateria():
    AGOTADO = 1
    BAJO = 2
    MEDIO = 3
    ALTO = 4
    APAGADO = 5


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





