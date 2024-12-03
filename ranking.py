ranking = [
    {
        "Nombre Jugador": "Pruebas",
        "Puntaje": 30
    },
    {
        "Nombre Jugador": "Pruebas",
        "Puntaje": 28
    },
    {
        "Nombre Jugador": "Pruebas",
        "Puntaje": 25
    },
    {
        "Nombre Jugador": "Pruebas",
        "Puntaje": 20
    },
    ]

jugador_actual = {
    "Nombre Jugador": "",
    "Puntaje": 0
}

def guardar_puntuacion_ordenada(ranking: list, nombre: str, puntaje: int) -> None:
    '''
    ¿Qué hace? : Agrega un nuevo jugador al ranking con su puntaje, lo ordena en orden descendente por puntaje, y asegura que el ranking no exceda los 10 jugadores.
    ¿Qué recibe? :
        - ranking : list > Lista de diccionarios con los jugadores y sus puntajes actuales.
        - nombre : str > Nombre del jugador a agregar.
        - puntaje : int > Puntaje del jugador a agregar.
    ¿Qué retorna? : None
    '''
    nuevo_jugador = {"Nombre Jugador": nombre, "Puntaje": puntaje}
    ranking.append(nuevo_jugador)
    ranking.sort(key=lambda x: x["Puntaje"], reverse=True)
    if len(ranking) > 10:
        ranking.pop(-1)

def mostrar_ranking(ranking: list) -> None:
    '''
    ¿Qué hace? : Muestra el ranking actual en la consola, enumerando los jugadores y sus puntajes.
    ¿Qué recibe? :
        - ranking : list > Lista de diccionarios con los jugadores y sus puntajes.
    ¿Qué retorna? : None.
    '''
    print("El ranking actual:")
    for i, jugador in enumerate(ranking, start=1):
        print(f"{i}. {jugador['Nombre Jugador']} - Puntaje: {jugador['Puntaje']}")

def gestionar_ranking(ranking: list, nombre: str, puntaje: int) -> None:
    '''
    ¿Qué hace? : Gestiona el proceso de agregar un jugador al ranking y mostrar el ranking actualizado.
    ¿Qué recibe? :
        - ranking : list > Lista de diccionarios con los jugadores y sus puntajes actuales.
        - nombre : str > Nombre del jugador a agregar.
        - puntaje : int > Puntaje del jugador a agregar.
    ¿Qué retorna? : None.
    '''
    guardar_puntuacion_ordenada(ranking, nombre, puntaje)
    mostrar_ranking(ranking)



print("Ranking actualizado:")
mostrar_ranking(ranking)