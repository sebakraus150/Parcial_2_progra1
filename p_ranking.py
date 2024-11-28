import pygame
from configs import *
from assets.boton import Boton
from assets.texto import Texto
from colores import *
from ranking import ranking

def pantalla_ranking():
    def botonazo():
        from p_menu_principal import menu_principal
        global pantalla_actual
        pantalla_actual = menu_principal()

        
    boton_volver = Boton(ANCHO // 2 - 100, ALTO - 100, 200, 50, "Volver al menú", COLOR_BLANCO, COLOR_GRIS, COLOR_CELESTE, COLOR_AMARILLO, botonazo)

    while True:
        PANTALLA.blit(fondo, (0, 0))
        texto = Texto("Ranking Top 10", tamano_fuente=72, color=COLOR_BLANCO, posicion=(100, 100), centrar_horizontal=True)
        texto.dibujar(PANTALLA)
        
        y_posicion = 150
        for i, jugador in enumerate(ranking):
            if i > 0:
                y_posicion += 50

            info_jugador = f"{i+1}. {jugador['Nombre Jugador']} - {jugador['Puntaje']} pts"
            texto_jugador = Texto(info_jugador, 48, COLOR_BLANCO, posicion=(0, y_posicion), centrar_horizontal=True)
            texto_jugador.dibujar(PANTALLA)

        boton_volver.dibujar(PANTALLA)

        for evento in pygame.event.get():
            if evento.type == pygame.QUIT:
                return "salir"
            
            boton_volver.manejar_evento(evento)

        pygame.display.flip()

