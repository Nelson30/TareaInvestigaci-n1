from __future__ import print_function

from abc import ABCMeta, abstractmethod

class Button:
    __metaclass__ = ABCMeta

    @abstractmethod
    def pintar(self):
        pass

class LinuxButton(Button):
    def pintar(self):
        return "Dibujar butón para Linux"

class WindowsButton(Button):
    def pintar(self):
        return "Dibujar butón para Windows"

class MacOSButton(Button):
    def pintar(self):
        return "Dibujar butón para MacOS"

class GUIFactory:
    __metaclass__ = ABCMeta

    @abstractmethod
    def crear_button(self):
        pass

class LinuxFactory(GUIFactory):
    def crear_button(self):
        return LinuxButton()

class WindowsFactory(GUIFactory):
    def crear_button(self):
        return WindowsButton()

class MacOSFactory(GUIFactory):
    def crear_button(self):
        return MacOSButton()

os = "osx"

if os == "linux":
    factory = LinuxFactory()
elif os == "osx":
    factory = MacOSFactory()
elif os == "win":
    factory = WindowsFactory()
else:
    raise NotImplementedError(
        "OS no reconocido: {}".format(os)
    )

if factory:
    button = factory.crear_button()
    result = button.pintar()
    print(result)