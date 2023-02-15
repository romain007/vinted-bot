# -*- coding: utf-8 -*-
import re
import json
import random

def moyenne(liste):
    return sum(liste)/len(liste)

def decoupage(source):
    """A partir d'un fichier html, trouve la partie json et la retourne"""
    #Découper le code source pour avoir que la partie json 
    # Mots début et fin à rechercher
    start_word = '{"catalogItems"'
    end_word = '"endReached"'
    ajout = ':false}}'
    # Rechercher la portion entre les mots début et fin
    match = re.search(f"{start_word}(.*?){end_word}", source, re.DOTALL)
    # Vérifier si la portion a été trouvée
    if match:
        # Extraire la portion trouvée et la stocker dans une variable
        result = match.group(1)
        json_part = f"{start_word}{result}{end_word}{ajout}"
    else:
        print('⚠️  ERREUR NON FATALE // PORTION NON TROUVER DANS LE CODE SOURCE DE LA RECHERCHE')
        json_part = '["ERROR"]'              
    return json_part

def formatage(string):
    """Formate un fichier json si erreur, retourne le fichier loader et corriger"""
    #Formater un fichier json pour qu'il soit lisible sans erreur
    condition = False
    while condition == False:
        #Essaye de load le json
        try:
            data=json.loads(string)
            condition = True
        #A la postion de l'erreur , remplace par la lettre E
        except json.decoder.JSONDecodeError as e:
            pos = e.pos
            string=list(string)
            string[pos] = ""
            print(e,"".join(string[pos-10:pos+10]))
            string = "".join(string)
            print("⚠️  ERREUR NON FATALE // CORECTION DU FICHIER EN COURS...")
    return data

def create_data(data_dict,recherche):
    """A partir des datas, crée un dictionnaire pour chaque item"""
    final_dico={}
    try:
        nb = len(data_dict['catalogItems']['ids'])
    except:
        nb = 1
    #Création d'un dictionnaire remplie de dictionnaire d'item
    for loop in range(nb):  
        #Crétion d'un dictionnaire d'un item
        dico={}
        try:
            dico["titre"] = data_dict['catalogItems']["byId"][str(data_dict['catalogItems']["ids"][loop])]["title"]
        except:
            dico["titre"] = "ERROR"
            print('⚠️  ERREUR NON FATALE // TITRE NON CHARGER')
        try:
            dico["price"] = data_dict['catalogItems']["byId"][str(data_dict['catalogItems']["ids"][loop])]["price"]
        except:
            dico["price"] = "ERROR"
            print('⚠️  ERREUR NON FATALE // PRICE NON CHARGER')
        try:
            dico["url"] = data_dict['catalogItems']["byId"][str(data_dict['catalogItems']["ids"][loop])]["url"]
        except:
            dico["url"] = "ERROR"
            print('⚠️  ERREUR NON FATALE // URL NON CHARGER')
        try:
            dico["photo"] = data_dict['catalogItems']["byId"][str(data_dict['catalogItems']["ids"][loop])]["photo"]["url"]
        except:
            dico["photo"] = "https://cdn.windowsreport.com/wp-content/uploads/2016/10/Error-code-930x620.jpg"
            print('⚠️  ERREUR NON FATALE // PHOTO NON CHARGER')
        try:
            dico["marque"] = data_dict['catalogItems']["byId"][str(data_dict['catalogItems']["ids"][loop])]["brand_title"]
        except:
            dico["marque"] = "ERROR"
            print('⚠️  ERREUR NON FATALE // MARQUE NON CHARGER')
        try:
            dico["devise"] = data_dict['catalogItems']["byId"][str(data_dict['catalogItems']["ids"][loop])]["currency"]
        except:
            dico["devise"] = "ERROR"
            print('⚠️  ERREUR NON FATALE // DEVISE NON CHARGER')
        try:
            dico["taille"] = data_dict['catalogItems']["byId"][str(data_dict['catalogItems']["ids"][loop])]["size_title"]
        except:
            dico["taille"] = "ERROR"
            print('⚠️  ERREUR NON FATALE // TAILLE NON CHARGER')
        try:
            dico["date"] = data_dict['catalogItems']["byId"][str(data_dict['catalogItems']["ids"][loop])]["photo"]["high_resolution"]["timestamp"]
        except:
            dico["date"] = 0
            print('⚠️  ERREUR NON FATALE // DATE NON CHARGER')
        try:
            dico["auteur"] = data_dict['catalogItems']["byId"][str(data_dict['catalogItems']["ids"][loop])]["user"]["login"]
        except:
            dico["auteur"] = "ERROR"
            print('⚠️  ERREUR NON FATALE // AUTEUR NON CHARGER')
        try:
            dico["auteur_photo"] = data_dict['catalogItems']["byId"][str(data_dict['catalogItems']["ids"][loop])]["user"]["photo"]["url"]
        except:
            dico["auteur_photo"] = "https://media.istockphoto.com/vectors/user-vector-id1138452882?k=6&m=1138452882&s=170667a&w=0&h=H31QWhznYhdGblAJX6Pp6RHcS6d6xF13D5L6wNJOQmc="
            print('⚠️  ERREUR NON FATALE // AUTEUR_PHOTO NON CHARGER')
        try:
            dico["id"] = str(data_dict['catalogItems']["ids"][loop])
        except:
            dico["id"] = random.randint(0,10000)
            print('⚠️  ERREUR NON FATALE // ID NON CHARGER')
        try:
            match = re.search("search_text=(.*?)&", recherche, re.DOTALL)
            match = match.group(1).replace("%20"," ")
            dico["recherche"] =  match
        except:
            dico["recherche"] =  "ERROR"
        try:
            dico["profile_url"] =  data_dict['catalogItems']["byId"][str(data_dict['catalogItems']["ids"][loop])]["user"]["profile_url"]
        except:
            dico["profile_url"] =  "ERROR"
            print('⚠️  ERREUR NON FATALE // PROFILE URL NON CHARGER')
        final_dico[loop] = dico    
    return final_dico     