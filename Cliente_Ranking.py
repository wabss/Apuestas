from ranking import Ranking
from usuario import Usuario
from deporte import Deporte
from billetera import Billetera

def probar_ranking():
    ranking = Ranking()

    deporte_1 = Deporte("Futbol")
    deporte_1.agregar_equipo("millos")
    deporte_1.agregar_equipo("nacional")
    deporte_1.agregar_equipo("deportivo cucuta")

    u1 = Usuario("Carlos", 19, Billetera(12345.6))
    u1.billetera.agregar_movimiento("depositos", 100)
    u1.billetera.agregar_movimiento("premios", 100)
    u1.billetera.agregar_movimiento("retiros", 30)

    u2 = Usuario("Ana", 30, Billetera(4663635.6))
    u2.billetera.agregar_movimiento("depositos", 200)
    u2.billetera.agregar_movimiento("retiros", 100)
    u2.billetera.agregar_movimiento("depositos", 50)

    u3 = Usuario("Juan", 20, Billetera(3123123.6))
    u3.billetera.agregar_movimiento("depositos", 80)

    ranking.clasificacion_usuarios.append(u1)
    ranking.clasificacion_usuarios.append(u2)
    ranking.clasificacion_usuarios.append(u3)

    print("Ranking usuarios:")
    print(ranking.ordenar_usuarios())

    print("Ranking equipos:")
    print(ranking.ordenar_equipos(deporte_1))


probar_ranking()
