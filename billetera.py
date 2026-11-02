"""Archivo encargado de la Billetera"""
class Billetera:
    """Clase Billetera perteneciente al usuario"""
    def __init__(self, saldo: float):
        self._saldo = saldo
        self._movimientos = dict(depositos=[], retiros=[], premios=[])
        self._apuestas = []

    @property
    def saldo(self):
        """Enseña el saldo actual de la billetera"""
        return self._saldo
    @saldo.setter
    def saldo(self):
        """Valida que el saldo no sea negativo"""
        if self._saldo <= 0:
            return "Saldo insuficiente para apostar"

    @property
    def movimientos(self):
        """Enseña los movimientos que ha realizado el Usuario con su billetera"""
        return self._movimientos
    @movimientos.setter
    def movimientos(self, nuevo_movimiento: str, valor: float):
        """Agrega un nuevo movimiento al historial de movimientos"""
        if nuevo_movimiento in self._movimientos.items():
            self._movimientos[nuevo_movimiento] += valor
        else:
            return "Movimiento invalido"

    @property
    def apuestas(self):
        """Enseña el historial de apuestas del usuario"""
        return self._apuestas
    @apuestas.setter
    def apuestas(self, nueva_apuesta: Apuesta):
        """Agrega una nueva apuesta creada en el historial de apuestas"""
        self._apuestas += nueva_apuesta

    def recarga(self, monto: float):
        """Aumenta el saldo al depositar un monto en la billetera"""
        if monto > 0:
            self._saldo += monto
            self._movimientos += "deposito", monto
            return True
        else:
            return False

    def retiro(self, monto: float):
        """Reduce el saldo al retirar un monto de la billetera"""
        if monto < self._saldo:
            self._saldo -= monto
            self._movimientos += "retiros", monto
            return True
        else:
            return False

    def mostrar_historial(self):
        """Muestra todo el historial de movimientos y de apuestas"""
        for movimiento, montos in self._movimientos.items():
            print(f"{movimiento} : {montos}")
        print(f"apuestas : {self._apuestas}")
