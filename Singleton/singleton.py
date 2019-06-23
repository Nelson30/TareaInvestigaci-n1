class Singleton(object):
    def __new__(instancia):

        if not hasattr(instancia, 'instance'):
            instancia.instance = super(Singleton, instancia).__new__(instancia)
        return instancia.instance

s = Singleton()
print ("Objeto: ", s)

s1 = Singleton()
print ("Objeto: ", s1)