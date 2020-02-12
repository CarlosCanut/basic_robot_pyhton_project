from paquete_robots.Robot.robot import Robot
from paquete_robots.Enumeraciones.enumeraciones import modo_vision

# Robot behaviour for watching over class
class RobotVigilador(Robot):

    modo_vision.NOCTURNA

    def cambiarModoVision(self):
        if modo_vision.NOCTURNA:
            modo_vision.DIURNA
        else:
            modo_vision.NOCTURNA
# ----------------- /class