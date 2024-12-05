import pygame
from configs import *
from assets.boton import Boton
from assets.texto import Texto
from colores import *
from preguntas import preguntas # Este es mi diccionario de preguntas 
from funciones_base import *
from p_ranking import *
from ranking import *
from p_opciones import *
import copy # Sirve para hacer una copia del diccionario de preguntas

def pantalla_juego():
    '''
    ¿Qué hace? : Configura y muestra la pantalla principal del juego, incluyendo una pregunta aleatoria, botones con respuestas posibles y el contador de vidas. Controla las acciones del jugador.
    ¿Qué recibe? : No recibe parámetros directamente.
    ¿Qué retorna? : None
    '''
    preguntas_copia = copy.deepcopy(preguntas)
    global pantalla_actual
    pantalla_actual = "juego"

    global jugador_actual

    global vidas
    vidas = int(valores_configuracion["vidas"])

    global contador_aciertos
    contador_aciertos = 0

    global pregunta
    pregunta = pregunta_aleatoria(preguntas_copia,0)

    global dificultad
    dificultad = 0 

    global puntaje
    puntaje = 0
    tiempo_inicio = pygame.time.get_ticks()  # Tiempo inicial en milisegundos
    tiempo_limite = int(valores_configuracion["tiempo_preguntas"]) * 1000
    def accion_boton(opcion):
        '''
        ¿Qué hace? : Verifica si la respuesta seleccionada es correcta o incorrecta. Modifica el número de vidas del jugador y cambia a la pantalla de ranking si las vidas llegan a 0.
        ¿Qué recibe? : 
            - opcion : int, la opción seleccionada por el jugador.
        ¿Qué retorna? : None
        '''

        global pregunta
        global vidas
        global dificultad
        global puntaje
        global ranking
        
        global tiempo_inicio
        tiempo_inicio = pygame.time.get_ticks()

        if modificar_vidas(pregunta["respuesta_correcta"], opcion):
            global contador_aciertos
            puntaje = modificar_puntaje(puntaje, contador_aciertos)
            contador_aciertos += 1
            eliminar_pregunta(preguntas_copia,dificultad, pregunta)

            if contador_aciertos >= 15:
                global jugador_actual
                jugador_actual["Puntaje"] = puntaje
                global pantalla_actual
                guardar_puntuacion_ordenada(ranking, jugador_actual)
                pantalla_actual = "ranking"
            elif contador_aciertos >= 10:
                dificultad = 2
            elif contador_aciertos >= 5:
                dificultad = 1
        else:
            puntaje = modificar_puntaje(puntaje,contador_aciertos, False,int(valores_configuracion["puntos_perdidos"]))
            vidas -= 1
        pregunta = pregunta_aleatoria(preguntas_copia,dificultad)
        
        jugador_actual["Puntaje"] = puntaje

        if vidas < 1:
            guardar_puntuacion_ordenada(ranking, jugador_actual)
            pantalla_actual = "ranking"

        boton1.actualizar_texto(pregunta["opciones"][1])
        boton2.actualizar_texto(pregunta["opciones"][2])
        boton3.actualizar_texto(pregunta["opciones"][3])
        boton4.actualizar_texto(pregunta["opciones"][4])

# Crear los botones pasando una lambda que ejecuta la acción cuando se hace click
    boton1 = Boton(150, 350, 350, 75, pregunta["opciones"][1], COLOR_BLANCO, COBALT, BLUE, BLUE3, lambda: accion_boton(1))
    boton2 = Boton(150, 500, 350, 75, pregunta["opciones"][2], COLOR_BLANCO, COBALT, BLUE, BLUE3, lambda: accion_boton(2))
    boton3 = Boton(550, 350, 350, 75, pregunta["opciones"][3], COLOR_BLANCO, COBALT, BLUE, BLUE3, lambda: accion_boton(3))
    boton4 = Boton(550, 500, 350, 75, pregunta["opciones"][4], COLOR_BLANCO, COBALT, BLUE, BLUE3, lambda: accion_boton(4))
    botones = [boton1, boton2, boton3, boton4]

    while True:
        PANTALLA.blit(fondo, (0, 0))

        tiempo_transcurrido = pygame.time.get_ticks() - tiempo_inicio

        if tiempo_transcurrido >= tiempo_limite:
            puntaje = modificar_puntaje(puntaje, contador_aciertos, False, int(valores_configuracion["puntos_perdidos"]))
            vidas -= 1
            pregunta = pregunta_aleatoria(preguntas_copia, dificultad)
            tiempo_inicio = pygame.time.get_ticks()
            if vidas < 1:
                guardar_puntuacion_ordenada(ranking, jugador_actual)
                pantalla_actual = "ranking"

        titulo_pregunta = Texto(pregunta["pregunta"], tamano_fuente=72, color=COLOR_BLANCO, posicion=(100, 100), centrar_horizontal=True, ancho_maximo=600)
        vidas_texto = Texto(f"VIDAS: {str(vidas)}", tamano_fuente=72, color=RED1, posicion=(25, 25))
        puntos_texto = Texto(f"PUNTOS: {str(puntaje)}", tamano_fuente=72, color=COLOR_BLANCO, posicion=(700, 25))
        tiempo_restante = max(0, (tiempo_limite - tiempo_transcurrido) // 1000)# Convertir a segundos
        timer_texto = Texto(f"{tiempo_restante} S", tamano_fuente=72, color=COLOR_BLANCO, posicion=(0, 25), centrar_horizontal=True)
        textos_juego = [titulo_pregunta,vidas_texto,puntos_texto, timer_texto]
        
        
        for evento in pygame.event.get():
            if evento.type == pygame.QUIT:
                return "salir"
            
            for boton in botones:
                boton.manejar_evento(evento)

        for boton in botones:
            boton.dibujar(PANTALLA)
        
        for texto in textos_juego:
            texto.dibujar(PANTALLA)

        pygame.display.flip()
    
        if pantalla_actual == "ranking":
                return pantalla_actual
