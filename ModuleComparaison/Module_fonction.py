

###Récuperation du nombre écrit###
def RequestNOMBRE():
    while True:
        str_nombretemp = input("Quel est le nombre ? ")
        if str_nombretemp.isnumeric():
            int_nombretemp = int(str_nombretemp)
            print(f"Votre nombre est le : '{int_nombretemp}'")
            return int_nombretemp  # "int_nombretemp" est la valeur temporaire donné renvoyé par la fonction
        else:
            print("Il faut renseigner un nombre")


###Comparaison du nombre avec le prix Amazon###
def CompareNOMBRE(nbrequest,nbprix):

    if nbrequest == nbprix:
        print(f"Bravo tu as trouvé le nombre mystère {nbprix} !")
        return False
    else:
        if nbrequest > nbprix:
            print(f"Moins grand")
        else:
            print(f"Plus grand")
        return True


###Fonction de comptage du nombre d'essaie###
def Count(i):
    #i = 0
    i += 1
    return i


###Affichage nomrbe de vie###
def Vie(int_resu,statut,prix):
    vie = 7
    if statut:
        if int_resu < vie:
            vie_restante = vie - int_resu
            print(f"Nombre de vie restante {vie_restante}")
            return True
        else:
            print("")
            print(f"Perdu !")
            print(f"Tu n'as plus de vie")
            print("")
            print(f"Le prix était {prix}€")
            return False
    else:
        print(f"Nombre de vie utilisé {int_resu}")
        return False


###Fonction demande du nom###
def RequestNOM(tabnom):
    while True:
        str_nom = input("Quel est ton prénom ? ")
        if str_nom == "":
            print(f"Il faut renseigner un prénom")
            # pass
        else:
            if not str_nom.isnumeric():
                tabnom.append(str_nom)
                return str_nom
            else:
                print("Il faut renseigner un prénom")

###Fonction ecriture du nom###

def AffichageNOM(nom):
    str_nom = str(nom)
    str_nom = str_nom.replace("['", "")
    str_nom = str_nom.replace("']", "")
    print(f"A toi de répondre {str_nom}")