"""Implementacion clase Apuesta Combinada"""
from apuesta import Apuesta
from eventos import Evento
from billetera import Billetera

class ApuestaCombinada(Apuesta):
    """"Clase para apuestas combinadas"""
    def __init__(self, monto: float, predicciones: list[str], eventos: list[Evento], estado: str="pendiente"):
        super().__init__(monto, estado)
        self._predicciones = predicciones
        self._eventos = eventos

    @property
    def eventos(self) -> list:
        """Muestra el evento por el que se apuesta"""
        return self._eventos

    @property
    def predicciones(self) -> list:
        """Muestra la prediccion hecha en la apuesta"""
        return self._predicciones


    def calcular_resultado(self) -> float:
        """
        Calcula y retorna el valor del premio obtenido en caso de ganar un apuesta.
        Si el evento aun no ha finalizado o la apuesta no se cumplio retorna 0
        """
        cuota_total = 1

        for i, prediccion in enumerate(self.predicciones, 0):
            if prediccion not in self.eventos[i].mercado.opciones_apuestas.keys():
                return 0
            if prediccion == self.eventos[i].resultado:
                cuota_total *= self.eventos[i].mercado.opciones_apuestas[prediccion]
            else:
                return 0

        return cuota_total * self._monto
        
    def transferencia(self, billetera: Billetera) -> None:  
        """Registra el premio en el historia de la billetera y actualiza el saldo de la misma"""
        billetera.agregar_movimiento("premios", self.calcular_resultado())
        billetera.actualizar_saldo(self.calcular_resultado())

