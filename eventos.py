"""Archivo encargado de la clase Evento"""
from deporte import Deporte
from mercado import Mercado

class Evento:
    """Clase que representa un evento deportivo"""
    def __init__(self, deporte: Deporte, equipo_1: str, equipo_2: str, fecha: str, mercado: Mercado, estado: str="programado", resultado: str=""):
        self._deporte = deporte
        self._equipo_1 = equipo_1
        self._equipo_2 = equipo_2
        self._fecha = fecha
        self._estado = estado
        self._resultado = resultado
        self._mercado = mercado

    @property
    def deporte(self):
        """Devuelve el deporte del evento"""
        return self._deporte

    @property
    def equipo_1(self):
        """Devuelve el primer equipo del evento"""
        return self._equipo_1

    @property
    def equipo_2(self):
        """Devuelve el segundo equipo del evento"""
        return self._equipo_2

    @property
    def fecha(self):
        """Devuelve la fecha del evento"""
        return self._fecha
    @fecha.setter
    def fecha(self, nueva_fecha):
        self._fecha = nueva_fecha

    @property
    def estado(self):
        """Devuelve el estado del evento"""
        return self._estado
    @estado.setter
    def estado(self, nuevo_estado:str):
        if nuevo_estado not in ["programado", "en juego", "finalizado"]:
            raise ValueError("El estado debe ser 'programado', 'en juego' o 'finalizado'")
        self._estado = nuevo_estado

    @property
    def resultado(self):
        """Devuelve el resultado del evento"""
        return self._resultado
    @resultado.setter
    def resultado(self, nuevo_resultado: str):
        if self._estado != "finalizado":
            raise ValueError("Solo se puede modificar el resultado de un evento finalizado")
        self._resultado = nuevo_resultado

    @property
    def mercado(self):
        """Devuelve el mercado asociado al evento"""
        return self._mercado
