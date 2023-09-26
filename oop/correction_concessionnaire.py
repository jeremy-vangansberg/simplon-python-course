
from abc import ABC, abstractmethod



class Vehicule(ABC):

    def __init__(self, couleur, marque, modele, prix_HT, reduction_applicable, TVA = 0.2):
        self.couleur = couleur
        self.marque = marque
        self.modele = modele
        self.prix_HT = prix_HT
        self.prix_TTC = prix_HT * (1 + TVA )
        self.reduction_applicable = reduction_applicable



    def __repr__(self):
        return str({"marque":self.marque, "modele":self.modele})


class Voiture(Vehicule):
    def __init__(self, couleur: str, marque :str, modele, prix_HT, reduction_applicable, nbr_portes: int, TVA = 0.2):
        self.nbr_portes = nbr_portes
        super().__init__(couleur, marque, modele, prix_HT, reduction_applicable)

    def __repr__(self):
        return str({"type": "Voiture", "marque":self.marque, "modele":self.modele})

class Moto(Vehicule):
    def __init__(self, couleur, marque, modele, prix_HT, reduction_applicable, topcase: bool, TVA = 0.2):
        self.topcase = topcase
        super().__init__(couleur, marque, modele, prix_HT, reduction_applicable)

    def __repr__(self):
        return str({"type": "Moto", "marque":self.marque, "modele":self.modele})

class Camion(Vehicule):
    def __init__(self, couleur, marque, modele, prix_HT, reduction_applicable, tonnage: float, TVA = 0.2):
        self.tonnage = tonnage
        super().__init__(couleur, marque, modele, prix_HT, reduction_applicable)

    def __repr__(self):
        return str({"type": "Camion", "marque":self.marque, "modele":self.modele})


class Contrat:
    pass


class Vendeur:
    def __init__(self, nom, statut, contrat:Contrat):
        self.nom = nom
        self.statut = statut
        self.contrat = contrat
        self.paie = contrat.calcul_paie(8)


from abc import ABC, abstractmethod

class Contrat(ABC):

    @abstractmethod
    def calcul_paie(self):
        pass


class Contrat_journalier(Contrat):
    def __init__(self, taux_horraire):
        self.taux_horraire = taux_horraire

    def calcul_paie (self, nbr_heure_travaillée):
        return self.taux_horraire * nbr_heure_travaillée

class Contrat_mensuel(Contrat):
    def __init__(self, salaire_mensuel):
        self.salaire_mensuel = salaire_mensuel

    def calcul_paie (self):
        return self.salaire_mensuel

class Contrat_freelance(Contrat):
    def __init__(self, TJM):
        self.TJM = TJM

    def calcul_paie (self, nbr_jour_travaillé):
        return self.TJM * nbr_jour_travaillé







class Vente:
    def __init__(self, vehicule:Vehicule, vendeur:Vendeur, reduction_demande: bool, vendeur_senior_associe=None):
        self.vehicule = vehicule
        self.vendeur = vendeur
        self.reduction_demande = reduction_demande
        self.prix_final = self.__calcul_prix_final()
        self.vendeur_senior_associe = vendeur_senior_associe

    def __calcul_prix_final(self):
        if self.reduction_demande == True:
            return self.vehicule.prix_TTC * (1 - self.vehicule.reduction_applicable) 
        else:
            return self.vehicule.prix_TTC



def creer_vente(vehicule, vendeur, reduction_demandee, vendeur_senior_associe: Vendeur = None):
    if vendeur.statut == "senior" or reduction_demandee == False:
        return Vente(vehicule, vendeur, reduction_demandee)
    elif vendeur.statut == "junior" and reduction_demandee == True and vendeur_senior_associe == None:
        print("Pour pouvoir accorder une reduction, il faut un vendeur senior associé")
    else: 
        if vendeur_senior_associe.statut == "senior":
            return Vente(vehicule, vendeur, reduction_demandee, vendeur_senior_associe)
        else: 
            print("le vendeur associé n'est pas non plus senior")


"""

il existe trois types de vendeur, les vendeurs payés à l’heure, ceux freelance à la mission et ceux payés au mois. Une méthode permettra de calculer leur paie chaque mois.


"""

class Concessionnaire:

    def __init__(self, adresse, siret):
        self.inventaire = []
        self.liste_vendeur = []
        self.adresse = adresse
        self.siret = siret
    
    def inventaire_par_marque(self):
        dictionnaire_par_marque = {}
        for vehicule in self.inventaire:
            if vehicule.marque not in dictionnaire_par_marque:
                dictionnaire_par_marque[vehicule.marque] = 1
            else:
                dictionnaire_par_marque[vehicule.marque] += 1
        return dictionnaire_par_marque

    def ajouter_inventaire(self,vehicule: Vehicule):
        self.inventaire.append(vehicule)

    def retirer_inventaire(self,vehicule: Vehicule):
        self.inventaire.remove(vehicule)

    def ajouter_liste_vendeur(self,vendeur: Vendeur):
        self.inventaire.append(vendeur)

    def retirer_liste_vendeur(self,vendeur: Vendeur):
        self.inventaire.remove(vendeur)



mon_vendeur = Vendeur ("Denis", "junior", Contrat_freelance(300))
mon_vendeur_senior = Vendeur ("Fred", "senior", Contrat_journalier(10))


print(mon_vendeur.contrat.calcul_paie(10))
print(mon_vendeur_senior.contrat.calcul_paie(7))


# ma_voiture = Voiture("rouge", "Toyota", 'Hiaris', 25000, 0.1, 4)
# ma_moto = Moto("rouge", "Toyota", 'ROméo', 15000, 0.1, True)

# ma_vente = creer_vente(ma_voiture,mon_vendeur, True,mon_vendeur_senior)

# mon_concessionnaire = Concessionnaire("5 rue De la République", 38499495)

# mon_concessionnaire.ajouter_inventaire(ma_voiture)
# mon_concessionnaire.ajouter_inventaire(ma_moto)
# mon_concessionnaire.retirer_inventaire(ma_moto)
# print(mon_concessionnaire.inventaire)

# mon_concessionnaire.ajouter_inventaire(Camion("rouge", "Toyota", 'ROméo', 15000, 0.1, 18.5))
# #mon_concessionnaire.retirer_inventaire(Camion("rouge", "Toyota", 'ROméo', 15000, 0.1, 18.5))


# print(mon_concessionnaire.inventaire)

