from clases.Entrega import Entregable

class Serie(Entregable):
 
    __tiutlo =""
    __temporadas = 0
    __genero=""
    __creador =""

    def __init__(self,titulo,genero,creador,temporadas=3,entregado=False) -> None:
        super().__init__(entregado)
        self.__titulo= titulo
        self.__temporadas= temporadas
        self.__genero = genero
        self.__creador = creador
    
    @property
    def titulo(self):
        return(self.__titulo)
    
    @property
    def temporadas(self):
        return self.__temporadas

    @property
    def genero(self):
        return self.__genero
    
    @property
    def creador(self):
        return self.__creador
  
    @titulo.setter
    def titulo(self,titulo):
        self.__titulo=titulo

    @temporadas.setter
    def temporadas(self,temporadas):
        self.__temporadas=temporadas
    
    @genero.setter
    def genero(self,genero):
        self.__genero=genero

    @creador.setter
    def creador(self,creador):
        self.__creador=creador
    
    #sobre carga de __str

    def __str__(self) -> str:
        cadena=  self.__titulo + " - " + self.__genero + " - " + self.__creador + " - " + str(self.__temporadas) + " - " +  str(self.isEntregado())
        return (cadena)
    
    #metodo que compara las temporadas de la serie
 
    def compare (self, objeto):
        if (isinstance(objeto,Serie)):
            if(self.temporadas>=objeto.temporadas):
                return(True)
            else:
                return(False)
        else:
            raise TypeError('No es una Serie')