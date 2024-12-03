import pygame

class Texto:
    def __init__(self, texto, tamano_fuente=36, color=(255, 255, 255), posicion=(0, 0), ruta_fuente=None, centrar_horizontal=False, ancho_maximo=None):
        '''
        ¿Qué hace? : Inicializa un objeto de texto con propiedades de estilo y posicionamiento, permitiendo opciones como centrado horizontal y ajuste automático de líneas según un ancho máximo.
        ¿Qué recibe? :
            - texto : str > Contenido del texto.
            - tamano_fuente : int > Tamaño de la fuente (por defecto 36).
            - color : tuple(int, int, int) > Color RGB del texto (por defecto blanco).
            - posicion : tuple(int, int) > Coordenadas (x, y) de inicio del texto.
            - ruta_fuente : str > Ruta a un archivo de fuente TTF (opcional, usa fuente predeterminada si es None).
            - centrar_horizontal : bool > Si True, el texto se centra horizontalmente.
            - ancho_maximo : int > Ancho máximo para dividir el texto en líneas (opcional).
        ¿Qué retorna? : None
        '''

        self.texto = texto
        self.tamano_fuente = tamano_fuente
        self.color = color
        self.posicion = posicion

        # Si no se proporciona ruta_fuente, usar la fuente predeterminada de Pygame
        if ruta_fuente is None:
            self.fuente = pygame.font.Font(None, tamano_fuente)
        else:
            self.fuente = pygame.font.Font(ruta_fuente, tamano_fuente)

        self.centrar_horizontal = centrar_horizontal
        self.ancho_maximo = ancho_maximo
        self.lineas = self.ajustar_texto()

    def ajustar_texto(self):
        '''
        ¿Qué hace? : Divide el texto en líneas ajustadas para que no superen el ancho máximo especificado.
        ¿Qué recibe? : No recibe parámetros externos, utiliza los atributos de la clase.
        ¿Qué retorna? : lineas -> list[str] > Lista de líneas ajustadas al ancho máximo.
        '''
        if not self.ancho_maximo:
            return [self.texto]  # Si no hay limite de ancho, devuelve el texto sin cambios
        
        palabras = self.texto.split(" ")
        lineas = []
        linea_actual = ""

        for palabra in palabras:
            # Prueba agregar la palabra actual a la linea en construcción
            linea_prueba = linea_actual + (" " if linea_actual else "") + palabra
            if self.fuente.size(linea_prueba)[0] <= self.ancho_maximo:
                linea_actual = linea_prueba
            else:
                lineas.append(linea_actual)  # Linea completa
                linea_actual = palabra  # Nueva linea con la palabra actual

        if linea_actual:
            lineas.append(linea_actual)  # Agrega la última linea

        return lineas

    def establecer_texto(self, nuevo_texto):
        '''
        ¿Qué hace? : Actualiza el texto contenido en el objeto y recalcula las lineas ajustadas.
        ¿Qué recibe? : 
            - nuevo_texto : str > El nuevo texto que reemplazará al actual.
        ¿Qué retorna? : None
        '''
        self.texto = nuevo_texto
        self.lineas = self.ajustar_texto()

    def centrar_texto_horizontal(self, superficie):
        '''
        ¿Qué hace? : Calcula las posiciones necesarias para centrar horizontalmente cada linea del texto en una superficie dada.
        ¿Qué recibe? : 
            - superficie : pygame.Surface > Superficie donde se dibujará el texto.
        ¿Qué retorna? : 
            - posiciones : list[tuple(int, int)] > Lista de coordenadas (x, y) para cada linea centrada.
        '''
        if not self.lineas:
            return
        
        # Calcula el centro para cada linea
        ancho_superficie = superficie.get_rect().width
        x_centrada = lambda linea: (ancho_superficie - self.fuente.size(linea)[0]) // 2

        # Ajusta las posiciones de cada linea
        posiciones = [(x_centrada(linea), self.posicion[1] + i * self.fuente.size(linea)[1]) for i, linea in enumerate(self.lineas)]
        return posiciones

    def dibujar(self, superficie):
        '''
        ¿Qué hace? : Dibuja el texto linea por linea en una superficie, con opciones para posicionamiento manual o centrado horizontal.
        ¿Qué recibe? : 
            - superficie : pygame.Surface > Superficie donde se dibujará el texto.
        ¿Qué retorna? : No retorna nada explícitamente, dibuja el texto en la superficie.
        '''

        desplazamiento_y = 0
        posiciones = self.centrar_texto_horizontal(superficie) if self.centrar_horizontal else None

        for i, linea in enumerate(self.lineas):
            superficie_texto = self.fuente.render(linea, True, self.color)
            if self.centrar_horizontal:
                posicion = posiciones[i]  # Usar las posiciones calculadas para centrar
            else:
                posicion = (self.posicion[0], self.posicion[1] + desplazamiento_y)
            
            superficie.blit(superficie_texto, posicion)
            desplazamiento_y += self.fuente.size(linea)[1]  # Incrementa el desplazamiento según la altura de la linea
