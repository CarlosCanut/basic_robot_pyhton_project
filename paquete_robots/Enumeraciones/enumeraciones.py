import enum

# State of the robot
class estado_robot(enum.Enum):
    ENCENDIDO = 1
    APAGADO = 2

# vision mode
class modo_vision(enum.Enum):
    NOCTURNA = 1
    DIURNA = 2

# Battery level
class nivel_bateria(enum.Enum):
    AGOTADO = 1
    BAJO = 2
    MEDIO = 3
    ALTO = 4
    