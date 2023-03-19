# ----   Clase para el EJERCICIO 7 ------
print("""Crea una clase llamada Cuenta que tendrá los siguientes atributos: titular (que es una
persona) y cantidad (puede tener decimales). El titular será obligatorio y la cantidad es
opcional. Crear los siguientes métodos para la clase:
* Un constructor, donde los datos pueden estar vacíos.
* Los setters y getters para cada uno de los atributos. El atributo no se puede modificar
directamente, sólo ingresando o retirando dinero.
* mostrar(): Muestra los datos de la cuenta.
* ingresar(cantidad): se ingresa una cantidad a la cuenta, si la cantidad introducida es
negativa, no se hará nada.
* retirar(cantidad): se retira una cantidad a la cuenta. La cuenta puede estar en números
rojos.""")



############################################################################
############   Clase       #################################################
############################################################################
class Cuenta:
    def __init__(self,titular,cantidad=0,edad=0):#NOTA: se agrega edad ya que en el ejercicio 8 se requiere
        if(type(titular)==str):#para asegurar que escriba un string en la primer posicion
            self.__titular=titular
            self.__cantidad=cantidad
            self.__edad=edad
        
    #getters y setters para el titular
    @property
    def titular(self):
        return self.__titular
    
    @titular.setter
    def titular(self,nombre):
        self.__titular=nombre

    #getters y setters para la edad
    @property
    def edad(self):
        return self.__edad
    
    @edad.setter
    def edad(self,nombre):
        self.__titular=nombre

    #getters y setters para la cantidad
    @property
    def cantidad(self):
        return self.__cantidad
    
    #dejo comentado el setter porque dice que solo se puede modificar directamente
    #@cantidad.setter
    #def cantidad(self,cantidad2):
    #    self.__cantidad=cantidad2
        
    #metodo mostrar
    def mostrar(self):
        print(f"datos de cuenta:\ntitular: {self.__titular}; cantidad: {self.__cantidad}")
    
    
    #metodo ingresar dinero

    def ingresar(self,monto):
        if(type(monto)==int or type(monto)==float):
            if(monto>0):
                self.__cantidad+=monto

    #metodo retirar dinero
    def retirar(self,monto):
        self.__cantidad-=monto



############################################################################
##################### Banco de Pruebas #####################################
############################################################################

print("\nCarga inicial de la cuenta completa:")
cuenta1=Cuenta("Jorge",15000)
cuenta1.mostrar()

#Si se descomentan las 3 lineas siguientes debe dar error ya que no esta permitido no ingresar un titular
#print("\nCarga inicial de cuenta sin titular:")
#cuenta2=Cuenta(15000)
#cuenta2.mostrar()

print("\nCarga inicial sin monto:")
cuenta3=Cuenta("Juan")
cuenta3.mostrar()


print("\nSe cambia el titular de la cuenta:")
cuenta1.titular="Brenda"
cuenta1.mostrar()

#Si se descomentan las 2 lineas siguientes debe dar error ya que no esta permitido por enunciado
#print("\nSe cambia el monto de la cuenta:")
#cuenta1.cantidad=100 no se permite modificar de esta manera por enunciado

print("\nSe ingresa monto negativo, accion no valida se ignora:")
cuenta1.ingresar(-32)
cuenta1.mostrar()


print("\nSe ingresa monto positivo, accion valida se actualiza monto:")
cuenta1.ingresar(5000)
cuenta1.mostrar()

print("\nSe retira monto positivo, accion valida se actualiza monto:")
cuenta1.retirar(10000)
cuenta1.mostrar()


print("\nSe retira monto positivo, accion valida se actualiza monto(queda en numeros rojos):")
cuenta1.retirar(20000)
cuenta1.mostrar()
