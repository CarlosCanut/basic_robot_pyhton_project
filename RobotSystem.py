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


# Robot behaviour for watching over class
class RobotVigilador(Robot):

    modo_vision.NOCTURNA

    def cambiarModoVision(self):
        if modo_vision.NOCTURNA:
            modo_vision.DIURNA
        else:
            modo_vision.NOCTURNA
# ----------------- /class



# Robot behaviour for transporting objects class
class RobotTransportador(Robot):

    capacidadMaxCarga = ""

    def __init__(self,id,estado_robot,nivel_bateria,coordenadaX,coordenadaY,capacidadMaxCarga):
        super().__init__(id,estado_robot,nivel_bateria,coordenadaX,coordenadaY)
        self.capacidadMaxCarga = capacidadMaxCarga

    # TO-DO: Make use of the Carga class for the methods

    def cogerCarga(self):
        print("agarro una carga")

    def soltarCarga(self):
        print("suelto una carga")

    def avanzar(self):
        print("Avanzo")

    def transportarCarga(self,x,y):
        print("transporto una carga a x: {}, y: {}".format(x,y))
# ----------------- /class


# Robot behaviour for flying class
class RobotVolador(RobotTransportador,RobotVigilador):

    def aterrizar(self):
        print("Aterrizo")

    def despegar(self):
        print("Despegar")
# ---------------- /class



# Robot behaviour for driving class
class RobotCirculador(RobotTransportador,RobotVigilador):

    def arrancar(self):
        print("Arrancar")
        estado_robot.ENCENDIDO

    def apagar(self):
        print("Apagar")
        estado_robot.APAGADO
# --------------- /class
