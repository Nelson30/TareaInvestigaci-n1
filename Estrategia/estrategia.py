from types import MethodType

class Animal(object):

    def __init__(self, *args, **kwargs):
        self.name = kwargs.pop('nombre', None) or 'Animal'
        if kwargs.get('caminar', None):
            self.caminar = MethodType(kwargs.pop('caminar'), self)

    def caminar(self):
        """
        Test
        """
        message = '{} debe implementar metodo caminar'.format(
            self.__class__.__name__)
        raise NotImplementedError(message)



def arrastrar(self):
    print('Me arrastro por que soy una {}.'.format(self.name))


def caminar_cuatro_patas(self):
    print('Uso mis 4 patas para caminar porque soy un(a) {}.'.format(
        self.name))


def caminar_dos_patas(self):
    print('Estoy en mis dos patas por soy {}.'.format(
        self.name))

if __name__ == "__main__":
    animal = Animal()
    cobra = Animal(nombre='Cobra Reina', caminar=arrastrar)
    elefante = Animal(nombre='Elefante', caminar=caminar_cuatro_patas)
    kanguro = Animal(nombre='Kanguro', caminar=caminar_dos_patas)

    kanguro.caminar()
    elefante.caminar()
    cobra.caminar()