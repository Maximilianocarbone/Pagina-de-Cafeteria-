"""3. Clase CuentaBancaria
Atributos privados: titular, saldo.

Métodos:

depositar(cantidad)

retirar(cantidad)

mostrar_saldo()"""

class CuentaVancaria():
    def __init__(self,titular,saldo):
        self.__titular = titular
        self.__saldo = int(saldo)
        
    def depositar(self,cantidad):
        if cantidad > 0:
            self.__saldo += cantidad
            return f"se ha depositado {cantidad} y el nuevo saldo es {self.__saldo}"
        else:
            return"la cantidad a depositar debe ser mayor a 0" 
        
    def mostrar_saldos(self):
        return f"el saldo es {self.__saldo} y el titular es {self.__titular}"
        
    
    def retirar(self,cantidad):
        if cantidad > 0 and cantidad <+ self.__saldo:
            self.__saldo -= cantidad
            return f"se ha retirado {cantidad} y el nuevo saldo es {self.__saldo}"
        else:
            return "la cantidad a retirar debe ser mayor a 0 y menor a el saldp actual "
            
persona1 = CuentaVancaria("angel",1000)
print("--" * 20)    
print(persona1.depositar(500))
print("--" * 20)
print(persona1.mostrar_saldos())
print("--" * 20)
print(persona1.retirar(200))
print("--" * 20)
print(persona1.mostrar_saldos())
print("--" * 20)
    