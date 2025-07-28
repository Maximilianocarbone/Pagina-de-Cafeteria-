class Coche():
    
    def __init__(self):
        self.__largochasis = 250
        self.__anchochasis = 120
        self.__ruedas = 4 #__ 
        self.__enmarcha = False
        

    def arrancar(self,arrancamos):
        self.__enmarcha = arrancamos
        
        if(self.__enmarcha): # empieza el chequeo interno
            chequeo = self.__chequeo_interno()
            
        #agregamos la variable chequeo para ver si el coche esta en condiciones de arrancar
        if(self.__enmarcha and chequeo == True):
            return "el coche esta en marcha"
        
        elif(self.__enmarcha and chequeo == False):
            return "algo a ido mal en el chequeo interno, el coche no puede arrancar"
        
        else:
            return "el coche esta parado"
        

    def estado(self):
        print("el coche tiene ", self.__ruedas, "ruedad. Un ancho de ",self.__anchochasis,"y un largo de ",self.__largochasis)
     
     
     
    #con este metodo podemos hacer un chequeo interno del coche 
    #para ver si esta en condiciones de arrancar                      
    def __chequeo_interno(self):#__ lo convierte en privado 
        print("Realizando chequeo interno...")
        
        self.gasolina ="ok"
        self.aceite="ok"
        self.puertas="cerradas"
        
        if(self.gasolina == "ok" and self.aceite=="ok" and self.puertas == "cerradas"):
            return True
        else:
            return False


micoche = Coche()
    

print(micoche.arrancar(True)) 
print(micoche.estado()) 

print("-------------A continuacion creamos el segundo objeto-----------------------------------------------------------")

micoche2 = Coche()

print(micoche2.arrancar(False))
print(micoche2.estado())
