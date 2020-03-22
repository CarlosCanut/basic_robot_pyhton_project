from paquete_robots.RobotTransportador.robotTransportador import RobotTransportador
from paquete_robots.RobotVigilador.robotVigilador import RobotVigilador
from paquete_robots.Enumeraciones.enumeraciones import *

# Robot behaviour for driving class
class RobotCirculador(RobotTransportador,RobotVigilador):

    arrancado = False

    def __init__(self, id, mi_estado_robot, mi_nivel_bateria, coordenadaX, coordenadaY, capacidadMaxCarga, pesoCargado, pesoDisponible, mi_modo_vision,arrancado):
        RobotTransportador.__init__(self,id,mi_estado_robot,mi_nivel_bateria,coordenadaX,coordenadaY,capacidadMaxCarga,pesoCargado,pesoDisponible)
        RobotVigilador.__init__(self,id,mi_estado_robot,mi_nivel_bateria,coordenadaX,coordenadaY,mi_modo_vision)
        #super().__init__(id, estado_robot, nivel_bateria, coordenadaX, coordenadaY, capacidadMaxCarga, pesoCargado, pesoDisponible)
        #super().__init__(id, estado_robot, nivel_bateria, coordenadaX, coordenadaY, modo_vision)
        self.arrancado = arrancado

    def __str__(self):
        return " id: {}, estado del robot: {}, nivel de bateria: {}, X: {}, Y: {}, Capacidad máxima de carga: {}, Peso cargado: {}, Peso disponible: {}, Modo vision: {}, arrancado: {}.".format(str(self.id),str(self.mi_estado_robot.name),str(self.mi_nivel_bateria.name),str(self.coordenadaX),str(self.coordenadaY),str(self.capacidadMaxCarga),str(self.pesoCargado),str(self.pesoDisponible),str(self.mi_modo_vision.name),str(self.arrancado))


    def arrancar(self):
        print("Arrancar")
        self.arrancado = True

    def apagar(self):
        print("Apagar")
        self.arrancado = False
# --------------- /class