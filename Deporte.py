class Deporte:
    def __init__(self,nombre):
        """
        Inicializa un deporte con su nombre, lista de equipos y
        lista de eventos
        """

        self.nombre= nombre
        self.equipos= {}
        self.eventos=[]


    def agregar_equipo(self,nombre_equipo):
        """
        Agrega un equipos al deporte con puntaje 0.
        Devuelve True si se agrego, False si ya existia.
        """

        if nombre_equipo in self.equipos:
            return False
        self.equipos[nombre_equipo]= 0
        return True

    def agregar_evento(self,evento):
        """
        Agrega une vento a la lista de eventos del deporte.
        Devuelve True si se agrego correctamente.
        """

        self.eventos.append(evento)
        return True

    def eliminar_equipo(self,nombre_equipo):
        """
        Elimina un equipo del deporte.
        Devuelve True si se elimino, False si no existia
        """
        if nombre_equipo in self.equipos:
            del self.equipos[nombre_equipo]
            return True
        return False

    def eliminar_evento(self, evento):
        """
        Elimina un evento de la lista.
        Devuelve True si se elimino y False si no estaba.
        """

        if evento in self.eventos:
            self.eventos.remove(evento)
            return True
        return False