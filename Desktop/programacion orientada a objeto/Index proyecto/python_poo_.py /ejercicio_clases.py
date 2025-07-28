"""Clase Libro:
Crea una clase llamada Libro con los siguientes atributos: titulo (string), autor (string), isbn (string) y disponible (booleano).
Todos los atributos deben ser privados.
Implementa un constructor para inicializar los atributos.
Crea métodos públicos para:
Obtener (get) el título, autor e ISBN.
Obtener y establecer (get y set) la disponibilidad del libro.
Un método llamado prestar() que cambie la disponibilidad a false si el libro está disponible y muestre un mensaje de éxito o fracaso.
Un método llamado devolver() que cambie la disponibilidad a true y muestre un mensaje."""

class Libro:
    def __init__(self,titulo,autor,isbn,disponible = True):
        self.__titulo = titulo
        self.__autor = autor
        self.isbn = isbn
        self.__disponible = disponible
        
    
    #getters
    def get__titulo(self):
        return self.__titulo
    
    def get__autor(self):
        return self.__autor
    
    def get__isbn(self):
        return self.isbn 
    
    def get__disponible(self):
        return self.__disponible
    
    #setters para la disponibilidad
    def set__disponible(self,disponible):
        self.__disponible = disponible
        
    #metodo para prestar el libro
    def prestar(self):
        if (self.__disponible):
            self.__disponible = False
            print(f"El libro {self.__titulo} ha sido prestado.")
            
        else:
            print(f"El libro {self.__titulo} no esta disponible en este momento ")
    
    #metodo para devolver el libro
    def devolver(self):
        self.__disponible = True
        print(f"El libro {self.__titulo} ha sido devuelto correctamente ")
        
libros = Libro("el quijotre","migel serbantes", "1234567")

libros.prestar()

libros.prestar()

libros.devolver()

libros. prestar()