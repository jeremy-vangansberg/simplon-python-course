from class_to_test import Voiture, Vehicule
# Tester une classe correspond à tester chacune de ses méthodes.
# Pour cela on crée une classe de test dont le nom commence par Test 
# Chacunes de ses méthodes permettra de tester les méthodes de la classe à tester
import pytest

class TestVoiture:

    def test_prix_apres_reduction(self):
        assert Voiture("toyota", "rouge",20000,0.1).prix_apres_reduction() == 18000

    def test_prix_apres_double_reduction(self):
        assert Voiture("toyota","rouge",20000,0.1).prix_apres_double_reduction() == 16000

    def test_prix_apres_triple_reduction(self):
        assert Voiture("toyota","rouge",20000,0.1).prix_apres_triple_reduction() == 14000
    
    def test_initialisation(self):
        assert Voiture("toyota","rouge",20000,0.1).prix == 20000
        with pytest.raises(ValueError) :
            Voiture("toyota","rouge","20000",0.1)
    
    def test_I_want_to_quit(self, monkeypatch):
        def no_func(x):
            pass
        #monkeypatch.setattr("class_to_test.Voiture.fonction_sans_fin",no_func)
        monkeypatch.setattr(Voiture, "fonction_sans_fin",no_func)
        #monkeypatch.delattr(Voiture, "fonction_sans_fin") (ne marche pas)

        assert Voiture("toyota","rouge",20000,0.1).I_want_to_quit() == "I quit"

# Je dois créer trois fois ma voiture. C'est plutot embettant. 

# Je peux préférer utiliser des fixtures

@pytest.fixture
def voiture_test():
   return Voiture("toyota","rouge",20000,0.1)


class TestVoiture2():
    def test_prix_apres_reduction(self,voiture_test):
        assert voiture_test.prix_apres_reduction() == 18000

    def test_prix_apres_double_reduction(self,voiture_test):
        assert voiture_test.prix_apres_double_reduction() == 16000

    def test_prix_apres_triple_reduction(self,voiture_test):
        assert voiture_test.prix_apres_triple_reduction() == 14000 

    def test_initialisation(self, voiture_test):
        assert voiture_test.prix == 20000
        with pytest.raises(ValueError) :
            Voiture("toyota","rouge","20000",0.1)



# Test an abstract class:
# Certaines abstract class possèdent des méthodes qui ne sont pas des abstact méthode
# On aimerait pouvoir les tester au niveau de la classe parent et pas plusieurs fois 
# Dans les classes enfant
class TestVehicule():
    def test_drive(self):
        #Cette ligne permet de supprimer toutes les abstactmethod
        Vehicule.__abstractmethods__ = set()
        # On peut donc instatancier un vehicule
        my_vehicule = Vehicule()
        # Et tester ses méthodes qui ne sont pas des abstractmethod
        assert my_vehicule.drive() == "the vehicule is on its wheels!"
