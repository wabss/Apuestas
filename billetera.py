"""Archivo encargado de la Billetera"""

class Billetera:
    """Clase Billetera perteneciente al usuario"""
    def __init__(self, saldo: float) -> None:
        self._saldo = saldo
        self._movimientos = {"depositos": [], "retiros": [], "premios": []}
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

    def agregar_premio(self, valor: float) -> bool:
        """Agrega un nuevo movimiento al historial de movimientos"""
        if valor > 0:
            self._movimientos["premios"].append(valor)
            return True
        return False

    @property
    def apuestas(self) -> list:
        """Enseña el historial de apuestas del usuario"""
        return self._apuestas

    def agregar_apuesta(self, nueva_apuesta) -> None:
        """Agrega una nueva apuesta creada en el historial de apuestas"""
        self._apuestas.append(nueva_apuesta)

    def recarga(self, monto: float) -> bool:
        """Aumenta el saldo al depositar un monto en la billetera"""
        if monto > 0:
            self._saldo += monto
            self._movimientos["depositos"].append(monto)
            return True
        return False

    def retiro(self, monto: float) -> bool:
        """Reduce el saldo al retirar un monto de la billetera"""
        if monto <= self._saldo:
            self._saldo -= monto
            self._movimientos["retiros"].append(monto)
            return True
        return False

    def mostrar_historial(self) -> None:
        """Muestra todo el historial de movimientos y de apuestas"""
        for movimiento, montos in self._movimientos.items():
            print(f"{movimiento} : {montos}")
        print(f"apuestas : {self._apuestas}")
