
def child_file_function():
    print ("I'm a child file function")
print(f"{__name__=}")

# cette condition permet de distinguer le code qui s'execute quand on run le script (tout) 
# du code qui s'execute quand on l'importe (le code qui  est en dehors de la condition)

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
    #pprint(sys.path)

    import Same_level
    print(Same_level.same_level_function("Child"))


    # Importtion d'un fichier depuis un fichier brother
    
    # de nouveau je dois trouver le chemin
    brotherdir = os.path.join(parentdir, "other_folder")

    # puis l'ajouter au python path
    sys.path.insert(0, brotherdir)

    import other_folder_file 
    print(other_folder_file.other_folder_function())

