
from Ranking import Ranking



def probar_ranking():
    ranking = Ranking()

    u1 = Usuario("Carlos")
    u1.billetera.movimientos["deposito"] = [100, 50]
    u1.billetera.movimientos["retiro"] = [30]

    u2 = Usuario("Ana")
    u2.billetera.movimientos["deposito"] = [200, 100, 50]
    u2.billetera.movimientos["apuesta"] = [20, 10]

    u3 = Usuario("Juan")
    u3.billetera.movimientos["deposito"] = [80]

    ranking.clasificacion_usuarios.append(u1)
    ranking.clasificacion_usuarios.append(u2)
    ranking.clasificacion_usuarios.append(u3)

    class Deporte:
        def __init__(self):
            self.equipos = {
                "Real Madrid": 10,
                "Barcelona": 7,
                "Atletico": 4
            }

    deporte = Deporte()

    print("Ranking usuarios:")
    print(ranking.ordenar_usuarios())

    print("Ranking equipos:")
    print(ranking.ordenar_equipos(deporte))

