from paquete_robots.Robot.robot import Robot
from paquete_robots.Enumeraciones.enumeraciones import *

# Robot behaviour for transporting objects class
class RobotTransportador(Robot):

    capacidadMaxCarga = 0
    pesoCargado = 0
    pesoDisponible = 0

    def __init__(self,id,mi_estado_robot,mi_nivel_bateria,coordenadaX,coordenadaY,capacidadMaxCarga,pesoCargado,pesoDisponible):
        Robot.__init__(self,id,mi_estado_robot,mi_nivel_bateria,coordenadaX,coordenadaY)
        self.capacidadMaxCarga = capacidadMaxCarga
        self.pesoCargado = pesoCargado
        self.pesoDisponible = pesoDisponible

    def __str__(self):
        return " id: {}, estado del robot: {}, nivel de bateria: {}, X: {}, Y: {}, Capacidad máxima de carga: {}, Peso cargado: {}, Peso disponible: {}".format(str(self.id),str(self.mi_estado_robot.name),str(self.mi_nivel_bateria.name),str(self.coordenadaX),str(self.coordenadaY),str(self.capacidadMaxCarga),str(self.pesoCargado),str(self.pesoDisponible))


    def cogerCarga(self, carga):
        if self.capacidadMaxCarga >= (carga.peso + self.pesoCargado):
            print("agarro la carga ".format(carga.nombre))
            self.pesoCargado += carga.peso
        else:
            print("Lo siento, excese el peso máximo de carga.")


    def soltarCarga(self, carga):
        if self.pesoCargado >= carga.peso:
            print("suelto la carga".format(carga.nombre))
            self.pesoCargado -= carga.peso
        else:
            print("lo siento, esto no se puede realizar.")


    def transportarCarga(self,carga,x,y):
        print("transporto la carga a x: {}, y: {}".format(x,y))
        carga.coordenadaX = x
        carga.coordenadaY = y

# ----------------- /class