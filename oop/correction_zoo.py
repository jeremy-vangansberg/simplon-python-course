"""
Vous gérez un zoo qui abrite des poissons, des oiseaux et des félins.
- Tous les animaux possèdent un régime alimentaire de la forme {aliment: bool, aliment: bool}
- tous les animaux doivent pouvoir manger selon leur régime alimentaire

- Pour que les félins mangent il faut vérifier que ce qu'on leur donne soit bien de la viande
- Pour que les poissons mangent il faut vérifier que ce qu'on leur donne soit bien de la nourriture pour poisson
- Pour que les oiseaux mangent il faut vérifier que ce qu'on leur donne soit bien des graines

- Tous les poissons doivent pouvoir nager
- Tous les oiseaux doivent piailler

- Les lions doivent rugir et les chats miauler, les panthères ne font rien
- les canaris piaillent en disant "cuicui" les autruches piaillent en disant "CUICUI"

Créer votre zoo avec 2 lion , 3 chat, 1 canari, 2 autruches, 3 raies et 1 dauphin.
"""

from abc import ABCMeta, abstractmethod  # permet de définir des classes de base


class Animal (metaclass = ABCMeta):
    @abstractmethod
    def manger(self):
        pass

    @property
    @abstractmethod
    def regime_alimentaire(self):
        pass

class Poisson (Animal):
    regime_alimentaire = {"nourriture_pour_poisson": True, "Viande":False, "Graine": False}

    def manger(self, aliment):
        if self.regime_alimentaire[aliment] == True:
            print ("le poisson a bien mangé")
        else:
            print("cet aliment ne convient pas aux poissons")

    @abstractmethod
    def nager(self):
        pass

class Raie(Poisson):
    def nager(self):
        print("la raie nage")


une_raie = Raie()
une_raie.manger("nourriture_pour_poisson")
une_raie.manger("Viande")
une_raie.nager()
