import random
import pygame
import sys
from configs import *
#from juego import screen




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


#2. Modificar vidas

def modificar_vidas(respuesta_correcta : str, respuesta_usuario : str):
    
    return respuesta_usuario == respuesta_correcta
    

# vidas_iniciales = 5

# respuesta_correcta = "Granate"

# respuesta_usuario = input("Ingrese su respuesta: ")

# vidas_restantes = modificar_vidas(vidas_iniciales, respuesta_correcta, respuesta_usuario)

# print(f"Te quedan {vidas_restantes} vidas")


#4.Pregunta aleatoria 

# preguntas = {
#     1:"¿Que selección ganó el campeonato del mundo 2022?",

#     2:"¿Cuál es el equipo que ganó más copas libertadores en argentina?",

#     3:"¿Cuál es el equipo con más participaciones en la historia de la copa sudamericana?"
# }



def pregunta_aleatoria(preguntas : dict, dificultad: int=0):

    pregunta_seleccionada = random.choice(preguntas[dificultad])

    return pregunta_seleccionada



# print(pregunta_aleatoria(preguntas))

#7. Agregar dato
# def agregar_dato(diccionario_origen, diccionario_destino, clave):
#     """
#     Agrega un dato específico de un diccionario a otro, usando una clave.

#     Args:
#     - diccionario_origen (dict): El diccionario desde el cual se tomará el dato.
#     - diccionario_destino (dict): El diccionario al cual se agregará el dato.
#     - clave (str): La clave del dato que se tomará del diccionario origen.
    
#     Returns:
#     - dict: El diccionario destino actualizado con el nuevo dato.
#     """
#     if clave in diccionario_origen:

#         diccionario_destino[clave] = diccionario_origen[clave]

#     else:
        
#         print(f"La clave '{clave}' no existe en el diccionario de origen.")
        
#     return diccionario_destino

# # Ejemplo de uso:
# diccionario_origen = {"nombre": "Thiago", "edad": 22}
# diccionario_destino = {"ciudad": "Lanús"}

# # Agregar dato de diccionario_origen a diccionario_destino
# diccionario_destino = agregar_dato(diccionario_origen, diccionario_destino, "nombre")

# print(diccionario_destino)

#8. Mostrar dato
# def mostrar_dato(diccionario : dict, clave) -> None:

#     if clave in diccionario:

#         print(diccionario[clave])
    
#     else:
        
#         print("La clave no existe")
# #9. Obtener dato
# def obtener_dato(diccionario : dict, clave):

#     if clave in diccionario:
        
#         return(diccionario[clave])
    
#     else:
        
#         return None

#10. Modificar dato

# def modificar_dato(diccionario : dict, diccionario_modificado : dict, clave):

#     if clave in diccionario and clave in diccionario_modificado:
        
#         diccionario[clave] = diccionario_modificado[clave]

#         return diccionario[clave]

#     else:
        
#         print("La clave no se encontró en uno de los diccionarios")
#         return None



#12. Guardar puntuaciones
#13. Ordenar puntuacion
#14. Mostrar ranking

# ranking = []

# def guardar_puntuacion_ordenada(ranking: list, nombre: str, puntaje: int) -> None:
#     nuevo_jugador = {"Nombre Jugador": nombre, "Puntaje": puntaje}
#     ranking.append(nuevo_jugador)
#     ranking.sort(key=lambda x: x["Puntaje"], reverse=True)
#     if len(ranking) > 10:
#         ranking.pop(-1)

# def mostrar_ranking(ranking: list) -> None:
#     print("El ranking actual:")
#     for i, jugador in enumerate(ranking, start=1):
#         print(f"{i}. {jugador['Nombre Jugador']} - Puntaje: {jugador['Puntaje']}")

# def gestionar_ranking(ranking: list, nombre: str, puntaje: int) -> None:
#     guardar_puntuacion_ordenada(ranking, nombre, puntaje)
#     mostrar_ranking(ranking)

# print("Ranking actualizado:")
# mostrar_ranking(ranking)

#15 ingresar nombre de usuario
# def ingresar_nombre_de_usuario(Name : str) -> str:

#     Name = input("Ingrese su nombre de usuario: ")

#     return Name



#17 mostrar menu
# def mostrar_menu()
#19.verificar estado del juego
# def verificar_estado_juego(vidas : int, puntuación: int, puntuacion_ganadora : int) -> bool:

#     if vidas <= 0:

#         print("GAME OVER")
        
#         return False

#     if puntuación >= puntuacion_ganadora:

#         print("GANASTE")

#         return False

#     return True



#20.jugar juego

    
def jugar_preguntas(preguntas, vidas):
    """
    Función principal para manejar las preguntas del juego según la dificultad.
    
    :param preguntas: list, Lista de preguntas dividida por niveles de dificultad.
    :param vidas: int, Número inicial de vidas del jugador.
    """
    niveles = ["facil", "medio", "dificil"]
    nivel_actual = 0  
    pregunta_actual = 0  

    while vidas > 0 and nivel_actual < len(niveles):
        nivel = niveles[nivel_actual]
        pregunta = preguntas[nivel_actual][pregunta_actual]

        print(f"Nivel {nivel.upper()}: {pregunta['pregunta']}")
        for opcion, texto in pregunta['opciones'].items():
            print(f"{opcion}: {texto}")

        
        try:
            respuesta = int(input("Tu respuesta (elige un número): "))
        except ValueError:
            print("Por favor, ingresa un número válido.")
            continue

        
        if respuesta == pregunta['respuesta_correcta']:
            print("Respuesta correcta")
        else:
            vidas -= 1
            print(f"Respuesta incorrecta. Te quedan {vidas} vidas.")

        
        pregunta_actual += 1
        if pregunta_actual >= len(preguntas[nivel_actual]):  
            pregunta_actual = 0  
            nivel_actual += 1  

    
    if vidas > 0:
        print("Felicidades, completaste todas las preguntas")
    else:
        print("Te quedaste sin vidas. Fin del juego.")


#12. Guardar puntuaciones
#13. Ordenar puntuacion
#14. Mostrar ranking

# ranking = []

# def guardar_puntuacion_ordenada(ranking: list, nombre: str, puntaje: int) -> None:
#     nuevo_jugador = {"Nombre Jugador": nombre, "Puntaje": puntaje}
#     ranking.append(nuevo_jugador)
#     ranking.sort(key=lambda x: x["Puntaje"], reverse=True)
#     if len(ranking) > 10:
#         ranking.pop(-1)

# def mostrar_ranking(ranking: list) -> None:
#     print("El ranking actual:")
#     for i, jugador in enumerate(ranking, start=1):
#         print(f"{i}. {jugador['Nombre Jugador']} - Puntaje: {jugador['Puntaje']}")

# def gestionar_ranking(ranking: list, nombre: str, puntaje: int) -> None:
#     guardar_puntuacion_ordenada(ranking, nombre, puntaje)
#     mostrar_ranking(ranking)

# print("Ranking actualizado:")
# mostrar_ranking(ranking)


def guardar_estadisticas(nombre : str, puntos : int):

    with open("Estadisticas.txt", "w") as archivo:

        archivo.write(f"{nombre}\n")

        archivo.write(f"{puntos}\n")


def leer_estadisticas():

    try:

        with open("Estadisticas.txt", "r") as archivo:

            nombre = str(archivo.readline().strip())

            puntos = int(archivo.readline().strip())
        
        return nombre, puntos
    
    except FileNotFoundError:

        return 3, 0, 1

