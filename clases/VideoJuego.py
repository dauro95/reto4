from clases.Entrega import Entregable

class VideoJuego(Entregable):
    
    __titulo =""
    __horas=0
    __genero=""
    __compania=""

#Creo el constructor de la clase

    def __init__(self,titulo,genero,compania,horas=10,entregado=False) -> None:
        super().__init__(entregado)
        self.__titulo=titulo
        self.__genero=genero
        self.__compania=compania
        self.__horas=horas

    @property
    def titulo(self):
        return(self.__titulo)

    @property
    def genero(self):
        return(self.__genero)

    @property
    def compania(self):
        return(self.__compania)

    @property
    def horas(self):
        return(self.__horas)

    @titulo.setter
    def titulo(self,titulo):
        self.__titulo=titulo

    @genero.setter
    def genero(self,genero):
        self.__genero=genero
    
    @compania.setter
    def compania(self,compania):
        self.__compania= compania
    
    @horas.setter
    def horas(self,horas):
        self.__horas=horas
    
    #sobre carga de __str

    def __str__(self) -> str:
        cadena=  self.__titulo + " - " + self.__genero +" - " + self.compania + " - " + str(self.__horas) + " " + str(self.isEntregado())
        return (cadena)
 
    # #metodo que compara las horas del videojuego
    def compare (self, objeto):
        if (isinstance(objeto,VideoJuego)):
            if(self.__horas>=objeto.horas):
                return(True)
            else:
                return(False)
        else:
            raise TypeError('No es un videojuego')