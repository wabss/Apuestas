"""archivo encargado de la clase mercado"""
class Mercado:
    """Clase que representa el mercado de apuestas, opciones de apuestas y sus cuotas"""
    def __init__(self, opciones_apuestas: dict):
        """opciones_apuestas: diccionario con las opciones de apuestas y sus cuotas que varia dependiendo del evento"""
        self._opciones_apuestas = opciones_apuestas

    @property
    def opciones_apuestas(self):
        """Devuelve las opciones de apuestas y sus cuotas"""
        return self._opciones_apuestas