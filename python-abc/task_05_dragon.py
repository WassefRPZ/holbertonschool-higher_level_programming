#!/usr/bin/python3
class SwimMixin:
    """
    Mixin qui ajoute la capacité de nager.
    Cette classe n'est pas destinée à être utilisée seule,
    mais à être héritée pour enrichir une autre classe.
    """
    def swim(self):
        """
        Affiche un message indiquant que la créature nage.
        """
        print("The creature swims!")


class FlyMixin:
    """
    Mixin qui ajoute la capacité de voler.
    Comme tout mixin, il est prévu pour être combiné avec d'autres classes.
    """
    def fly(self):
        """
        Affiche un message indiquant que la créature vole.
        """
        print("The creature flies!")


class Dragon(SwimMixin, FlyMixin):
    """
    Classe représentant un dragon.
    Hérite de SwimMixin et FlyMixin, ce qui lui permet de
    nager et de voler sans dupliquer de code.
    Peut aussi avoir des comportements supplémentaires spécifiques.
    """
    def roar(self):
        """
        Affiche un message indiquant que le dragon rugit.
        """
        print("The dragon roars!")
