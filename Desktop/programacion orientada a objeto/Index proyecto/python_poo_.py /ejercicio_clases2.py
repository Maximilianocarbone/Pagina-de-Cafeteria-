"""Clase CuentaBancaria:

Diseña una clase CuentaBancaria con atributos privados: numeroCuenta (string), titular (string) y saldo (double/float).

El saldo debe inicializarse en 0 en el constructor.

Crea métodos públicos para:

Depositar dinero (depositar(cantidad)): Agrega cantidad al saldo. Asegúrate de que la cantidad sea positiva.

Retirar dinero (retirar(cantidad)): Resta cantidad del saldo. Asegúrate de que la cantidad sea positiva y que haya suficiente saldo.

Obtener el saldo actual (getSaldo()).

Un método mostrarInformacion() que imprima todos los detalles de la cuenta."""

class CuestaBancaria():
    def __init__(self,numeroCuenta, titular, saldo ):
        self.__numeroCuenta = numeroCuenta
        self.__titular = titular 
        self.__saldo = float(saldo)
    
    def depositar(self,cantidad):
        
        if cantidad > 0 :
            self.__saldo += cantidad
            print (f"se deposito correctamete : ${cantidad}")
        else:
            print( "es mayor al sueldo ")
        
    
    
    def retirar(self,cantidad):
        
        if(cantidad < 0 ):
            print( "no se puede retirar ingrese otro monto")
            
        elif (cantidad > self.__saldo):
            print("el monto es mayor al saldo disponible")
        
        else:
            self.__saldo -= cantidad
            print(f"se retiro correctamente: ${cantidad}")
    
    def saldoActual(self):
        print(self.__saldo)
        
    
    def MostrarInformacion(self):
        print(f"El numero de cuenta es {self.__numeroCuenta} | El saldo es de : {self.__saldo} | El titular es: {self.__titular} ")

    
sueldo = CuestaBancaria("1234","manuel", 23.000)
sueldo.saldoActual()

sueldo.depositar(23.000)

sueldo.retirar(12.000)

sueldo.saldoActual()

sueldo.MostrarInformacion()