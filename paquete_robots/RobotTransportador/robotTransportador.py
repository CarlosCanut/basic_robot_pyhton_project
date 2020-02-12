from paquete_robots.Robot.robot import Robot

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