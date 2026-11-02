"""Implementacion clase Apuestas"""
from abc import ABC, abstractmethod

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
