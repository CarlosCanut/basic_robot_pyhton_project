
# Robot class
class Carga:
    peso = 0
    esFragil = False
    nombre = "carga"
    coordenadaX = 0
    coordenadaY = 0

    def __init__(self, peso, esFragil, nombre, coordenadaX, coordenadaY):
        self.peso = peso
        self.esFragil = esFragil
        self.nombre = nombre
        self.coordenadaX = coordenadaX
        self.coordenadaY = coordenadaY
        print("Nueva carga creada")
    
    def __str__(self):
        return " peso: {}, esFragil: {}, nombre: {}, X: {}, Y: {}".format(str(self.peso),str(self.esFragil),str(self.nombre),str(self.coordenadaX),str(self.coordenadaY))
        #return "("+str(self.peso)+","+str(self.esFragil)+","+str(self.nombre)+str(self.coordenadaX)+","+str(self.coordenadaY)+")"

    
        

# ------------- /Carga class