"""Modulo principal"""

from usuario import Usuario
from eventos import Evento
from mercado import Mercado

usuario_1 = Usuario.registrar_usuario()
mercado_1 = Mercado({"+1 gol": 1.2, "+2 gol": 2.4})
evento_1 = Evento("Futbol", "Millos", "Deportivo Cucuta", "12/11/2026", mercado_1, "finalizado", "+2 gol")

usuario_1.billetera.apuestas = usuario_1.crear_apuesta(125000, [evento_1], ["+2 gol"])
usuario_1.billetera.apuestas = usuario_1.crear_apuesta(3240, [evento_1], ["+1 gol"])

usuario_1.billetera.apuestas[0].transferencia(usuario_1.billetera)

print(usuario_1.billetera.saldo)
usuario_1.billetera.mostrar_historial()

