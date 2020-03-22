# ---------------------------------------------------------
# main.py
# description: fichero para realizar las pruebas del paquete_robots
# autor: Carlos Canut
# ---------------------------------------------------------
from paquete_robots.Carga.carga import Carga
from paquete_robots.Enumeraciones.enumeraciones import *
from paquete_robots.Robot.robot import Robot
from paquete_robots.RobotCirculador.robotCirculador import RobotCirculador
from paquete_robots.RobotVigilador.robotVigilador import RobotVigilador
from paquete_robots.RobotTransportador.robotTransportador import RobotTransportador
from paquete_robots.RobotVolador.robotVolador import RobotVolador
import time
import pickle
from io import open

def main():
    while True:
        # http://patorjk.com/software/taag/#p=testall&h=0&v=0&f=Dancing%20Font&t=Jinko%20Robotics
        print("   ___  _         _            ______         _             _    _            ")
        print("  |_  |(_)       | |           | ___ \       | |           | |  (_)           ")
        print("    | | _  _ __  | | __  ___   | |_/ /  ___  | |__    ___  | |_  _   ___  ___ ")
        print("    | || || '_ \ | |/ / / _ \  |    /  / _ \ | '_ \  / _ \ | __|| | / __|/ __|")
        print("/\__/ /| || | | ||   < | (_) | | |\ \ | (_) || |_) || (_) || |_ | || (__ \__ \ ")
        print("\____/ |_||_| |_||_|\_\ \___/  \_| \_| \___/ |_.__/  \___/  \__||_| \___||___/")
        print("                                                                              ")
        
        print('')
        print("Selecciona una opción:")
        print("a) Crear un nuevo robot")
        print("b) Crear una nueva carga")
        print("c) Asignar carga a robot para transportar")
        print("d) Transportar carga con robot")
        print("e) Soltar carga")
        print("f) Imprime informe de sistema")
        print("g) Guardar datos del sistema en fichero")
        print("h) Cargar datos del sistema en fichero")
        print("i) Terminar")
        print('')
        
        respuesta = input()

        if respuesta == 'a':
            print('')
            tipoRobot = input("Elige que tipo de robot quieres crear: a) Robot, b) RobotTransportador, c) RobotVigilador, d) RobotVolador, e) RobotCirculador")
            if tipoRobot == 'a':
                miRobot = Robot("543fdd",estado_robot.ENCENDIDO,nivel_bateria.ALTO,3,3)
                print(miRobot)
                miRobot.encender()
            elif tipoRobot == 'b':
                miRobotTransportador = RobotTransportador("5326fsf",estado_robot.APAGADO,nivel_bateria.ALTO,0,0,7,0,7)
                print(miRobotTransportador)
            elif tipoRobot == 'c':
                miRobotVigilador = RobotVigilador("88rghg",estado_robot.APAGADO,nivel_bateria.MEDIO,5,5,modo_vision.NOCTURNA)
                print(miRobotVigilador)
            elif tipoRobot == 'd':
                miRobotVolador = RobotVolador("7898gf",estado_robot.ENCENDIDO,nivel_bateria.BAJO,7,7,5,0,5,False)
                print(miRobotVolador)
            elif tipoRobot == 'e':
                miRobotCirculador = RobotCirculador("765fdsa",estado_robot.APAGADO,nivel_bateria.AGOTADO,6,6,8,0,8,modo_vision.DIURNA,False)
                print(miRobotCirculador)
            time.sleep(2)
        elif respuesta == 'b':
            print('')
            print("Vamos a crear una nueva carga")
            miCarga = Carga(2,True,"La carga de ejemplo",2,2)
            print(miCarga)
            time.sleep(2)
        elif respuesta == 'c':
            print('')
            print("Vamos a asignar una carga a un robot para transportar")
            miRobotTransportador.cogerCarga(miCarga)
            print('')
            print("Mi Robot Transportador: ")
            print(miRobotTransportador)
            print("Mi Carga: ")
            print(miCarga)
            print('')
            time.sleep(2)
        elif respuesta == 'd':
            print('')
            nuevaPosicionX = input("Introduce la coordenada X: ")
            nuevaPosicionY = input("Introduce la coordenada Y: ")
            print("Vamos a transportar una carga de las coordenadas : x = {0}, y = {1} ".format(miCarga.coordenadaX,miCarga.coordenadaY))
            print("Hasta las coordenadas: x = {0}, y = {1}".format(nuevaPosicionX,nuevaPosicionY))
            miRobotTransportador.transportarCarga(miCarga,nuevaPosicionX,nuevaPosicionY)
            print('')
            print("Mi Robot Transportador: ")
            print(miRobotTransportador)
            print("Mi Carga: ")
            print(miCarga)
            print('')
            time.sleep(2)
        elif respuesta == 'e':
            print('')
            print("Vamos a soltar la carga")
            miRobotTransportador.soltarCarga(miCarga)
            print('')
            print("Mi Robot Transportador: ")
            print(miRobotTransportador)
            print("Mi Carga: ")
            print(miCarga)
            print('')
            time.sleep(2)
        elif respuesta == 'f':
            print('')
            try:
                print(miRobot)
                print(miRobotTransportador)
                print(miRobotVigilador)
                print(miRobotVolador)
                print(miRobotCirculador)
                print(miCarga)
            except:
                print("Fin del informe")
                time.sleep(2)
            

        elif respuesta == 'q':
            print("     _                      _   _        _  __       U  ___ u ")
            print('  U |"| u        ___       | \ |"|      |"|/ /        \/"_ \/ ')
            print(' _ \| |/        |_"_|     <|  \| |>     |   /         | | | | ')
            print("| |_| |_,-.      | |      U| |\  |u   U/| . \\u   .-,_| |_| | ")
            print(' \___/-(_/     U/| |\ u    |_| \_|      |_|\_\     \_)-\___/  ')
            print("  _//       .-,_|___|_,-.  ||   \\,-. ,-,>> \\,-.       \\    ")
            print(' (__)        \_)-' '-(_/   (_")  (_/   \.)   (_/       (__)   ') 
            return
        elif respuesta == 'g':
            print('')
            print("Cargar Datos del sistema en fichero")
            print('')
            try:
                miRobot
            except NameError:
                miRobot = None 
            try:
                miRobotTransportador
            except NameError:
                miRobotTransportador = None 
            try:
                miRobotVigilador
            except NameError:
                miRobotVigilador = None 
            try:
                miRobotVolador
            except NameError:
                miRobotVolador = None
            try:
                miRobotCirculador
            except NameError:
                miRobotCirculador = None
            try:
                miCarga
            except NameError:
                miCarga = None

            robots_y_cargas = {}

            if miRobot != None:
                robots_y_cargas['Robot'] = str(miRobot)
            if miRobotTransportador != None:
                robots_y_cargas['RobotTransportador'] = str(miRobotTransportador)
            if miRobotVigilador != None:
                robots_y_cargas['RobotVigilador'] = str(miRobotVigilador)
            if miRobotVolador != None:
                robots_y_cargas['RobotVolador'] = str(miRobotVolador)
            if miRobotCirculador != None:
                robots_y_cargas['RobotCirculador'] = str(miRobotCirculador)
            if miCarga != None:
                robots_y_cargas['Carga'] = str(miCarga)

            print(robots_y_cargas)
            fichero = open('sistemaRobots.bd','wb')
            pickle.dump(robots_y_cargas,fichero)
            fichero.close()
                
            print('')
            time.sleep(2)
        elif respuesta == 'h':
            print('')
            print("Cargar datos del sistema desde fichero")
            fichero = open('sistemaRobots.bd','rb')
            datosRobots = pickle.load(fichero)
            fichero.close()
            print("Estos son los datos de los robots encontrado en el fichero sistemaRobots.bd: ")
            print(datosRobots)
            print('')
            time.sleep(2)
        elif respuesta == 'i':
            print('')
            print("Adios :) !!!")
            return
        
    
    


main()



