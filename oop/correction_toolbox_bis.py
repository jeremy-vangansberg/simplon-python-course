"""**`Exercice`**
- Créer des classes: boite à outils, marteau, tournevis, clou, vis 
- Instanciez une boîte à outils, un tournevis, et un marteau.
- Placez le marteau et le tournevis dans la boîte à outils.
- Instanciez une visse, et serrez-la avec le tournevis. Affichez la vis avant et après avoir été serrée.
- Instanciez un clou, puis enfoncez-le avec le marteau. Affichez le clou avant et après avoir été enfoncé.
- Une boite à outil possède 5 emplacements. (classe attributs)
- Régulièrement le constructeur des boites à outils sort un nouveau modèle qui permet d'etendre la capacité des boites à outils de 1 emplacement.

Pour chaque classe vous devez définir les attributs et les méthodes qui permettront d'éxecuter et de rapporter dans le terminal ces actions et ces états.
"""





class Vis:
    def __init__(self,type,statut = "non vissée"):
        self.type = type
        self.statut = statut

    def visser(self):
        self.statut = "non vissée" if self.statut =="vissée" else "vissée"
        


class Clou:
    def __init__(self,longueur, statut = "non cloué"):
        self.longueur = longueur
        self.statut = statut

    def clouer(self):
        self.statut = "cloué"

    pass


class Tournevis:
    def __init__(self,type):
        self.type = type

    def vissage(self,vis):
        if self.type == vis.type:
            vis.visser()
            print(f"la vis est maintenant {vis.statut}")
        else:
            print("le tournevis ne convient pas à la vis")

class Marteau:
    
    def clouage(self, clou):
        clou.clouer()
        print(f"le clou est maintenant {clou.statut}")


class Toolbox:
    nb_emplacement = 5

    def __init__(self):
        self.contenu = []
    
    def add_tool(self,outil):
        if len(self.contenu) < self.nb_emplacement:
            self.contenu.append(outil)
        else:
            print("la boite à outil est déja pleine")

    @classmethod
    def update_toolbox(cls,nb_emplacement_supp =1 ):
        cls.nb_emplacement += nb_emplacement_supp




mon_clou = Clou(4)



mon_clou.clouer()




ma_vis = Vis("plate")

print(f"{ma_vis.statut=}")



mon_tournevis = Tournevis("plate")

mon_tournevis.vissage(ma_vis)


# print(f"{ma_vis.statut=}")

# mon_marteau = Marteau()

# # print(type(mon_marteau))
# # print(mon_marteau.__dict__)

# # mon_marteau.clouage(mon_clou)

# ma_toolbox = Toolbox()
# print(f"{ma_toolbox.contenu=}")

# ma_toolbox.add_tool(mon_marteau)
# ma_toolbox.add_tool(mon_tournevis)

# marteau_2 = Marteau()
# marteau_3 = Marteau()
# marteau_4 = Marteau()
# marteau_5 = Marteau()

# ma_toolbox.add_tool(marteau_2)
# ma_toolbox.add_tool(marteau_3)
# ma_toolbox.add_tool(marteau_4)
# ma_toolbox.add_tool(marteau_5)


# print(f"{ma_toolbox.contenu=}")

# ma_toolbox.update_toolbox(1)

# ma_toolbox.add_tool(marteau_5)

# print(f"{ma_toolbox.contenu=}")

