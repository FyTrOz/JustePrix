import json

i = True


class Character:
    def __init__(self, nom, pin):
        self.nom = nom
        self.pin = pin
        self.record = 0
        self.last_score = 0


def ChoixUSER():
    i = True
    while i:
        print("Dans un premier temps, Connecte toi ou Inscrit toi !")
        request = input("Connexion ou Inscription ('c'/'i') : ")
        if request == "Connexion" or request == "connexion" or request == "c":
            return "connexion"
        elif request == "Inscription" or request == "inscription" or request == "i":
            return "inscription"
        elif request == "l":
            return "lire"
        else:
            print("Veuillez bien ecrire")
            print("--------------------")

def LectureBASE():
    try:
        print("Entrée dans la base")
        fileObject = open("data.json", "r")
        jsonContent = fileObject.read().strip()
        aList = json.loads(jsonContent)
        for item in aList:
            for key, value in item.items():
                print(f"{key}: {value}")
            print()  # imprime une ligne vide entre chaque dictionnaire
        fileObject.close()

    except:
        print("Vous ne pouvez pas lire car le fichier et vide ou inexistant")
        pass




def EcritureBASE():
    w_nom = True
    while w_nom:
        nom_give = input("Quel ton nom ? : ")
        if not nom_give.isnumeric():
            str_nom_give = str(nom_give)
            print(f"Bonjour {str_nom_give}")
            w_nom = False
        else:
            print("Il faut renseigner une chaine de caractère")
    w_pin = True
    while w_pin:
        pin_give = input("Quel est ton code PIN ? : ")
        if pin_give.isnumeric():
            int_pin_give = int(pin_give)
            print(f"Votre nom est {str_nom_give} et votre code PIN est le : '{pin_give}'")
            w_pin = False
        else:
            print("Il faut renseigner un nombre")

    character = Character(nom_give, pin_give)

    jsonString = json.dumps(character.__dict__)
    print(jsonString)
    # Ouverture en mode lecture pour lire le contenu actuel
    jsonFile = open("data.json", "r")
    jsonContent = jsonFile.read()
    jsonFile.close()

    # Ajout de la nouvelle ligne au contenu existant
    if len(jsonContent) > 0:
        jsonContent = jsonContent[:-1] + "," + "\n" + jsonString + "]"
    else:
        jsonContent = "[" + jsonString + "]"

    # Ouverture en mode écriture pour écrire le nouveau contenu
    jsonFile = open("data.json", "w")
    jsonFile.write(jsonContent)
    jsonFile.close()
    print("Inscription Validé")
    print("------------------")



def ConnexionBASE():
    i = True
    while i:
        fileObject = open("data.json", "r")
        jsonContent = fileObject.read().strip()
        playerList = json.loads(jsonContent)

        # Demande des informations
        foundPlayer = None
        foundPin = None

        w_playerName = True
        while w_playerName:
            playerName_give = input("Entrez le nom du joueur : ")
            if not playerName_give.isnumeric():
                str_playerName_give = str(playerName_give)
                trouver = False
                for player in playerList:
                    if player["nom"] == str_playerName_give:
                        foundPlayer = player
                        trouver = True
                        break
                if not trouver:
                    print("Le joueur est introuvable")
                else:
                    w_playerName = False
            else:
                print("Il faut renseigner une chaine de caractère")


        if foundPlayer != None:
            w_playerPin = True
            while w_playerPin:
                    playerPin_give = input("Entrez le code PIN du joueur : ")
                    if playerPin_give.isnumeric():
                        str_playerPin_give = str(playerPin_give)
                        for player in playerList:
                            if player["pin"] == str_playerPin_give:
                                foundPin = player
                                w_playerPin = False
                            else:
                                print("Pin incorrect")
                    else:
                        print("Il faut renseigner un nombre pour le code pin")

        if foundPin:
            print("-------------------------")
            print("Récapitulatif du compte :")
            print("Nom : ", foundPlayer["nom"])
            print("Record : ", foundPlayer["record"])
            print("Dernier score : ", foundPlayer["last_score"])
            print("-------------------------")

        else:
            print("Joueur introuvable ou code PIN incorrect.")

        return(foundPlayer["nom"])

        fileObject.close()
        fileObject.close()
