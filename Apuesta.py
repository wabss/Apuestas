"""Implementacion clase Apuestas"""
from abc import ABC, abstractmethod
from random import randint

class Apuesta(ABC):
    def __init__(self, monto: float, estado: str):
        self._monto = monto
        self._estado = estado

    @abstractmethod
    def calcular_resultado(self) -> str:
        pass

    @abstractmethod
    def transferencia(self, billetera: Billetera) -> bool:
        pass
