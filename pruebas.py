from usuario import Usuario
from billetera import Billetera
from evento import Evento
from mercado import Mercado
from deporte import Deporte
from Ranking import Ranking

usuario_2 = Usuario("Juan", 21, Billetera(123000041))
usuario_3 = Usuario("Benito", 21, Billetera(100000))
usuario_1 = Usuario("Jose", 21, Billetera(20000))

mercado_1 = Mercado({"gana equipo 1": 1.3, "gana equipo 2": 1.3, "empate": 0.5})
deporte_1 = Deporte("futbol")
deporte_1.agregar_equipo("equipo 1")
deporte_1.agregar_equipo("equipo 2")

evento_1 = Evento(deporte_1, "equipo 1", "equipo 2", "12/11/2026", mercado_1, "finalizado", "gana equipo 1")
evento_2 = Evento(deporte_1, "equipo 1", "equipo 2", "12/11/2026", mercado_1, "finalizado", "empate")

usuario_1.crear_apuesta(12000, [evento_1], ["gana equipo 1"])
usuario_2.crear_apuesta(340000, [evento_1, evento_2], ["gana equipo 1", "empate"])


print(usuario_1.billetera.saldo)
print(usuario_2.billetera.saldo)

print(usuario_2.billetera.apuestas[0].calcular_resultado())
print(usuario_1.billetera.apuestas[0].calcular_resultado())

usuario_2.billetera.apuestas[0].transferencia(usuario_2.billetera)
usuario_1.billetera.apuestas[0].transferencia(usuario_1.billetera)

usuario_1.billetera.mostrar_historial()
usuario_2.billetera.mostrar_historial()

usuario_1.billetera.retiro(1000)
print(usuario_1.billetera.saldo)

ranking = Ranking()

ranking.clasificacion_usuarios.append(usuario_1)
ranking.clasificacion_usuarios.append(usuario_2)
ranking.clasificacion_usuarios.append(usuario_3)
print(ranking.ordenar_usuarios())
