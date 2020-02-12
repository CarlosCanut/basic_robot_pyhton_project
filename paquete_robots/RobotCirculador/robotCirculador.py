from paquete_robots.RobotTransportador.robotTransportador import RobotTransportador
from paquete_robots.RobotVigilador.robotVigilador import RobotVigilador
from paquete_robots.Enumeraciones.enumeraciones import estado_robot

# Robot behaviour for driving class
class RobotCirculador(RobotTransportador,RobotVigilador):

    def arrancar(self):
        print("Arrancar")
        estado_robot.ENCENDIDO

    def apagar(self):
        print("Apagar")
        estado_robot.APAGADO
# --------------- /class