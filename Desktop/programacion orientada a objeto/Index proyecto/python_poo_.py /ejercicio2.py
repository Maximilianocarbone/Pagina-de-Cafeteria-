"""2. Clase Rectángulo
Atributos: base, altura.

Método area() → base * altura

Método perimetro() → 2 * (base + altura)"""

class Rectangulo():
   def __init__(self,base,altura):
       self.base = int(base)
       self.altura = int(altura)
    
   def area(self):
        return self.base * self.altura 

base = int(input("ingrese el calor de la base: "))
altura = int(input("ingrese el valor de la altura "))

rectangul1 = Rectangulo(base,altura)

print(rectangul1.area())

   