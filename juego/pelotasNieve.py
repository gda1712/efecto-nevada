import pygame

class PelotasNieve(object):
    
    """
    Clase que representa una pelota de nieve
    """

    def __init__(self, ventana, posX, posY, color, radio):

        # Inicializamos la posición
        self.__posX = posX
        self.__posY = posY

        # Le damos el color y tamaño a la pelota
        self.__color = color
        self.__radio = radio

        # Le indicamos a la ventana a la que pertenece
        self.__ventana = ventana

    
    # Métodos SET
    def setPosX(self, posX):
        self.__posX = posX
    def setPosY(self, posY):
        self.__posY = posY

    
    # Métodos GET
    def getPosX(self):
        return self.__posX
    def getPosY(self):
        return self.__posY


    def pintarPelotaNieve(self):
        # Método que se encarga de pintar la pelota de nieve
        pygame.draw.circle(self.__ventana, self.__color, (self.__posX, self.__posY), self.__radio)

