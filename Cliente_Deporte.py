
from Deporte import Deporte
def probar_deporte():
    futbol = Deporte("Futbol")

    print("Agregar Real Madrid:", futbol.agregar_equipo("Real Madrid"))
    print("Agregar Barcelona:", futbol.agregar_equipo("Barcelona"))
    print("Agregar Atletico:", futbol.agregar_equipo("Atletico"))
    print("Agregar Real Madrid otra vez:", futbol.agregar_equipo("Real Madrid"))

    evento1 = Evento("Real Madrid", "Barcelona")
    evento2 = Evento("Atletico", "Sevilla")

    print("\nAgregar evento 1:", futbol.agregar_evento(evento1))
    print("Agregar evento 2:", futbol.agregar_evento(evento2))

    print("\nEquipos:")
    print(futbol.equipos)
    print("Cantidad de eventos:", len(futbol.eventos))

    print("\nEliminar Atletico:", futbol.eliminar_equipo("Atletico"))
    print("Equipos después:")
    print(futbol.equipos)

    print("Eliminar evento 1:", futbol.eliminar_evento(evento1))
    print("Cantidad de eventos después:", len(futbol.eventos))

