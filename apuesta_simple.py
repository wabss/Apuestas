"""Implementacion clase ApuestaSimple"""
from apuesta import Apuesta
from evento import Evento
from billetera import Billetera

class ApuestaSimple(Apuesta):
    """"Clase para apuestas simples"""
    def __init__(self, monto: float, evento: Evento, prediccion: str, estado: str="pendiente") -> None:
        super().__init__(monto, estado)
        self._evento = evento
        self._prediccion = prediccion

    @property
    def evento(self) -> Evento:
        """Muestra el evento por el que se apuesta"""
        return self._evento

    @property
    def prediccion(self) -> str:
        """Muestra la prediccion hecha en la apuesta"""
        return self._prediccion

    def calcular_resultado(self) -> float:
        """
        Calcula y retorna el valor del premio obtenido en caso de ganar un apuesta.
        Si el evento aun no ha finalizado o la apuesta no se cumplio retorna 0
        """
        if self._prediccion not in self._evento.mercado.opciones_apuestas.keys():
            return 0
        if self._evento.estado in ("programado", "en juego"):
            return 0
        if self._evento.resultado == self._prediccion:
            self._estado = "ganada"
            return self._monto * self._evento.mercado.opciones_apuestas[self._prediccion]
        self._estado = "perdida"
        return 0

    def transferencia(self, billetera: Billetera) -> None:
        """Registra el premio en el historia de la billetera y actualiza el saldo de la misma"""
        billetera.agregar_premio(self.calcular_resultado())
        billetera.actualizar_saldo(self.calcular_resultado())
