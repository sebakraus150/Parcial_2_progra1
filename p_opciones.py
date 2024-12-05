import pygame
from configs import *
from assets.boton import Boton
from assets.texto import Texto
from colores import *

def abrir_ventana_edicion(titulo, variable_objetivo,key):
    """
    Hace: Abre una ventana para ingresar un valor con un botón como contenedor del texto y un botón de aceptar.
    Recibe:
        - titulo: str, título o descripción de la variable a editar.
        - variable_objetivo: dict, referencia al diccionario donde se guardará el valor.
    Devuelve: None
    """
    ventana_abierta = True
    nombre_ingresado = ""
    def aceptar():
        """
        Guarda el texto ingresado en la variable objetivo y cierra la ventana.
        """
        variable_objetivo[key] = nombre_ingresado
        nonlocal  ventana_abierta
        ventana_abierta = False

    texto_titulo = Texto(titulo, tamano_fuente=72, color=COLOR_BLANCO, posicion=(0, 200), centrar_horizontal=True)
    boton_texto = Boton(300, 350, 400, 80, nombre_ingresado, COLOR_BLANCO, COBALT, COBALT, COBALT)
    boton_aceptar = Boton(375, 500, 250, 80, "Aceptar", COLOR_BLANCO, BLUE, COBALT, GREEN, aceptar)

    elementos = [texto_titulo, boton_texto, boton_aceptar]

    while ventana_abierta:
        PANTALLA.blit(fondo, (0, 0))

        for evento in pygame.event.get():
            if evento.type == pygame.QUIT:
                pygame.quit()
                exit()

            if evento.type == pygame.KEYDOWN:
                if evento.key == pygame.K_BACKSPACE:
                    nombre_ingresado = nombre_ingresado[:-1]
                elif evento.key == pygame.K_RETURN:
                    aceptar()
                elif evento.key >= pygame.K_0 and evento.key <= pygame.K_9:
                    nombre_ingresado += evento.unicode
                    
                boton_texto.actualizar_texto(nombre_ingresado)

            for elemento in elementos:
                if isinstance(elemento, Boton):
                    elemento.manejar_evento(evento)

        for elemento in elementos:
            elemento.dibujar(PANTALLA)

        pygame.display.flip()

# Variables globales para almacenar los valores editados
valores_configuracion = {
    "puntos_perdidos": 1,
    "vidas":5,
    "tiempo_preguntas": 20,
}

def pantalla_opciones():
    def boton_menu_principal():
        global pantalla_actual
        pantalla_actual = "menu"
    
    def editar_puntos():
        abrir_ventana_edicion("Puntos perdidos por respuesta incorrecta", valores_configuracion,"puntos_perdidos")

    def editar_vidas():
        abrir_ventana_edicion("Número de vidas", valores_configuracion, "vidas")

    def editar_tiempo():
        abrir_ventana_edicion("Tiempo entre preguntas (segundos)", valores_configuracion,"tiempo_preguntas")

    texto_puntos = Boton(100, 200, 500, 50, "Puntos perdidos por respuesta incorrecta", WHITE, GREEN3, GREEN3, GREEN3)
    boton_puntos = Boton(750, 200, 100, 50, "Editar", WHITE, GREEN, BLUE, RED1, editar_puntos)

    texto_vidas = Boton(100, 300, 500, 50, "Número de vidas", WHITE, GREEN3, GREEN3, GREEN3)
    boton_vidas = Boton(750, 300, 100, 50, "Editar", WHITE, GREEN, BLUE, RED1, editar_vidas)

    texto_tiempo = Boton(100, 400, 500, 50, "Tiempo entre preguntas", WHITE, GREEN3, GREEN3, GREEN3)
    boton_tiempo = Boton(750, 400, 100, 50, "Editar", WHITE, GREEN, BLUE, RED1, editar_tiempo)

    boton_agregar = Boton(300, 525, 450, 50, "Agregar Pregunta", WHITE, GREEN, BLUE, RED1, boton_menu_principal)

    boton_confirmar = Boton(300, 650, 150, 50, "Confirmar", WHITE, GREEN, BLUE, RED1, boton_menu_principal)
    boton_volver = Boton(600, 650, 150, 50, "Salir", WHITE, GREEN, BLUE, RED1, boton_menu_principal)

    botones_opciones = [texto_puntos,boton_puntos,texto_vidas,boton_vidas,texto_tiempo,boton_tiempo,boton_agregar,boton_confirmar,boton_volver]

    titulo = Texto("CONFIGURACIONES", tamano_fuente=100, color=COLOR_BLANCO, posicion=(0, 50), centrar_horizontal=True)

    global pantalla_actual
    pantalla_actual = "opciones"

    while True:
        PANTALLA.blit(fondo, (0, 0))

        if pantalla_actual != "opciones":
            return pantalla_actual

        for evento in pygame.event.get():
            if evento.type == pygame.QUIT:
                pygame.quit()
                exit()
            for boton in botones_opciones:
                    boton.manejar_evento(evento)
            
        for boton in botones_opciones:
            boton.dibujar(PANTALLA)
        
        titulo.dibujar(PANTALLA)

        pygame.display.update()
