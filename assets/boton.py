import pygame
from configs import *
from colores import *

class Boton:
    def __init__(self, x, y, ancho, alto, texto, color_texto, color_normal, color_hover, color_click, accion=None):
        '''
        ¿Qué hace? : Representa un botón interactivo con texto, que responde a eventos del mouse y ejecuta una acción específica cuando se presiona.
        ¿Qué recibe? : 
            - x : int > Posición X del botón.
            - y : int > Posición Y del botón.
            - ancho : int > Ancho del botón.
            - alto : int > Altura del botón.
            - texto : str > Texto a mostrar dentro del botón.
            - color_texto : tuple(int, int, int) > Color RGB del texto del botón.
            - color_normal : tuple(int, int, int) > Color RGB del botón en estado normal.
            - color_hover : tuple(int, int, int) > Color RGB del botón al pasar el mouse por encima.
            - color_click : tuple(int, int, int) > Color RGB del botón al hacer clic.
            - accion : callable > Función que se ejecuta al presionar el botón (opcional).
        ¿Qué retorna? : None
        '''

        self.rect = pygame.Rect(x, y, ancho, alto)
        self.texto = texto
        self.color_texto = color_texto
        self.color_normal = color_normal
        self.color_hover = color_hover
        self.color_click = color_click
        self.accion = accion
        self.color_actual = color_normal
        self.fuente = pygame.font.Font(None, 36)
        self.click_iniciado = False  # Verifica donde inicia el click

    def ajustar_texto(self):
        """
        Ajusta el texto del botón para que no exceda el ancho del botón.
        Si es necesario, agrega '...' al final.
        """
        texto = self.texto
        while self.fuente.size(texto)[0] > self.rect.width - 10:
            texto = texto[:-1]
        if texto != self.texto:
            texto = texto[:-3] + "..."
        return texto

    def dibujar(self, pantalla):
        '''
        ¿Qué hace? : Dibuja el botón en la pantalla con el color correspondiente al estado actual (normal, hover, o clic) y renderiza el texto centrado.
        ¿Qué recibe? :
            - pantalla : pygame.Surface > Superficie en la que se dibuja el botón.
        ¿Qué retorna? : None
        
        '''
        posicion_mouse = pygame.mouse.get_pos()

        # Determinar el color según el estado
        if self.rect.collidepoint(posicion_mouse):
            if self.click_iniciado and pygame.mouse.get_pressed()[0]:
                color_actual = self.color_click
            else:
                color_actual = self.color_hover
        else:
            color_actual = self.color_normal

        pygame.draw.rect(pantalla, color_actual, self.rect)

        texto_ajustado = self.ajustar_texto()
        superficie_texto = self.fuente.render(texto_ajustado, True, self.color_texto)
        texto_rect = superficie_texto.get_rect(center=self.rect.center)
        pantalla.blit(superficie_texto, texto_rect)


    def manejar_evento(self, evento):
        '''
        ¿Qué hace? : Maneja eventos del mouse para detectar si el botón fue presionado y ejecutar su acción asociada.
        ¿Qué recibe? :
            - evento : pygame.event.Event > Evento de Pygame que representa una interacción del mouse.
        ¿Qué retorna? : None
        '''
        if evento.type == pygame.MOUSEBUTTONDOWN and evento.button == 1:
            # Verificar si el click comenzó dentro del botón
            if self.rect.collidepoint(evento.pos):
                self.click_iniciado = True

        elif evento.type == pygame.MOUSEBUTTONUP and evento.button == 1:
            # Verificar si el click se soltó dentro del botón y si comenzó dentro del botón
            if self.click_iniciado and self.rect.collidepoint(evento.pos):
                if self.accion:
                    self.accion()
            # Reiniciar el estado del click
            self.click_iniciado = False
    def actualizar_texto(self, nuevo_texto):
        self.texto = nuevo_texto

