import pygame
from configs import *
from assets.boton import Boton
from assets.texto import Texto
from colores import *
from preguntas import preguntas
from funciones_base import *
from p_ranking import *
from ranking import *
import random

print(f"las {vidas}")

def pantalla_juego():
    '''
    ¿Qué hace? : Configura y muestra la pantalla principal del juego, incluyendo una pregunta aleatoria, botones con respuestas posibles y el contador de vidas. Controla las acciones del jugador.
    ¿Qué recibe? : No recibe parámetros directamente.
    ¿Qué retorna? : None
    '''

    global pregunta
    pregunta = pregunta_aleatoria(preguntas[0])

    def accion_boton(opcion):
        '''
        ¿Qué hace? : Verifica si la respuesta seleccionada es correcta o incorrecta. Modifica el número de vidas del jugador y cambia a la pantalla de ranking si las vidas llegan a 0.
        ¿Qué recibe? : 
            - opcion : int, la opción seleccionada por el jugador.
        ¿Qué retorna? : None
        '''
        global pregunta
        pregunta = pregunta_aleatoria(preguntas[0])
        global vidas
        print(opcion)
        vidas = modificar_vidas(vidas, pregunta["respuesta_correcta"], opcion)
        if vidas < 1:
            global pantalla_actual
            pantalla_actual = pantalla_ranking()
                
        boton1.actualizar_texto(pregunta["opciones"][1])
        boton2.actualizar_texto(pregunta["opciones"][2])
        boton3.actualizar_texto(pregunta["opciones"][3])
        boton4.actualizar_texto(pregunta["opciones"][4])
        print(jugador_actual)
# Crear los botones pasando una lambda que ejecuta la acción cuando se hace click
    boton1 = Boton(150, 350, 350, 75, pregunta["opciones"][1], COLOR_BLANCO, COBALT, BLUE, BLUE3, lambda: accion_boton(1))
    boton2 = Boton(150, 500, 350, 75, pregunta["opciones"][2], COLOR_BLANCO, COBALT, BLUE, BLUE3, lambda: accion_boton(2))
    boton3 = Boton(550, 350, 350, 75, pregunta["opciones"][3], COLOR_BLANCO, COBALT, BLUE, BLUE3, lambda: accion_boton(3))
    boton4 = Boton(550, 500, 350, 75, pregunta["opciones"][4], COLOR_BLANCO, COBALT, BLUE, BLUE3, lambda: accion_boton(4))
    botones = [boton1, boton2, boton3, boton4]

    while True:
        PANTALLA.blit(fondo, (0, 0))

        titulo_pregunta = Texto(pregunta["pregunta"], tamano_fuente=72, color=COLOR_BLANCO, posicion=(100, 100), centrar_horizontal=True, ancho_maximo=600)
        vidas_texto = Texto(f"vidas restantes: {str(vidas)}", tamano_fuente=72, color=RED1, posicion=(25, 25))
        
        vidas_texto.dibujar(PANTALLA)
        titulo_pregunta.dibujar(PANTALLA)

        for evento in pygame.event.get():
            if evento.type == pygame.QUIT:
                return "salir"
            
            for boton in botones:
                boton.manejar_evento(evento)

        for boton in botones:
            boton.dibujar(PANTALLA)

        pygame.display.flip()
