# -*- coding: utf-8 -*-

from Data.managment import *

from Discord.webhook import *

from Vinted.nouveauté import *

from Vinted.recherche import *



lien = r"Parametre\config.json"



def all_object(url):

    #Fais une recherche

    source = search(url)

    #Découper le code source pour avoir que la partie json 

    json_file = decoupage(source)

    #Formater le fichier json pour qu'il soit lisible sans erreur

    json_file_formated = formatage(json_file)

    #Extraire info interresante du json et création de data

    data = create_data(json_file_formated,url)

    return data



def main():



    liste_id = []



    with open (lien,'r') as file:

        parametre = json.load(file)

    #Run

    while parametre["stop"] == "False": 

        #Paramètre----------------------------------------

        with open (lien,'r') as file:

            parametre = json.load(file)



        params={}

        count=0

        for i in parametre["suburl"]:

            params2={}

            params2["BOT"] = i

            params2["URL"] = parametre["suburl"][i]["url"] 

            params[count] = params2

            count=count+1

        #--------------------------------------------------  

                    

        #Actualise tous les salons

        for loop in range(len(params)):

            #Recherche d'item pour un salon

            items = all_object(params[loop]["URL"])

            #moyenne price
            moyenne_price = int(moyenne([float(items[i]["price"]) for i in range(len(items))]))

            for element in items:
                items[element]["prix_moyen"] = moyenne_price

                if isNew(items[element],parametre["cooldown"]) and items[element]["id"] not in liste_id:

                    discord_send(items[element],params[loop]["BOT"])

                    time.sleep(3)

                    liste_id.append(items[element]["id"])     

            print("✅ SALON NUMERO ", loop, "ACTUALISER")

            time.sleep(5)

        time.sleep(5)