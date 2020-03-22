from paquete_robots.Robot.robot import Robot
from paquete_robots.Enumeraciones.enumeraciones import *

# Robot behaviour for watching over class
class RobotVigilador(Robot):

    mi_modo_vision = modo_vision.DIURNA

    def __init__(self, id, mi_estado_robot, mi_nivel_bateria, coordenadaX, coordenadaY, mi_modo_vision):
        Robot.__init__(self,id, mi_estado_robot, mi_nivel_bateria, coordenadaX, coordenadaY)
        self.mi_modo_vision = mi_modo_vision
    
    def __str__(self):
        return " id: {}, estado del robot: {}, nivel de bateria: {}, X: {}, Y: {}, Modo de visión: {}".format(str(self.id),str(self.mi_estado_robot.name),str(self.mi_nivel_bateria.name),str(self.coordenadaX),str(self.coordenadaY),str(self.mi_modo_vision.name))


    def cambiarModoVision(self):
        if self.mi_modo_vision == modo_vision.NOCTURNA:
            self.mi_modo_vision = modo_vision.DIURNA
        elif self.mi_modo_vision == modo_vision.DIURNA:
            self.mi_modo_vision == modo_vision.NOCTURNA
# ----------------- /class