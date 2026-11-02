"""Sección para probar que el sistema funciona"""

from usuario import Usuario
from eventos import Evento
from mercado import Mercado
from apuesta_combinada import ApuestaCombinada

usuario_1 = Usuario.registrar_usuario()
mercado_1 = Mercado({"+0.5 gol": 1.2, "+1.5 gol": 2.4})
mercado_2 = Mercado({"+2 gol": 1.2})
evento_1 = Evento("Futbol", "Millos", "Deportivo Cucuta", "12/11/2026", mercado_1, "finalizado", "+0.5 gol")
evento_2 = Evento("Futbol", "waos", "waos-2", "12/11/2026", mercado_2, "finalizado", "+2 gol")

usuario_1.billetera.apuestas = usuario_1.crear_apuesta(125000, [evento_1], ["+1.5 gol"])
usuario_1.billetera.apuestas = usuario_1.crear_apuesta(3240, [evento_1], ["+0.5 gol"])

usuario_1.billetera.apuestas[0].transferencia(usuario_1.billetera)

print(usuario_1.billetera.saldo)
usuario_1.billetera.mostrar_historial()

print(ApuestaCombinada(13212.3, ["+0.5 gol", "+2 gol"], [evento_1, evento_2], "Finalizado").calcular_resultado())
