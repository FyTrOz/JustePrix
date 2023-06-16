from InformationAmazon.Amazon_main import *
from InformationAmazon.Amazon_fonction import *
from ModuleComparaison.Module_fonction import *
from ModuleComparaison.Module_main import *
from ModuleUser.User_main import *

###Appel des fonctions###

Echec = True

while Echec:
    try:
        Nom = UserConnexion()
        ITEM_object = FonctionMainAmazon()
        FonctionMainModule(ITEM_object, Nom)
        Echec = False
    except:
        pass

