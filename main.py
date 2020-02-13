# ---------------------------------------------------------
# main.py
# description: fichero para realizar las pruebas del paquete_robots
# autor: Carlos Canut
# ---------------------------------------------------------

def main():

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
    print("g) Terminar")
    print('')
    
    respuesta = input()

    if respuesta == 'a':
        print('')
        print("Vamos a crear un nuevo robot")
    elif respuesta == 'b':
        print('')
        print("Vamos a crear una nueva carga")
    elif respuesta == 'c':
        print('')
        print("Vamos a asignar una carga a un robot para transportar")
    elif respuesta == 'd':
        print('')
        print("Vamos a transportar una carga con un robot")
    elif respuesta == 'e':
        print('')
        print("Vamos a soltar la carga")
    elif respuesta == 'f':
        print('')
        print("Vamos a imprimir un informe del sistema")
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
        print("Adios :) !!!")
        return
    
    
    


main()



