from abc import ABC, abstractmethod

class Vehicule(ABC):
    def drive(self) -> str:
        return "the vehicule is on its wheels!"

    @property
    @abstractmethod
    def prix(self):
        pass

class Voiture(Vehicule):
    def __init__(self, marque, couleur, prix, reduction_applicable):
        self.marque = marque
        self.couleur = couleur
        self.prix = prix
        self.reduction_applicable = reduction_applicable

    def __str__(self):
        return f'{self.marque} {self.couleur} à {self.prix}'

    def __repr__(self):
        return f'{self.marque} {self.couleur} à {self.prix}'
    
    @property
    def prix(self):
        return self._prix

    @prix.setter
    def prix(self, value):
        if  not isinstance(value,int):
            raise ValueError("prix should be int")
        self._prix = value

    def prix_apres_reduction(self):
        return self.prix * (1-self.reduction_applicable)

    def prix_apres_double_reduction(self):
        return self.prix * (1 - 2*self.reduction_applicable)
    
    def prix_apres_triple_reduction(self):
        return self.prix * (1 - 3*self.reduction_applicable)

    def fonction_sans_fin(self):
        while True:
            print("sans fin!")

    def I_want_to_quit(self):
        self.fonction_sans_fin()
        return "I quit"

