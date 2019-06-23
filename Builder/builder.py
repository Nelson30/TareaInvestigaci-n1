from abc import ABCMeta, abstractstaticmethod


class ICasaBuilder(metaclass=ABCMeta):
    """Interface Builder"""

    @abstractstaticmethod
    def set_tipo_material(self, value):
        """Tipo material"""

    @abstractstaticmethod
    def set_tipo_construccion(self, value):
        """Tipo de construcción"""

    @abstractstaticmethod
    def set_puertas(self, value):
        """Cantidad Puertas"""

    @abstractstaticmethod
    def set_numero_ventanas(self, value):
        """Cantidad ventanas"""

    @abstractstaticmethod
    def get_result(self):
        """Devuelve construcción"""


class CasaBuilder(ICasaBuilder):


    def __init__(self):
        self.casa = Casa()

    def set_tipo_material(self, value):
        self.casa.tipo_material = value
        return self

    def set_tipo_construccion(self, value):
        self.casa.tipo_construccion = value
        return self

    def set_puertas(self, value):
        self.casa.puertas = value
        return self

    def set_numero_ventanas(self, value):
        self.casa.ventanas = value
        return self

    def get_result(self):
        return self.casa


class Casa():


    def __init__(self, tipo_contruccion="Apartmento", puertas=0, ventanas=0, tipo_material="Block"):

        self.tipo_material = tipo_material
        self.tipo_construccion = tipo_contruccion
        self.doors = puertas
        self.windows = ventanas

    def __str__(self):
        return "Esta es de {0} es un(a) {1} con {2} puerta(s) y {3} ventana(s).".format(
            self.tipo_material, self.tipo_construccion, self.puertas, self.ventanas
        )


class IglooDirector:

    @staticmethod
    def construct():
        return CasaBuilder()\
            .set_tipo_construccion("Igloo")\
            .set_tipo_material("Hielo")\
            .set_puertas(1)\
            .set_numero_ventanas(0)\
            .get_result()


class CasaFlotanteDirector:

    @staticmethod
    def construct():
        return CasaBuilder()\
            .set_tipo_construccion("Casa Flotante")\
            .set_tipo_material("madera")\
            .set_puertas(6)\
            .set_numero_ventanas(8)\
            .get_result()


class CastilloDirector:

    @staticmethod
    def construct():
        return CasaBuilder()\
            .set_tipo_construccion("Castillo")\
            .set_tipo_material("Granito")\
            .set_puertas(100)\
            .set_numero_ventanas(200).get_result()


if __name__ == "__main__":
    IGLOO = IglooDirector.construct()
    HOUSE_BOAT = CasaFlotanteDirector.construct()
    CASTLE = CastilloDirector.construct()
    print(IGLOO)
    print(HOUSE_BOAT)
    print(CASTLE)