from slevel import add
from child_folder.child import divide


if __name__ == "__main__":
    import os
    import sys
    import inspect
    # Importation d'un fichier depuis un fichier parents
    # je recherche dans un premier temps le chemin de mon répertoire courant
    currentdir = os.path.dirname(os.path.abspath(inspect.getfile(inspect.currentframe())))
    # A partir de celui-ci je déduis le chemin de mon répertoire parent
    parentdir = os.path.dirname(currentdir)

    # J'ajoute le chemin de mon répertoire parent au "python path" 
    # qui est l'endroit ou la fonction import va chercher ce qu'elle est capable d'importer
    sys.path.insert(0, parentdir) 

    from pprint import pprint

    pprint(sys.path)

    from parent_file import multiply

    result = divide(multiply(add(5,2), 3),3)
    print(result)