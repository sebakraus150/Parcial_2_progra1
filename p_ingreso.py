import pygame
from configs import *
from assets.boton import Boton
from assets.texto import Texto
from colores import *
from p_juego_iniciado import *
from ranking import jugador_actual

def mostrar_ventana_ingreso_nombre():
    '''
    ¿Qué hace? : Muestra una ventana donde el usuario puede ingresar su nombre, actualizarlo y confirmar para avanzar a la pantalla del juego.
    ¿Qué recibe? : None
    ¿Qué retorna? : None
    '''
    global pantalla_actual
    pantalla_actual = "ingreso_nombre"
    def accion_boton_aceptar():
        '''
        ¿Qué hace? : Guarda el nombre ingresado por el usuario en el diccionario "jugador_actual" y cambia la pantalla actual al juego
        ¿Qué recibe? : None
        ¿Qué retorna? : None
        '''
        global pantalla_actual
        
        if len(boton_aceptar.texto) == 0:
            jugador_actual["Nombre Jugador"] = "Alguien"
        else:
            jugador_actual["Nombre Jugador"] = nombre_usuario
        
        pantalla_actual = "juego"
    
    nombre_usuario = ""

    texto_ingreso = Texto("Ingresa tu nombre ", tamano_fuente=70, color=WHITE, posicion=(0,200), centrar_horizontal=True)
    nombre_ingresado = Boton(300,350,400,80,nombre_usuario, COLOR_BLANCO, COBALT, COBALT, COBALT)
    boton_aceptar = Boton(375, 550,250, 80, "Aceptar", COLOR_BLANCO, BLUE, COBALT , GREEN, accion_boton_aceptar)

    elemento_dibujar = [texto_ingreso,nombre_ingresado,boton_aceptar]

    # Bucle para que el jugador ingrese su nombre
    while True:
        PANTALLA.blit(fondo, (0, 0))

        for evento in pygame.event.get():
            if evento.type == pygame.QUIT:
                pygame.quit()
                exit()

            boton_aceptar.manejar_evento(evento)

            if evento.type == pygame.KEYDOWN:
                if evento.key == pygame.K_BACKSPACE:
                    nombre_usuario = nombre_usuario[:-1]
                else:
                    nombre_usuario += evento.unicode
                nombre_ingresado.actualizar_texto(nombre_usuario)


        for elemento in elemento_dibujar:
            elemento.dibujar(PANTALLA)

        pygame.display.flip()
        if pantalla_actual == "juego":
            return pantalla_actual