import pygame
from configs import *
from assets.boton import Boton
from assets.texto import Texto
from colores import *
from p_juego_iniciado import *
from p_ranking import *
from p_ingreso import *
from p_opciones import *
import pygame.mixer as mixer

pygame.init()
mixer.init()

# Funciones de los botones
def menu_boton_1():
    global pantalla_actual
    pantalla_actual = "ingreso_nombre"

def menu_boton_2():
    global pantalla_actual
    pantalla_actual = "ranking"

def menu_boton_3():
    global pantalla_actual
    pantalla_actual = "opciones"

# Instanciación de los botones
menu_boton1 = Boton(350, 250, 300, 75, "Iniciar Juego", COLOR_BLANCO, COBALT, BLUE, BLUE3, menu_boton_1)
menu_boton2 = Boton(350, 400, 300, 75, "Ver Ranking", COLOR_BLANCO, COBALT, BLUE, BLUE3, menu_boton_2)
menu_boton3 = Boton(350, 550, 300, 75, "Opciones", COLOR_BLANCO, COBALT, BLUE, BLUE3, menu_boton_3)
menu_botones = [menu_boton1, menu_boton2, menu_boton3]

# Música de fondo
pygame.mixer.music.load("assets/musica/Cancion_Fondo.mp3")
pygame.mixer.music.play(-1)
mixer.music.set_volume(0.3)

# Texto en pantalla
texto = Texto("FULBITO", tamano_fuente=200, color=COLOR_BLANCO, posicion=(100, 50), centrar_horizontal=True)

# Control de pantallas
pantalla_actual = "menu"

def menu_principal():
    '''Función del menú principal que muestra los botones y maneja los eventos de click.'''
    global pantalla_actual

    while True:
        PANTALLA.blit(fondo, (0, 0))
        texto.dibujar(PANTALLA)

        # Manejo de eventos
        for evento in pygame.event.get():
            if evento.type == pygame.QUIT:
                return "salir"
            for boton in menu_botones:
                boton.manejar_evento(evento)

        # Dibujar los botones
        for boton in menu_botones:
            boton.dibujar(PANTALLA)

        pygame.display.flip()

        # Control de cambio de pantalla
        if pantalla_actual != "menu":
            return pantalla_actual

# Control de pantallas
while pantalla_actual != "salir":
    if pantalla_actual == "menu":
        pantalla_actual = menu_principal()
    elif pantalla_actual == "ingreso_nombre":
        pantalla_actual = mostrar_ventana_ingreso_nombre()
    elif pantalla_actual == "juego":
        pantalla_actual = pantalla_juego()
    elif pantalla_actual == "ranking":
        pantalla_actual = pantalla_ranking()
    elif pantalla_actual == "opciones":
        pantalla_actual = pantalla_opciones()

pygame.quit()
