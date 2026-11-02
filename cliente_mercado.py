"""pruba de mercado"""
from mercado import Mercado
from evento import Evento
class Deporte: # cambiar por la clase Deporte del archivo deporte.py
    """Clase que representa un deporte"""
    def __init__(self, nombre: str):
        self._nombre = nombre

    @property
    def nombre(self):
        """Devuelve el nombre del deporte"""
        return self._nombre

deporte_futbol = Deporte("futbol")
deporte_tenis = Deporte("tenis")
deporte_baloncesto = Deporte("baloncesto")
deporte_boxeo = Deporte("boxeo")

mercado_futbol = Mercado({"ganador_equipo_1": 1.5, "ganador_equipo_2": 2.5, "empate": 3.0,\
                           "total_goles_mas_2.5": 1.8, "total_goles_menos_2.5": 2.0})

mercado_tenis = Mercado({"ganador_jugador_1": 1.7, "ganador_jugador_2": 2.1,\
                          "total_sets_mas_3.5": 1.9, "total_sets_menos_3.5": 1.9})

mercado_baloncesto = Mercado({"ganador_equipo_1": 1.6, "ganador_equipo_2": 2.4,\
                               "total_puntos_mas_200.5": 1.7, "total_puntos_menos_200.5": 2.0})

mercado_boxeo = Mercado({"ganador_boxeador_1": 1.8, "ganador_boxeador_2": 2.0,\
                          "total_asaltos_mas_10.5": 1.9, "total_asaltos_menos_10.5": 1.9})

print(mercado_futbol.mostrar_opciones())
print(mercado_tenis.mostrar_opciones())
print(mercado_baloncesto.mostrar_opciones())
print(mercado_boxeo.mostrar_opciones())

evento_futbol = Evento(deporte_futbol, "equipo_1", "equipo_2", "2023-06-01", mercado_futbol)

print(evento_futbol.estado)
evento_futbol.estado = "en juego"
print(evento_futbol.estado)