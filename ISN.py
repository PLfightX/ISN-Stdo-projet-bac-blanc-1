#Python 3.6
import getpass

alphabet = list("ABCDEFGHIJKLMNOPQRSTUVWXYZ")

def verif(mot): #on créé une fonction que vérifie si le mot est "correct": il fait 7 lettres de long et n'utilise que des lettres de l'alphabet
        legit = True
        if len(mot) == 7:
                for loop in range(7):
                        if mot[loop] in alphabet:
                                pass
                        else:
                                legit = False
        else:
                legit = False
        return legit #on retourne si le mot est correct ou non

sortie = 1
while sortie != 0: #on créé une boucle qui recommence le jeu jusqu'à ce que l'on l'arr?te
        print("Entrez votre nom Joueur 1") #le joueur 1 choisis un nom
        joueur1 = input()
        print("Entrez votre nom Joueur 2") #le joueur 2 choisis un nom
        joueur2 = input()

        mot = ""
        while not(verif(mot)): #le joueur 1 choisis un mot qu'on vérifie avec la fonction 'verif'
                mot = getpass.getpass("{0} entre le mot de 7 lettres : ".format(joueur1)).upper()  #on utilise getpass pour ne pas afficher le mot
        print("Mot validé")

        print("{0}, à toi".format(joueur2)) #c'est maintenant au joueur 2 de jouer
        for essais in range(6): #on créé une boucle avec 6 essais maximum
                proposition = ""
                reponse = ["."]*7
                while not(verif(proposition)):
                        proposition = input("Votre proposition (7 lettres) : ").upper() #On demande au joueur une proposition de mot
                propls = list(proposition)
                copy = list(mot)
                for lettre in range(7):
                        if propls[lettre] == copy[lettre]:
                                reponse[lettre] = mot[lettre]
                                propls[lettre] = "!"
                                copy[lettre] = "."
                for lettre in range(7):
                        if propls[lettre] in copy:
                                reponse[lettre] = propls[lettre].lower()
                                copy[copy.index(propls[lettre])] = "."
                print("".join(reponse))
                if "".join(reponse) == proposition: #on vérifie si la proposition après traitement est le mot qu'on doit deviner
                        print("Bien joué !")
                        break
        sortie = int(input("Voulez vous rejouer [1] ou quitter [0] ? ")) #On demande au joueur si on veut rejouer
