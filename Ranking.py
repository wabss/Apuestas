class Ranking:
    """
    Clase para ordenar usuarios y equipos
    """
    def __init__(self):
        """
        Crea las listas vacias
        """
        self.clasificacion_usuarios = []
        self.clasificacion_equipos = []

    def ordenar_usuarios(self):
        """
        Ordena los usuarios por el que tenga mas movimientos en la billetera
        """
        for i in range(len(self.clasificacion_usuarios)):
            for j in range(len(self.clasificacion_usuarios) - 1):
                cantidad1 = 0
                for lista in self.clasificacion_usuarios[j].billetera.movimientos.values():
                    cantidad1 = cantidad1 + len(lista)

                cantidad2 = 0
                for lista in self.clasificacion_usuarios[j + 1].billetera.movimientos.values():
                    cantidad2 = cantidad2 + len(lista)

                if cantidad1 < cantidad2:
                    temporal = self.clasificacion_usuarios[j]
                    self.clasificacion_usuarios[j] = self.clasificacion_usuarios[j + 1]
                    self.clasificacion_usuarios[j + 1] = temporal

        texto = ""
        for usuario in self.clasificacion_usuarios:
            texto = texto + usuario.nombre + "\n"
        return texto

    def ordenar_equipos(self, deporte):
        """
        Ordena los equipos por cuantas veces se apostaron (el numero del diccionario)
        """
        nombres = []
        veces = []
        for nombre in deporte.equipos:
            nombres.append(nombre)
            veces.append(deporte.equipos[nombre])

        for i in range(len(nombres)):
            for j in range(len(nombres) - 1):
                if veces[j] < veces[j + 1]:
                    aux = veces[j]
                    veces[j] = veces[j + 1]
                    veces[j + 1] = aux
                    aux2 = nombres[j]
                    nombres[j] = nombres[j + 1]
                    nombres[j + 1] = aux2

        texto = ""
        for i in range(len(nombres)):
            texto = texto + nombres[i] + " - " + str(veces[i]) + "\n"
        return texto