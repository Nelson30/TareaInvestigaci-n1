from abc import ABCMeta, abstractmethod


class Musica():
    __metaclass__ = ABCMeta

    @abstractmethod
    def reproducir(self):
        pass


class Mp3(Musica):
    def reproducir(self):
        print("Reproduciendo .mp3 music!")


class Acc(Musica):
    def reproducir(self):
        print("Reproduciendo .acc music!")


class MusicFactory(object):
    def play(self, object_type):
        return eval(object_type)().reproducir()


if __name__ == "__main__":
    mf = MusicFactory()
    music = input("Que desea reproducir Mp3 o ACC")
    mf.play(music)