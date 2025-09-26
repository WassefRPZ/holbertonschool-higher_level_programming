#!/usr/bin/python3
class VerboseList(list):
    """
    Liste personnalisée qui affiche des messages lors des modifications.
    Hérite directement de la classe intégrée list.
    Les méthodes append, extend, remove et pop sont redéfinies
    pour ajouter des notifications tout en conservant le
    comportement normal des listes.
    """

    def append(self, item):
        """
        Ajoute un élément à la fin de la liste.
        Affiche un message indiquant l'élément ajouté.
        :param item: élément à ajouter
        """
        super().append(item)
        print(f"Added [{item}] to the list.")

    def extend(self, iterable):
        """
        Étend la liste avec les éléments d'un itérable.
        Affiche un message indiquant combien d'éléments ont été ajoutés.
        :param iterable: séquence d'éléments à ajouter
        """
        count = len(iterable)
        super().extend(iterable)
        print(f"Extended the list with [{count}] items.")

    def remove(self, item):
        """
        Supprime la première occurrence d'un élément dans la liste.
        Affiche un message avant la suppression.
        :param item: élément à supprimer
        """
        print(f"Removed [{item}] from the list.")
        super().remove(item)

    def pop(self, index=-1):
        """
        Supprime et retourne un élément de la liste à l’index donné.
        Si aucun index n’est fourni, supprime le dernier élément.
        Affiche un message indiquant quel élément est supprimé.
        :param index: position de l’élément à retirer (par défaut -1, dernier)
        :return: l’élément supprimé
        """
        item = self[index]
        print(f"Popped [{item}] from the list.")
        return super().pop(index)
