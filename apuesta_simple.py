"""Implementacion clase ApuestaSimple"""
from Apuesta import Apuesta
from eventos import Evento
from billetera import Billetera

class ApuestaSimple(Apuesta):
    """"Clase para apuestas simples"""
    def __init__(self, monto: float, evento: Evento, prediccion: str, estado: str="pendiente"):
        super().__init__(monto, estado)
        self._evento = evento
        self._prediccion = prediccion

    def calcular_resultado(self) -> float:
        if self._evento.estado == "programado" or self._evento.estado == "en juego":
            return 0
        if self._evento.resultado == self._prediccion:
            return self._monto * self._evento.mercado.opciones_apuestas[self._prediccion]

    def transferencia(self, billetera: Billetera) -> bool:
        billetera.agregar_movimiento("premios", self.calcular_resultado())
        billetera.actualizar_saldo(self.calcular_resultado())
