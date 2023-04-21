import os
from ModuleComparaison.Module_fonction import RequestNOMBRE, CompareNOMBRE, Count, Vie, RequestNOM, AffichageNOM


###Information utile###



###Appel des fonctions###

def FonctionMainModule(ITEM_OBJECT):
    i = 0
    tabnom = []
    w_compare = True
    w_comptage = True

    print(f"Bienvenue dans le juste prix !")
    print(f"A toi de trouver le prix de de l'article qui va apparaitre")
    chaine_nom = RequestNOM(tabnom)
    os.system('clear')
    while w_compare and w_comptage:
        print(f"L'article à chercher est le : {ITEM_OBJECT.description}")
        print(f"Voici une image de l'article : {ITEM_OBJECT.image_url}")
        AffichageNOM(tabnom)
        nbdemande = RequestNOMBRE()
        os.system('clear')
        print(f"Le nombre précédent est : {nbdemande}")
        w_compare = CompareNOMBRE(nbdemande, ITEM_OBJECT.prix)
        Count_VIE = Count(i)
        i = Count_VIE
        w_comptage = Vie(Count_VIE, w_compare, ITEM_OBJECT.prix)
