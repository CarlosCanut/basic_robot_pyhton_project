from paquete_robots.RobotTransportador.robotTransportador import RobotTransportador

# Robot behaviour for flying class
class RobotVolador(RobotTransportador):

    def aterrizar(self):
        print("Aterrizo")

    def despegar(self):
        print("Despegar")
# ---------------- /class