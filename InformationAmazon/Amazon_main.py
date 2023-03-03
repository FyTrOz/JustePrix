###Que faut-il que je fasse (reprécise),
#on stocke les url que l'on a trouvé

###Ne pas oublier de faire un try except pour evité les bugs amazon###


from InformationAmazon.Amazon_fonction import InfoPAGE, MainPAGE, ListeITEM, InfoITEM, ArrondiPRIX, InfoARTICLE, DlIMAGE
import random


###Tableau###

tab_url = []


###Constante###

URL = 'https://www.amazon.fr/gp/bestsellers/ref=zg_mg_tab'

URL_BASE = "https://www.amazon.fr/"



###Appel des fonctions###

def FonctionMainAmazon():
    Soup_MAINPAGE = InfoPAGE(URL)

    liste_URLCATEGORIE = MainPAGE(Soup_MAINPAGE,URL_BASE)

    URLCATERGORIE = random.choice(liste_URLCATEGORIE)

    Soup_PAGE = InfoPAGE(URLCATERGORIE)

    liste_ITEM = ListeITEM(Soup_PAGE)

    ITEM = random.choice(liste_ITEM)

    ITEM_obj = InfoITEM(ITEM)

    arrondi_PRIX = ArrondiPRIX(ITEM_obj.prix)

    ITEM_obj.prix = arrondi_PRIX

    DlIMAGE(ITEM_obj.image_url)

    return ITEM_obj





