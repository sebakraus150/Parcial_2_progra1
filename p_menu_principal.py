import pygame
from configs import *
from assets.boton import Boton
from assets.texto import Texto
from colores import *
from p_juego_iniciado import *
from p_ranking import *
from p_fin import *
import pygame.mixer as mixer

pygame.init()
mixer.init()

# Funciones de pantalla
def menu_principal():
    '''
    ¿Qué hace? : Muestra la pantalla del menú principal con botones interactivos y un texto destacado. Permite navegar entre pantallas o salir del juego.
    ¿Qué recibe? : No recibe parámetros directamente, utiliza las variables globales configuradas (PANTALLA, botones, texto, fondo).
    ¿Qué retorna? : 
        - "salir" -> str > Si el usuario cierra la ventana.
        - pantalla_actual -> str > El identificador de la pantalla actual a mostrar después del menú.
    '''
    while True:
        PANTALLA.blit(fondo, (0, 0))
        texto.dibujar(PANTALLA)

        for evento in pygame.event.get():
            if evento.type == pygame.QUIT:
                return "salir"

            for boton in botones:
                boton.manejar_evento(evento)

        for boton in botones:
            boton.dibujar(PANTALLA)

        pygame.display.flip()


        if pantalla_actual != "menu":
            return pantalla_actual

# Acciones de los botones
def accion_boton_1():
    global pantalla_actual
    print("Cambiando a pantalla de juego")
    pantalla_actual = "juego"

def accion_boton_2():
    global pantalla_actual
    print("Cambiando a pantalla de ranking")
    pantalla_actual = "ranking"

def accion_boton_3():
    print("Opciones (pendiente)")  

# Configurar la pantalla
pygame.display.set_caption("Fulbito")

# Instanciación de los botones
boton1 = Boton(350, 250, 300, 75, "Iniciar Juego", COLOR_BLANCO, COBALT, BLUE, BLUE3, accion_boton_1)
boton2 = Boton(350, 400, 300, 75, "Ver Ranking", COLOR_BLANCO, COBALT, BLUE, BLUE3, accion_boton_2)
boton3 = Boton(350, 550, 300, 75, "Opciones", COLOR_BLANCO, COBALT, BLUE, BLUE3, accion_boton_3)
botones = [boton1, boton2, boton3]

#Musica de fondo
pygame.mixer.music.load("assets/musica/Cancion_Fondo.mp3")
pygame.mixer.music.play(-1)
mixer.music.set_volume(0.3)

# Instanciación de los textos
texto = Texto("FULBITO", tamano_fuente=200, color=COLOR_BLANCO, posicion=(100, 50), centrar_horizontal=True)

# Control de pantallas
pantalla_actual = "menu"

while pantalla_actual != "salir":
    print(pantalla_actual) # sacar despues
    if pantalla_actual == "menu":
        pantalla_actual = menu_principal()
    elif pantalla_actual == "juego":
        pantalla_actual = pantalla_juego()
    elif pantalla_actual == "ranking":
        pantalla_actual = pantalla_ranking()

pygame.quit()
