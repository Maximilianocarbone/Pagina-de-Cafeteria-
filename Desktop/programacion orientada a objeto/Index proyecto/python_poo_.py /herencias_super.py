class persona():
    def __init__(self,nombre, edad, lugar):
        self.nombre = nombre
        self.edad = edad
        self.lugar = lugar
    
    
    def descripcion(self):
        print("nombre: ", self.nombre, "\nEdad: ", self.edad, "\nLugar: ", self.lugar)
         
class empleado(persona):
    
    def __init__(self, salario, antiguedad, nombre_empleado, edad_empleado, residencia_empleado):
        
        super().__init__(nombre_empleado, edad_empleado, residencia_empleado)
        #llamamos al constructor de la clase padre persona
        #super() hace referencia a la clase padre
        self.salario = salario
        
        self.antiguedad = antiguedad
         
Manuel = empleado(1500,15,"manuel",55,"Colombia")

Manuel.descripcion()