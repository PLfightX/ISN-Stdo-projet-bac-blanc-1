#Python 3.6
import getpass
import random

alphabet = list("ABCDEFGHIJKLMNOPQRSTUVWXYZ")

def readNbLettres():
    settingsFile = open("settings.conf", "r")
    settings = settingsFile.read()
    settingsFile.close()
    return int(settings)

def verif(mot, nbLettres = readNbLettres()): #on créé une fonction que vérifie si le mot est "correct": il fait le bon nombre de lettres de long et n'utilise que des lettres de l'alphabet
    legit = True
    if len(mot) == nbLettres:
        for loop in range(nbLettres):
            if mot[loop] in alphabet:
                pass
            else:
                legit = False
    else:
        legit = False
    return legit #on retourne si le mot est correct ou non

def multi():
    sortie = 1
    print("Entrez votre nom Joueur 1") #le joueur 1 choisis un nom
    joueur1 = input()
    print("Entrez votre nom Joueur 2") #le joueur 2 choisis un nom
    joueur2 = input()
    while sortie != 0: #on créé une boucle qui recommence le jeu jusqu'à ce que l'on l'arr?te
        
        mot = ""
        while not(verif(mot)): #le joueur 1 choisis un mot qu'on vérifie avec la fonction 'verif'
            mot = getpass.getpass("{0} entre le mot de {1} lettres : ".format(joueur1, readNbLettres())).upper()  #on utilise getpass pour ne pas afficher le mot
        print("Mot validé")

        print("{0}, à toi".format(joueur2)) #c'est maintenant au joueur 2 de jouer
        victoire = False
        for essais in range(6): #on créé une boucle avec 6 essais maximum
            proposition = ""
            reponse = ["."]*readNbLettres()
            while not(verif(proposition)):
                proposition = input("Votre proposition ({0} lettres) : ".format(readNbLettres())).upper() #On demande au joueur une proposition de mot
            propls = list(proposition)
            copy = list(mot)
            for lettre in range(readNbLettres()):
                if propls[lettre] == copy[lettre]:
                    reponse[lettre] = mot[lettre]
                    propls[lettre] = "!"
                    copy[lettre] = "."
            for lettre in range(readNbLettres()):
                if propls[lettre] in copy:
                    reponse[lettre] = propls[lettre].lower()
                    copy[copy.index(propls[lettre])] = "."
            print("".join(reponse))
            if "".join(reponse) == proposition: #on vérifie si la proposition après traitement est le mot qu'on doit deviner
                print("Bien joué {0} !".format(joueur2))
                victoire = True
                break
            
        if victoire == False:
            print("Vous avez échoué. La bonne réponse était {0}".format(mot))
        sortie = int(input("Voulez vous rejouer [1] ou revenir au menu [0] ? ")) #On demande au joueur si on veut rejouer
        mémoire = joueur1
        joueur1 = joueur2
        joueur2 = mémoire #On inverse les rôles pour la partie suivante
        

def solo():
    sortie = 1
    print("Entrez votre nom") #le joueur 1 choisis un nom
    joueur = input()
    while sortie != 0: #on créé une boucle qui recommence le jeu jusqu'à ce que l'on l'arrète
        listFile = open("list"+str(readNbLettres())+".motus", "r")
        liste = listFile.read().split("\n")
        listFile.close()
        mot = str(liste[random.randint(0, len(liste))]).upper()
        
        print("Un mot de {0} lettres a été choisi. {1}, à toi de jouer".format(readNbLettres(), joueur)) #c'est maintenant au joueur 2 de jouer
        victoire = False
        for essais in range(6): #on créé une boucle avec 6 essais maximum
            proposition = ""
            reponse = ["."]*readNbLettres()
            while not(verif(proposition)):
                proposition = input("Votre proposition ({0} lettres) : ".format(readNbLettres())).upper() #On demande au joueur une proposition de mot
            propls = list(proposition)
            copy = list(mot)
            for lettre in range(readNbLettres()):
                if propls[lettre] == copy[lettre]:
                    reponse[lettre] = mot[lettre]
                    propls[lettre] = "!"
                    copy[lettre] = "."
            for lettre in range(readNbLettres()):
                if propls[lettre] in copy:
                    reponse[lettre] = propls[lettre].lower()
                    copy[copy.index(propls[lettre])] = "."
            print("".join(reponse))
            if "".join(reponse) == proposition: #on vérifie si la proposition après traitement est le mot qu'on doit deviner
                print("Bien joué {0} !".format(joueur))
                victoire = True
                break
            
        if victoire == False:
            print("Vous avez échoué. La bonne réponse était {0}".format(mot))
        sortie = int(input("Voulez-vous rejouer [1] ou revenir au menu [0] ? ")) #On demande au joueur si on veut rejouer

def options():
    while True:
        print("OPTIONS\n[1] - Changer le nombre de lettres\n[2] - Ajouter un mot à la liste\n[3] - Retour")
        try:
            choix = int(input("Votre choix : "))
            if choix == 1:
                try:
                    nbLettres = input("Nombre de lettres (entre 6 et 9, vide pour par défaut) : ")
                    if nbLettres == "":
                        print("Valeur par défaut : 7")
                        nbLettres = 7 
                    elif int(nbLettres) >= 6 and int(nbLettres) <= 9:
                        print("Nombre de lettres défini sur {0}.".format(nbLettres))
                    else:
                        print("Incorrect, valeur par défaut : 7")
                        nbLettres = 7
                except ValueError:
                    print("Incorrect, valeur par défaut : 7")
                    nbLettres = 7
                settingsFile = open("settings.conf", "w")
                settingsFile.write(str(nbLettres))
                settingsFile.close()
            if choix == 2:
                try:
                    nbLettres = int(input("Combien de lettre le mot à ajouter a-t-il ? : "))
                    if nbLettres <= 9 and nbLettres >= 6:
                        print("Le mot ne peut contenir que les 26 lettres de l'alphabet")
                        mot = input("Le mot à ajouter : ").upper()
                        listFile = open("list"+str(nbLettres)+".motus", "r")
                        liste = listFile.read()
                        listFile.close()
                        if mot.lower() in liste:
                            print("Le mot existe déja !")
                        else:
                            try:
                                if verif(mot, nbLettres):
                                    mot = mot.lower()
                                    listFile = open("list"+str(nbLettres)+".motus", "a")
                                    listFile.write("\n"+mot)
                                    listFile.close()
                                    print("Mot Ajouté !")
                                else:
                                    print("Mot Incorrect !")
                            except TypeError:
                                print("Mot Incorrect !")
                    else :
                        print("Incorrect !")
                except ValueError:
                    print("Incorrect ! ")
            if choix == 3:
                break
        except ValueError:
            print("Incorrect !")

while True:
    print("Bienvenue dans Motus !\n[1] - Jouer en 1v1\n[2] - Jouer en solo\n[3] - Options\n[4] - Quitter")
    try:
        choix = int(input("Votre choix : "))
        if choix == 1:
            multi()
        if choix == 2:
            solo()
        if choix == 3:
            options()
        if choix == 4:
            raise SystemExit
    except ValueError:
        print("Incorrect !")
