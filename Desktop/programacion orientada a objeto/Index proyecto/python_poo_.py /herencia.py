class Vehiculos():
    
    def __init__(self, marca, modelo):
        
        self.marca = marca
        self.modelo = modelo 
        self.enmarcha = False #por defecto el vehiculo no esta en marcha
        self.acelera = False #por defecto el vehiculo no acelera
        self.frena = False #por defecto el vehiculo no frena
        
    def arrancar(self):
        self.enmarcha = True
        
    
    def acelerar(self):
        self.acelera = True
        
    def frenar(self):
        self.frena = True
        
    def estado(self):
        print("marca; ", self.marca, "\nmodelo: ", self.modelo, "\nen marcha: ", self.enmarcha, "\nacelera: ", self.acelera, "\nfrena: ", self.frena)
        
        
class furgoneta(Vehiculos):
    
    def carga(self,cargar):
        self.cargado= cargar
        if(self.cargado):
            return "La furgneta esta cargada"
        else:
            return"la furgoneta no esta cargada"        
        
#aplicamos herencia
class Moto(Vehiculos):
    hcaballito = ""
    
    #metodo propio de la clase moto 
    def caballito(self):
        self.hcaballito = "voy haciendo el caballito"
        
    #este metodo es heredado de la clase Vehiculos
    #ahora haciendo esto sobrescribimos el metodo estado de la clase Vehiculos
    def estado(self):
        print("marca; ", self.marca, "\nmodelo: ", self.modelo, "\nen marcha: ", self.enmarcha, "\nacelera: ", self.acelera, 
              "\nfrena: ", self.frena, "\n", self.hcaballito)

class Velectricos():
    def __init__(self):
        self.autonomia = 100
        
    def cargarenergia(self):
        self.cargando = True

miMoto = Moto("Yamaha", "MT-07")
miMoto.caballito()
miMoto.estado()

miFurgoneta = furgoneta("Mercedes", "Sprinter")

miFurgoneta.arrancar()

miFurgoneta.estado()

print(miFurgoneta.carga(True))

#cuando hay herencia multiple, se da preferencia a la clase que se encuentra primero en el parentesis
class Bicicletaelectrica(Vehiculos, Velectricos):
    pass

mibici =Bicicletaelectrica("orbea", "e-1000")