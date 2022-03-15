from abc import ABC, abstractmethod

class Entregable(ABC):
    
    __entregado = False

    def __init__(self,entregado=False) -> None:
        pass

    #no tiene atributos
    # metodos

    def entregar(self):
        self.__entregado=True

    def devolver(self):
        self.__entregado=False

    def isEntregado(self):
        if (self.__entregado):
            return(True)
        else:
            return(False)

    @abstractmethod   
    def compare (self, objeto):
        pass    
