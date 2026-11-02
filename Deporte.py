"""Código para la clase Deporte y su relación con Evento"""
from eventos import Evento
class Deporte:
    """Clase encargada de la creación de un Deporte y """
    def __init__(self,nombre) -> None:
        """Inicializa un deporte con su nombre, lista de equipos y lista de eventos"""
        self._nombre = nombre
        self._equipos = {}
        self._eventos = []

    @property
    def equipos(self) -> dict:
        """Enseña los equipos y las apuestas en las que han participado"""
        return self._equipos

    @property
    def eventos(self) -> list:
        """Enseña los eventos del deporte"""
        return self._eventos

    def agregar_equipo(self,nuevo_equipo: str) -> bool:
        """
        Agrega un equipo al deporte con 0 apuestas.
        Devuelve True si se agrego o False si ya existia.
        """
        if nuevo_equipo in self._equipos:
            return False
        self._equipos.update({nuevo_equipo: 0})
        return True

    def agregar_evento(self, evento: Evento) -> bool:
        """Agrega un evento a la lista de eventos del deporte.
        Devuelve True si se agrego o False si ya existia.
        """
        if evento in self._eventos:
            return False
        self._eventos.append(evento)
        return True

    def eliminar_equipo(self, equipo: str) -> bool:
        """
        Elimina un equipo del deporte.
        Devuelve True si se elimino o False si no existia
        """
        if equipo in self._equipos:
            self._equipos.pop(equipo)
            return True
        return False

    def eliminar_evento(self, evento) -> bool:
        """
        Elimina un evento de la lista.
        Devuelve True si se elimino y False si no estaba.
        """
        if evento in self._eventos:
            self._eventos.remove(evento)
            return True
        return False
