
from dataclasses import dataclass, field
from abc import ABC, abstractmethod

@dataclass
class Vehicule(ABC):
    
    couleur: str
    _marque: str
    modele: str
    prix_ht: float
    reduction_applicable: float

    @property
    @abstractmethod
    def marque(self):
        return self._marque

    def __post_init__(self):
        self.prix_ttc: float = self.prix_ht * 1.20
    

@dataclass
class Voiture(Vehicule):
    
    boitier: str

    @property
    def marque(self):
        return self._marque

@dataclass
class Moto(Vehicule):
    
    visiere: str

    @property
    def marque(self):
        return self._marque

@dataclass
class Camion(Vehicule):
    
    remorque: str

    @property
    def marque(self):
        return self._marque

@dataclass
class Vente:

    vendeurs: list["Vendeur"]
    vehicule: Vehicule
    reduction: bool = False

    def __post_init__(self):
        self.prix_de_vente: float = self.vehicule.prix_ttc
   
    def imprimer_en_pdf(self):
        print(f"Impression en PDF terminée: {self}")

    def appliquer_reduction(self, Vendeur):
        if not Vendeur.senior:
            raise ValueError("Ce vendeur n'est pas habilité à appliquer une réduction")
        self.reduction = True
        self.prix_de_vente = self.prix_de_vente*(1-self.vehicule.reduction_applicable)
        if not Vendeur in self.vendeurs:
            self.vendeurs.append(Vendeur)

@dataclass
class Vendeur:

    nom: str
    senior: bool
    nombre_ventes: int = 0

    def creer_vente(self, voiture):
        self.nombre_ventes += 1
        return Vente([self], voiture)

@dataclass
class Concessionnaire:

    adresse: str
    siret: int
    vendeurs: list[Vendeur]
    inventaire: list[Vehicule] = field(default_factory=list)

    def afficher_voiture_par_marque(self, marque):
        return len([vehicule for vehicule in self.inventaire if vehicule.marque == marque])

    def add_inventaire(self, vehicule: Vehicule):
        self.inventaire.append(vehicule)

    def remove_inventaire(self, vehicule: Vehicule):
        self.inventaire.remove(vehicule)


ma_voiture = Voiture("rouge","Toyota","Iaris",20000,0.1,"automatique")
mon_vendeur = Vendeur("denis",True)
ma_vente = Vente([mon_vendeur],ma_voiture)
print(ma_vente.prix_de_vente)
ma_vente.appliquer_reduction(mon_vendeur)
print(ma_vente.prix_de_vente)
#print(ma_vente)
print(ma_vente.imprimer_en_pdf())

