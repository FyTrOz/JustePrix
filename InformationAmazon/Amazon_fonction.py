import os

import requests
from bs4 import BeautifulSoup

###Object###
class InfoARTICLE:
    def __init__(self):
        self.prix = ""
        self.description = ""
        self.image_url = ""


###Recuperation d'information d'une PAGE###
def InfoPAGE(URL):
    r = requests.get(URL)
    page = r.content
    soup = BeautifulSoup(page, "html.parser")
    return soup

###Récuperation des URL de la page best sellers###
def MainPAGE(soup,URL_BASE): # ok mais de la a importer un tableu vide?#C'est du scrap on casse les codes ici

    tabtemp = []
    div = soup.find("div", class_="_p13n-zg-nav-tree-all_style_zg-browse-group__88fbz")
    a_s = div.find_all("a")
    for a in a_s:
        item_url = URL_BASE + str(a.get("href"))
        tabtemp.append(item_url)
    return tabtemp




###Récuperation de la liste des articles###
def ListeITEM(Soup_PAGE):
    MainBOX = Soup_PAGE.find("div", class_="p13n-gridRow _cDEzb_grid-row_3Cywl")
    liste_ITEM = MainBOX.find_all("div", class_="a-column a-span12 a-text-center _cDEzb_grid-column_2hIsc")
    return liste_ITEM  # Renvoie de l'entièreté de la liste des articles de la 'Soup_PAGE'

###Récupération des champs articles###
def InfoITEM(ITEM):
    item = InfoARTICLE()
    item.description = ITEM.find_all("div")[7].text
    item.image_url = ITEM.find_all("div")[6].find("img").get("data-a-dynamic-image").split('"')[-2]
    item.prix = ITEM.find_all("div")[10].find("span", class_="p13n-sc-price").text

    return item  # La fonction retourne les objects 'item.description' item.image_url' 'item.prix'

###Arrondi du prix###
def ArrondiPRIX(prix_ITEM):
    edit_PRIX = prix_ITEM.replace("€", "").replace(",", ".").replace(" ", "")
    int_prix = int(float(edit_PRIX))
    return int_prix  # 'int_prix' est le prix arrondi qui est retourné par la fonction


###Telechargement une image avec son URL###
def DlIMAGE(url):
    r=requests.get(url)
    content = r.content
    file = "imgITEM.jpg"
    file_path = "Download/imgITEM.jpg"
    #file_path = "/config/home/PycharmProjects/JustePrix/Download/imgITEM.jpg"
    file = open(file_path, "wb")
    file.write(content)

