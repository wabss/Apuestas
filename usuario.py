"""Código para la clase Usuario y su relación con Billetera"""
from apuesta_simple import ApuestaSimple
from billetera import Billetera
from eventos import Evento
# from ApuestaCombinada import ApuestaCombinada

class Usuario:
    """Clase encargada de la creación de usuario y sus apuestas"""
    def __init__(self, nombre: str, edad: int, billetera: Billetera):
        self._nombre = nombre
        self._edad = edad
        self._billetera = billetera # publico

    @property
    def nombre(self):
        """Enseña el nombre del Usuario"""
        return self._nombre

    @property
    def edad(self):
        """Enseña la edad del Usuario"""
        return self._edad

    @property
    def billetera(self):
        """Enseña algunos datos basicos del Usuario"""
        return self._billetera

    @classmethod
    def registrar_usuario(cls):
        """Registra un usuario con su nombre y edad"""
        nombre = str(input("Ingrese su nombre: "))
        edad = int(input("Ingrese su edad: "))
        billetera = Billetera(float(input("Cuanto saldo tienes ")))
        if edad >= 18:
            return cls(nombre, edad, billetera)
        else: 
            return "Menor\nDiddy va por ti"

    def crear_apuesta(self, monto: float, eventos: list[Evento], predicciones: list[str]):
        """Crea una apuesta con las especificaciones dadas por el usuario"""
        if len(eventos) == 1:
            return ApuestaSimple(monto, eventos[0], predicciones[0])
        # else:
        #     return ApuestaCombinada(monto, eventos, predicciones)
