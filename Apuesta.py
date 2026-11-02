"""Implementacion clase Apuestas"""
from abc import ABC, abstractmethod
from billetera import Billetera

class Apuesta(ABC):
    "Clase abstracta para apuestas"
    def __init__(self, monto: float, estado: str):
        self._monto = monto
        self._estado = estado

    @abstractmethod
    def calcular_resultado(self) -> str:
        "Calcula el resultado de la apuesta"

    @abstractmethod
    def transferencia(self, billetera: Billetera) -> bool:
        "Transfiere el dinero a la billetera del usuario"

    @property
    def estado(self) -> str:
        """Muestra el estado de la apuesta"""
        return self._estado

    @property
    def monto(self) -> float:
        """Muestra el monto apostado"""
        return self._monto
