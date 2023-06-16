from ModuleUser.User_fonction import LectureBASE, EcritureBASE, ConnexionBASE, ChoixUSER


def UserConnexion():
    print(f"Bienvenue dans le juste prix !")

    i = True
    while i:
        Choix = ChoixUSER()
        if Choix == "inscription" or Choix == "connexion":
            if Choix == "connexion":
                Nom = ConnexionBASE()
                return Nom
            elif Choix == "inscription":
                EcritureBASE()
                print("Il faut maintenant te connecter")
                Nom = ConnexionBASE()
                return Nom
        elif Choix == "lire":
            LectureBASE()

    print(f"Un article va apparaitre à toi de trouver le prix de cet l'article")
