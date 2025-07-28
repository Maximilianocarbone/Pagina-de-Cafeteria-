class Coche(): #establecemos las propiedades de los objetos de tipo coche 
    #definimos el estado inicial con def __init__(self):
    def __init__(self):
        self.__largochasis = 250 # 4 propiedadaes 
        self.__anchochasis = 120
        self.__ruedas = 4 #__ significa que es privado(encapsulado)
        self.__enmarcha = False
        
    #pueden haber mas pero para hacerlo corto lo hacemos asi
    
    #creanado un metodo con def(self):
    def arrancar(self,arrancamos):
        self.enmarcha = arrancamos
    #evalua si en marcha es True o False
        if(self.enmarcha):
            return "el coche esta en marcha"
        else:
            return "el coche esta parado"
        
    def estado(self):
        print("el coche tiene ", self.__ruedas, "ruedad. Un ancho de ",self.__anchochasis,"y un largo de ",self.__largochasis)
                                
    

#Instanciar un objeto de tipo coche 
micoche = Coche()
    

print(micoche.arrancar(True)) #llamamos al metodo arrancar del objeto micoche
print(micoche.estado()) #llamamos al metodo estado del objeto micoche

print("-------------A continuacion creamos el segundo objeto-----------------------------------------------------------")

micoche2 = Coche()
print(micoche2.arrancar(False))
print(micoche2.estado())
