"""Implementacion clase ApuestaSimple"""
from Apuesta import Apuesta

class ApuestaSimple(Apuesta):
    """"Clase para apuestas simples"""
    def __init__(self, monto: float, estado: str, evento: Evento, prediccion: str):
        super().__init__(monto, estado)
        self._evento = evento
        self._prediccion = prediccion

    def calcular_resultado(self):
        return self._monto * self._evento.mercado.opciones_apuestas[self._prediccion]

    def transferencia(self, billetera: Billetera) -> bool:
        billetera.movimientos("premios", self.calcular_resultado())
        billetera.saldo += self.calcular_resultado()
