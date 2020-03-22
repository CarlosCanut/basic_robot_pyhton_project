from paquete_robots.RobotTransportador.robotTransportador import RobotTransportador
from paquete_robots.Enumeraciones.enumeraciones import *

# Robot behaviour for flying class
class RobotVolador(RobotTransportador):

    aterrizado = False

    def __init__(self, id, mi_estado_robot, mi_nivel_bateria, coordenadaX, coordenadaY, capacidadMaxCarga, pesoCargado, pesoDisponible, aterrizado):
        RobotTransportador.__init__(self,id, mi_estado_robot, mi_nivel_bateria, coordenadaX, coordenadaY, capacidadMaxCarga, pesoCargado, pesoDisponible)
        self.aterrizado = aterrizado

    def __str__(self):
        return " id: {}, estado del robot: {}, nivel de bateria: {}, X: {}, Y: {}, Capacidad máxima de carga: {}, Peso cargado: {}, Peso disponible: {}, Aterrizado: {}".format(str(self.id),str(self.mi_estado_robot.name),str(self.mi_nivel_bateria.name),str(self.coordenadaX),str(self.coordenadaY),str(self.capacidadMaxCarga),str(self.pesoCargado),str(self.pesoDisponible),str(self.aterrizado))


    def aterrizar(self):
        print("Aterrizo")
        self.aterrizado = True

    def despegar(self):
        print("Despegar")
        self.aterrizado = False
# ---------------- /class
