"""Crea una clase Persona con:

Atributos: nombre, edad.

Método saludar() que devuelva: "Hola, soy [nombre] y tengo [edad] años".

"""

class persona():
    def __init__(self, nombre, edad):
        self.nombre = nombre
        self.edad = edad
        
    def saludar(self):
        return f"Hola ,soy {self.nombre} y Tengo {self.edad} anos "
    
nombre_usuario = input("ingrese su nombre: ")
edad_usuario = int(input("ingrese su edad: "))


persona1 = persona(nombre_usuario,edad_usuario)
print(persona1.saludar()) 