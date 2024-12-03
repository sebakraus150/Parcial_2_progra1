
import random

#region Modificar puntajes del jugador

# #1. Modificar puntaje del jugador

# respuesta = input("Ingrese su respuesta: ")

# def modificar_puntaje(puntaje : int, respuesta_correcta : str):

        

#         if respuesta_correcta:

#             puntaje += 1

#         else:

#             puntaje -= 1


#             return puntaje


# puntaje_inicial = 5

# respuesta = True

# puntaje_actualizado = modificar_puntaje(puntaje_inicial, respuesta)

# print(f"Puntaje actual {puntaje_actualizado}")

# respuesta = False

# puntaje_actualizado = modificar_puntaje(puntaje_inicial, respuesta)

# print(f"Puntaje actual {puntaje_actualizado}")

#endregion

#region Modificar vidas

#2. Modificar vidas

# def modificar_vidas(vidas : int, respuesta_correcta : str, respuesta_usuario : str):
    
#     if respuesta_usuario != respuesta_correcta:

#             vidas -= 1

#             return vidas
    

# vidas_iniciales = 5

# respuesta_correcta = "Granate"

# respuesta_usuario = input("Ingrese su respuesta: ")

# vidas_restantes = modificar_vidas(vidas_iniciales, respuesta_correcta, respuesta_usuario)

# print(f"Te quedan {vidas_restantes} vidas")

#region preguntas aleatorias

#4.Pregunta aleatoria 

# preguntas = {
#     1:"¿Que selección ganó el campeonato del mundo 2022?",

#     2:"¿Cuál es el equipo que ganó más copas libertadores en argentina?",

#     3:"¿Cuál es el equipo con más participaciones en la historia de la copa sudamericana?"
# }



# def pregunta_aleatoria(preguntas : dict):

#     pregunta_random = random.choice(list(preguntas.keys()))

#     return preguntas[pregunta_random]



# print(pregunta_aleatoria(preguntas))

#endregion

#7. Agregar dato
#8. Mostrar dato
#9. Obtener dato
#10. Modificar dato
#11.Terminar Juego
#12. Guardar puntuación
#13. ordenar puntuaciones
#14 mostrar ranking
#15 ingresar nombre de usuario
#17 mostrar menu
#19.verificar estado del juego
#20.jugar juego




#region sumar aciertos
# def sumar_aciertos(preguntas : dict, respuestas : int):

#     aciertos = 0

#     for pregunta, respuesta_correcta in preguntas.items():

#         if respuestas.get(pregunta) == respuesta_correcta:

#             aciertos += 1

#     return aciertos



# preguntas = {
#     "¿Cuál es la capital de Francia?": "París",
#     "¿Cuántos planetas hay en el sistema solar?": "8",
#     "¿De qué color es el cielo?": "Azul"
# }

# respuestas = {
#     "¿Cuál es la capital de Francia?": "París",
#     "¿Cuántos planetas hay en el sistema solar?": "9",  
#     "¿De qué color es el cielo?": "Azul"
# }

# aciertos = sumar_aciertos(preguntas, respuestas)
# print(f"La cantidad de aciertos es {aciertos}")

#endregion


#region modificar puntajes

# def modificae_puntajes(puntaje : int, acierto = bool, Aumento_de_puntaje = +10, penalizacion_por_fallar = -5):

#     if acierto == True:

#         puntaje += Aumento_de_puntaje
    
#     else:

#         puntaje -= penalizacion_por_fallar

    
#     #EVITAMOS PUNTOS NEGATIVOS 

#     if puntaje < 0:

#         puntaje = 0


#     return puntaje

#endregion 


#region Mostrar dificultad

def mostrar_dif_preguntas(preguntas : dict):

    niveles = ["Fácil", "Media", "Difícil"]

    for i in range(len(preguntas)):

        print(f"Dificultad: {niveles[i]}")

    for j in range(len(preguntas[i])):

        print(preguntas[i][j]["pregunta"])

        print(preguntas[i][j]["opciones"])
        
        print()
