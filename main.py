from InformationAmazon.Amazon_main import *
from InformationAmazon.Amazon_fonction import *
from ModuleComparaison.Module_fonction import *
from ModuleComparaison.Module_main import *

###Appel des fonctions###

Echec = True

while Echec:
    try:
        ITEM_object = FonctionMainAmazon()
        FonctionMainModule(ITEM_object)
        Echec = False
    except:
        pass


