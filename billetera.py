"""Archivo encargado de la Billetera"""
from Apuesta import Apuesta

class Billetera:
    """Clase Billetera perteneciente al usuario"""
    def __init__(self, saldo: float) -> None:
        self._saldo = saldo
        self._movimientos = dict(depositos=[], retiros=[], premios=[])
        self._apuestas = []

    @property
    def saldo(self) -> float:
        """Enseña el saldo actual de la billetera"""
        return self._saldo

    def actualizar_saldo(self, monto: float) -> None:
        """Actualiza el saldo"""
        self._saldo += monto

    @property
    def movimientos(self) -> dict:
        """Enseña los movimientos que ha realizado el Usuario con su billetera"""
        return self._movimientos

    def agregar_movimiento(self, nuevo_movimiento: str, valor: float) -> None:
        """Agrega un nuevo movimiento al historial de movimientos"""
        if nuevo_movimiento in self._movimientos.items():
            self._movimientos[nuevo_movimiento].append(valor)
        else:
            print("Movimiento invalido")

    @property
    def apuestas(self) -> list:
        """Enseña el historial de apuestas del usuario"""
        return self._apuestas
    @apuestas.setter
    def apuestas(self, nueva_apuesta: Apuesta) -> None:
        """Agrega una nueva apuesta creada en el historial de apuestas"""
        self._apuestas.append(nueva_apuesta)

    def recarga(self, monto: float) -> bool:
        """Aumenta el saldo al depositar un monto en la billetera"""
        if monto > 0:
            self._saldo += monto
            self._movimientos += "deposito", monto
            return True
        return False

    def retiro(self, monto: float) -> bool:
        """Reduce el saldo al retirar un monto de la billetera"""
        if monto < self._saldo:
            self._saldo -= monto
            self._movimientos += "retiros", monto
            return True
        return False

    def mostrar_historial(self) -> None:
        """Muestra todo el historial de movimientos y de apuestas"""
        for movimiento, montos in self._movimientos.items():
            print(f"{movimiento} : {montos}")
        print(f"apuestas : {self._apuestas}")
