# ----   Clase para el EJERCICIO 8 ------
print("""Vamos a definir ahora una “Cuenta Joven”, para ello vamos a crear una nueva clase
CuantaJoven que deriva de la clase creada en el punto 7. Cuando se crea esta nueva clase,
además del titular y la cantidad se debe guardar una bonificación que estará expresada en
tanto por ciento. Crear los siguientes métodos para la clase:
* Un constructor.
* Los setters y getters para el nuevo atributo.
* En esta ocasión los titulares de este tipo de cuenta tienen que ser mayor de edad, por lo
tanto hay que crear un método es_titular_valido() que devuelve verdadero si el titular es
mayor de edad pero menor de 25 años y falso en caso contrario.
* Además, la retirada de dinero sólo se podrá hacer si el titular es válido.
* El método mostrar() debe devolver el mensaje de “Cuenta Joven” y la bonificación de la
cuenta.""")

########################################################################################
#############   Clase Padre ############################################################
########################################################################################


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

########################################################################################
#############   Clase Hijo #############################################################
########################################################################################

class CuentaJoven(Cuenta):
    def __init__(self,titular,cantidad,edad,bonificacion=0):
        super().__init__(titular,cantidad,edad)
        self.__bonificacion=bonificacion

    #getters y setters para la bonificacion
    @property
    def bonificacion(self):
        return self.__bonificacion
    
    @bonificacion.setter
    def bonificacion(self,bonificacion):
        self.__bonificacion=bonificacion


    def es_titular_valido(self):
        if self.edad>=18 and self.edad<25:
            return True
        else:
            return False

    #metodo mostrar
    def mostrar(self):#si titular valido muestro cuenta joven sino muestro el mostrar del punto 7
        if self.es_titular_valido():
            print(f"Cuenta Joven:\ntitular:{self.titular}; edad:{self.edad}; bonificacion:{self.__bonificacion}%; cantidad:{self.cantidad}")
        else:
            super().mostrar()
        
    #metodo retirar dinero
    def retirar(self,monto):
        if self.es_titular_valido():
            super().retirar(monto)
        else:
            print ("para retirar debe ser mayor de edad")


########################################################################################
#############   Banco de Pruebas #######################################################
########################################################################################

#prueba del ejercicio 8
print("\n\nejercicio 8:\n\n")
#titular,edad,cantidad,bonificacion=0):

print("\nCarga inicial de titular con edad invalida:")
cuenta1=CuentaJoven("Juan",1000,15,0)
cuenta1.mostrar()

print("\nCarga inicial de titular con edad valida:")
cuenta2=CuentaJoven("Karen",11000,19,10)
cuenta2.mostrar()

print("\nPrueba de cambio de titular en cuenta invalida:")
cuenta1.titular="Jenny"
cuenta1.mostrar()


print("\nPrueba de cambio de titular en cuenta valida:")
cuenta2.titular="Chloe"
cuenta2.mostrar()

#Si se descomentan las 3 lineas siguientes debe dar error ya que no esta permitido no ingresar un titular
#print("\nCarga inicial de cuenta sin titular:")
#cuenta3=Cuenta(15000)
#cuenta3.mostrar()

print("\nPrueba de ingreso de dinero:")
cuenta2.ingresar(5000)
cuenta2.mostrar()

print("\nPrueba de retiro de dinero:")
cuenta2.retirar(10000)
cuenta2.mostrar()

print("\nPrueba de retiro de dinero (cuenta en numero rojos):")
cuenta2.retirar(20000)
cuenta2.mostrar()
