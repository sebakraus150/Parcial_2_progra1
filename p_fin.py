import pygame
from configs import *
from assets.boton import Boton
from assets.texto import Texto
from colores import *
from funciones_base import *

def terminar_juego():
    global pantalla_actual
    pantalla_actual = "menu"

    # while True:
    #     PANTALLA.fill((0, 0, 0))

    #     texto = Texto("Juego Finalizado", 128, COLOR_BLANCO,posicion=(0,500), centrar_horizontal=True)
    #     texto.dibujar(PANTALLA)

    #     pygame.display.flip
    #     pygame.time.wait(3000)

    #     pygame.quit()

    #     pygame.display.flip()

    