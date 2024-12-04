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
    def accion_boton_aceptar():
        '''
        ¿Qué hace? : Guarda el nombre ingresado por el usuario en el diccionario "jugador_actual" y cambia la pantalla actual al juego
    ¿Qué recibe? : None
    ¿Qué retorna? : None
        '''
        global pantalla_actual
        jugador_actual["Nombre Jugador"] = nombre_usuario
        pantalla_actual = pantalla_juego()
    
    nombre_usuario = ""
    texto_ingreso = Texto("Ingresa tu nombre ", tamano_fuente=48, color=WHITE, posicion=(0,300), centrar_horizontal=True)
    rectangulo = pygame.Rect(ANCHO // 2 - 90, ALTO // 2, 200, 40)  # Rectángulo para ingresar el nombre
    
    boton_aceptar = Boton(350, 550,250, 80, "Aceptar", GREEN, BLUE, (0, 0, 128) , BLACK, accion_boton_aceptar)
    nombre_ingresado = Boton(350,350,250,80,nombre_usuario, COLOR_BLANCO, COBALT, COBALT, COBALT)

    # Bucle para que el jugador ingrese su nombre
    while True:
        for evento in pygame.event.get():
            if evento.type == pygame.QUIT:
                pygame.quit()
                exit()

            boton_aceptar.manejar_evento(evento)

            if evento.type == pygame.KEYDOWN:
                if evento.key == pygame.K_RETURN:  # Si presiona Enter
                    print(nombre_usuario)
                elif evento.key == pygame.K_BACKSPACE:
                    nombre_usuario = nombre_usuario[:-1]
                else:
                    nombre_usuario += evento.unicode
                nombre_ingresado.actualizar_texto(nombre_usuario)

        # Dibujar elementos en pantalla
        PANTALLA.blit(fondo, (0, 0))
        texto_ingreso.dibujar(PANTALLA)
        
        pygame.draw.rect(PANTALLA, WHITE, rectangulo, 2)  # Dibujamos el rectángulo de texto
        nombre_ingresado.dibujar(PANTALLA)

        # Mostrar botón de aceptar
        boton_aceptar.dibujar(PANTALLA)
        
        pygame.display.update()