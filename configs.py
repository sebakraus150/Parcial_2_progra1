import pygame
# Pantalla

ANCHO = 1000
ALTO = 800

PANTALLA = pygame.display.set_mode((ANCHO, ALTO))

pantalla_actual = "menu"

# Cargar la imagen de fondo
fondo = pygame.image.load("segundo_parcial/assets/imgs/fondo-campo.jpg")
fondo = pygame.transform.scale(fondo, (ANCHO, ALTO))

# Vidas
vidas = 3