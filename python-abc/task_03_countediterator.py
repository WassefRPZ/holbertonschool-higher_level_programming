#!/usr/bin/python3
class CountedIterator:
    """
    Itérateur personnalisé qui encapsule un itérateur classique
    et compte le nombre d'éléments déjà consommés.
    """

    def __init__(self, iterable):
        """
        Constructeur.
        :param iterable: tout objet itérable (liste, tuple, string, etc.)
        """
        self.iterator = iter(iterable)
        self.count = 0

    def __iter__(self):
        """
        Un itérateur doit être iterable lui-même.
        On retourne self pour permettre l'utilisation dans une boucle for.
        """
        return self

    def __next__(self):
        """
        Récupère l'élément suivant de l'itérateur.
        Incrémente le compteur à chaque appel réussi.
        Lève StopIteration quand la séquence est terminée.
        """
        item = next(self.iterator)
        self.count += 1
        return item

    def get_count(self):
        """
        Retourne le nombre d'éléments déjà consommés.
        """
        return self.count
