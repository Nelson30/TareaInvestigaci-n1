class Persona:
    def __init__(self):
        self.name = None
        self.sexo = None

    def getName(self):
        return self.name

    def getSexo(self):
        return self.sexo


class Masculino(Persona):
    def __init__(self, name):
        print("Hola Sr. " + name)


class Femenino(Persona):
    def __init__(self, name):
        print("Hola Srta. " + name)



class Factory:
    def getPersona(self, name, sexo):
        if sexo == 'M':
            return Masculino(name)
        if sexo == 'F':
            return Femenino(name)


if __name__ == '__main__':
    factory = Factory()         #aquí se ejemplifica una de las consecuencias en las que siempre se debe instanciar la clase creator/factory
    persona = factory.getPersona("Rubilio", "M")