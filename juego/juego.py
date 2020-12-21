from sys import exit
from random import randint
from .pelotasNieve import PelotasNieve
import pygame


class Juego(object):

    """ 
    Clase que se encarga de administrar el juego y las pelotas
    """
    
    def __init__(self, cantidadPelotas):

        # Creamos la ventana y el reloj de los fps
        self.__tamanoVentana = (800, 600)
        self.__ventana = pygame.display.set_mode(self.__tamanoVentana)
        self.__reloj = pygame.time.Clock()

        # Declaramos los colores necesarios en el programa
        self.__colorFondo = (34,40,49)
        self.__colorPelotas = (255, 255, 255)

        # Declaramos la lista de pelotas y sus valores
        self.__pelotas = list()

        # Generamos las pelotas COPOS de NIEVE y lo añadimos a la lista
        for i in range(0, cantidadPelotas):
            nuevaPelota = PelotasNieve(self.__ventana, randint(0, 800), randint(0, 600), self.__colorPelotas, 1)
            self.__pelotas.append(nuevaPelota)

        # Iniciamos el Loop
        self.mainLoop()

    
    def mainLoop(self):
        # Ciclo principal del juego

        while True:
            for evento in pygame.event.get():
                if evento.type == pygame.QUIT:
                    # En caso que se trate de cerrar el juego, se cierra el programa
                    exit()
            
            # Pintamos fondo de pantalla
            self.__ventana.fill(self.__colorFondo)

            # Pintamos y agregamos las pelotas de nieve
            self.moverPelotasNieve()

            # Actualizamos pantalla y establecemos fps
            pygame.display.flip()
            self.__reloj.tick(60)


    def moverPelotasNieve(self):
        # Método que se encarga de mover las pelotas de nieve

        for pelota in self.__pelotas:

            # En caso de que se salgan las peltoas de la ventana, las ponemos en un principio
            if(pelota.getPosX() > self.__tamanoVentana[0]):
                pelota.setPosX(0)

            if(pelota.getPosY() > self.__tamanoVentana[1]):
                pelota.setPosY(0)

            # Le asignamos un movimiento para que la caida sea más realista
            pelota.setPosX(pelota.getPosX() + randint(-3, 3))
            pelota.setPosY(pelota.getPosY() + 3)

            # Pintamos la pelota de nieve
            pelota.pintarPelotaNieve()


