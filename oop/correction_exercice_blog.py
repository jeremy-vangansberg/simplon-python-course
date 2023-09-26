"""
**'Exercice'** Ecrire le diagramme de classe correspondant au cas suivant:
Fort de votre expérience en pâtisserie, vous décidez de créer un forum en ligne pour parler de gâteaux ! 
- Vous devez définir et instancier trois classes: Utilisateurs (et ses héritiers), fil de discussion et post (et ses héritiers)


Sur ce forum
- les utilisateurs fans de pâtisserie pourront : s’inscrire et se connecter ;
- parler de leurs gâteaux préférés, en créant de nouveaux fils de discussion ;
- répondre à des messages, dans les fils existants.
- Un fil de discussion sur ce forum a un titre, une date de création et une collection de posts lui correspondant.
- Chaque post contient du texte, l’utilisateur qui l’a publié et la date de publication.
- Les utilisateurs ont la possibilité d’attacher des fichiers à leurs posts :
- Partez du principe qu’il peut y avoir de nombreux types de fichiers, mais nous sommes surtout intéressés par les fichiers images (GIF ou JPEP).
- Un post peut avoir un fichier attaché, ce qui changera la façon dont le post est affiché. Ce serait donc un nouveau type de post.
- Enfin, il y a des utilisateurs spéciaux nommés modérateurs, qui ont la capacité de modifier un post pour qu’il contienne du contenu nouveau, et de supprimer ceux qui ne parlent pas de gâteaux. ;)


**`Exercice user_creation`**

- créer une classe user avec un attribut publique "profil", des attribut protégés "password" et "user_name" et un attribut privée "validation_code"
- créer des méthodes publiques "set_password", "get_password" et "get_user_name"
- créer une méthode publique "set_username" qui prend comme argument un code et un nouveau user name. Cette méthode fait appelle à une autre méthode, privée cette fois qui compare le code avec le code de validation. Si le code correspond au validation_code alors le changement est réalisé.


 """

from datetime import datetime



class User:

    def __init__(self,profil,user_name,password):
        self.profil = profil
        self._password = self.set_password(password)
        self._user_name = user_name
        self.__validation_code = "XHDJFOD"
        

    def set_password(self, password):
        if isinstance(password,str) and len(password)>=8:
            return password
        else:
            print("le password de correspond pas")

    def get_password(self):
        return self._password

    def __validation(self,validation_code):
        return self.__validation_code == validation_code

    def set_username(self,new_user_name,validation_code):
        if self.__validation(validation_code):
            self._user_name = new_user_name
        else:
            print("erreur dans le code de validation")

    def get_user_name(self):
        return self._user_name
 

    def login(self, password):
        if self._password == password:
            self.statut = "connecté"
            print("vous etes bien connecté")
        else: 
            print("vous n'avez pas de compte ou mot de passe incorrect")

    def new_fil(self,fil:"Fil"):
        return fil

    def new_post(self,fil,post):
        fil.add_post(post)
        print(f"un nouveau post a été ajouté à {fil}")
        return post


class Moderateur(User):
    def modify_post(self,fil,post,new_text):
        if post in fil.contenu:
            post.texte = new_text


class Post:
    def __init__(self,utilisateur,texte):
        self.utilisateur = utilisateur
        self.texte = texte
        self.date_creation = datetime.now()

class Post_fichier(Post):
    def __init__(self,utilisateur,texte,type_fichier):
        super().__init__(utilisateur,texte)
        self.type_fichier = type_fichier

class Fil:

    def __init__(self,titre):
        self.contenu = []
        self.date_creation = datetime.now()
        self.titre = titre

    def add_post(self,post:Post):
        self.contenu.append(post)
        





charles = User("Actif","Charles","SecretKeys")

print(charles.get_password())

charles.set_username("charles B", "XHDJFOD")


print(charles.get_user_name())

charles.set_username("charles Be", "XHDJFO")

charles.__validation("XHDJFO")

# charles.sign_in(1234)
# charles.login(1234)

# mon_fil = Fil("carrotcake")


# print(f"{mon_fil.__dict__=}")

# mon_post=Post(charles,"le contenu de mon 1er poste")

# charles.new_post(mon_fil,mon_post)


# print(f"{mon_fil.contenu=}")

# denis = Moderateur("denis")

# denis.sign_in(9987)
# denis.login(9987)


# print(f"{mon_post.texte=}")

# denis.modify_post(mon_fil,mon_post, "un nouveau texte" )

# print(f"{mon_post.texte=}")

# mon_post_avec_fichier = Post_fichier(charles,"le contenu de mon 1er poste",type_fichier="GIF")

# print(f"{mon_post.__dict__=}")
