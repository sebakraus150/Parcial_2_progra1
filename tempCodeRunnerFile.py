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
        print(tiempo_inicio)