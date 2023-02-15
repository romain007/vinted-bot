import sys

import platform

import requests

import json

import requests

import time

import os 

from discordwebhook import Discord

discord = Discord(url="https://discord.com/api/webhooks/1071118595465158706/lhD_LMD6azXszIuvZPuvX9ovwliPQQ1yMLveWpZYeHkPB_dRxaoDb20rXqM205iqHENG")



def poster(mess,clé):

    discord.post(

        username="BOT USER",

        avatar_url= "https://static.vecteezy.com/ti/vecteur-libre/p3/4437510-text-reading-bot-glyph-icon-screen-reader-application-virtual-assistant-robot-with-book-software-app-speech-synthesizer-silhouette-symbol-negative-space-vector-isolated-illustration-vectoriel.jpg",

        embeds=[{

            "title":"@ORAMI",

            "fields": [

                {"name": "MOIS_finit","value": f"{mess == 'end_mois'}"},

                {"name": "ESSAI_GRATUIT_finit","value": f"{mess == 'end_essai'}"},

                {"name": "clé_gratuit_entrer","value": f"{mess == 'gratuit'}"},

                {"name": "clé_payante_entrer","value": f"{mess == 'payant'}"},

                {"name": "key","value": f"{clé}" },

                {"name": "time","value": f"{time.time()}" } ]



        }],

    )



def mise_a_jour():

    liste = {"managment":"cibi2WMi",

            "bot" : "maVfn7if",

            "webhook" : "iEgsfTLL",

            "nouveauté" : "tbFbf0Uk",

            "recherche" : "j9HPRk9v",

            "loop" : "gN3wGt31"}

    try:

        time.sleep(10)

        with open(r"Data\managment.py","w", encoding="utf-8") as reload:

            response = requests.get(f"https://pastebin.com/raw/{liste['managment']}")

            reload.write(str(response.text))

            print("✅ file managment installé")

        time.sleep(10)

        with open(r"Discord\bot.py","w", encoding="utf-8") as reload:

            response = requests.get(f"https://pastebin.com/raw/{liste['bot']}")

            reload.write(str(response.text))

            print("✅ file bot installé")

        time.sleep(10)

        with open(r"Discord\webhook.py","w", encoding="utf-8") as reload:

            response = requests.get(f"https://pastebin.com/raw/{liste['webhook']}")

            reload.write(str(response.text))

            print("✅ file webhook installé")

        time.sleep(10)

        with open(r"Vinted\nouveauté.py","w", encoding="utf-8") as reload:

            response = requests.get(f"https://pastebin.com/raw/{liste['nouveauté']}")

            reload.write(str(response.text))

            print("✅ file nouveauté installé")

        time.sleep(10)

        with open(r"Vinted\recherche.py","w", encoding="utf-8") as reload:

            response = requests.get(f"https://pastebin.com/raw/{liste['recherche']}")

            reload.write(str(response.text))

            print("✅ file recherche installé")

        time.sleep(10)

        with open(r"loop.py","w", encoding="utf-8") as reload:

            response = requests.get(f"https://pastebin.com/raw/{liste['loop']}")

            reload.write(str(response.text))

            print("✅ file loop installé")

    except:

        print('⚠️  ERREUR FATALE // ECHEC DU TELECHARGEMENT DE LA MISE A JOUR')

        return "ECHEC"       

    return "SUCCES"





#Charge les clés

response = requests.get("https://pastebin.com/raw/3SWPtGs9")



data = json.loads(response.text)



#Récupere info_user

with open(r"\Data\info_user.txt","r+") as f:

    info = f.readlines()



#récupere info sur ordi

system_fingerprint = platform.uname()

ordi_info = [system_fingerprint.node , system_fingerprint.processor , system_fingerprint.system , system_fingerprint.release , platform.architecture()[0]  , system_fingerprint.machine ]



print("██╗   ██╗██╗███╗   ██╗████████╗███████╗██████╗     ██████╗  ██████╗ ████████╗")

print("██║   ██║██║████╗  ██║╚══██╔══╝██╔════╝██╔══██╗    ██╔══██╗██╔═══██╗╚══██╔══╝")

print("██║   ██║██║██╔██╗ ██║   ██║   █████╗  ██║  ██║    ██████╔╝██║   ██║   ██║ ")  

print("╚██╗ ██╔╝██║██║╚██╗██║   ██║   ██╔══╝  ██║  ██║    ██╔══██╗██║   ██║   ██║")   

print(" ╚████╔╝ ██║██║ ╚████║   ██║   ███████╗██████╔╝    ██████╔╝╚██████╔╝   ██║ ")  

print("  ╚═══╝  ╚═╝╚═╝  ╚═══╝   ╚═╝   ╚══════╝╚═════╝     ╚═════╝  ╚═════╝    ╚═╝  ")

print("██████╗ ██╗   ██╗     ██████╗ ██████╗  █████╗ ███╗   ███╗██╗")

print("██╔══██╗╚██╗ ██╔╝    ██╔═══██╗██╔══██╗██╔══██╗████╗ ████║██║")

print("██████╔╝ ╚████╔╝     ██║   ██║██████╔╝███████║██╔████╔██║██║")

print("██╔══██╗  ╚██╔╝      ██║   ██║██╔══██╗██╔══██║██║╚██╔╝██║██║")

print("██████╔╝   ██║       ╚██████╔╝██║  ██║██║  ██║██║ ╚═╝ ██║██║")

print("╚═════╝    ╚═╝        ╚═════╝ ╚═╝  ╚═╝╚═╝  ╚═╝╚═╝     ╚═╝╚═╝")

#Premier lancement

if info[6] != "False\n":

    

    token = input("🤖 Rentrez le token de votre bot discord : ")

    with open("Parametre\config.json","r") as file:

        config = json.load(file)

    config["token"] = token

    with open("Parametre\config.json","w") as configedit:

        json.dump(config,configedit,indent=4)

    

    key = input("🔑 Rentrez la clé d'activation : ")



    #Clé valide

    if key in data["vinted"]["clé"] or key in data["vinted"]["clé_gratuite"]:

        

        #Ecrit info user pour sécuriter

        with open(r"Data\info_user.txt","w") as f:

            for element in ordi_info:

                f.write(element+'\n' )

            f.write("False"+'\n')

            #version---

            f.write(data["vinted"]["version"]+'\n')

            f.write(str(key in data["vinted"]["clé_gratuite"])+'\n')

            f.write(str(time.time())+'\n')

            f.write(key)

        print("✅ Clé valide ! Logiciel activé, redémarrer le pour commencer")

        if key in data["vinted"]["clé"]:

            poster("payant",key)

        else:

            poster("gratuit",key)



    #quit

    else:

        print("❌ Clé non valide. Veuillez relancer le logiciel pour réessayer")

    sys.exit()



#Pas premier lancement

else:



    #Vérifier que c'est le meme ordi

    if [i.replace("\n","")for i in info][:6] == ordi_info:

        #Si essai gratuit

        if info[8] == "True\n" and ( time.time() - float(info[9]) ) > 3600*24*10 :

            print("❌ Essai gratuit expiré, ça fait 10 jours !\n Ecrit ton avis dans le serveur et si t'a bien aimer tu peux passer à l'offre vip,\n le seul changement est que tu pourras accéder au logiciel à vie ! Renseigne toi dans le serveur https://discord.gg/4RgD6WTZAs si ça te tente")

            poster("end_essai",info[10])

            with open(r"Data\info_user.txt","w") as f:

                f.write("0\n0\n0\n0\n0\n0\n0\n0\n0\n0\n")

            sys.exit()

        #Si mois a pris fin

        if info[8] == "False\n" and ( time.time() - float(info[9]) ) > 3600*24*30 :

            print("❌ ça fait un mois ! Si tu souhaite obtenir un accés pour le mois suivant, re-obtient le role vip. (ps: si tu as déja repayer, relance simplement le logiciel)")

            poster("end_mois",info[10])

            with open(r"Data\info_user.txt","w") as f:

                f.write("0\n0\n0\n0\n0\n0\n0\n0\n0\n0\n")

            sys.exit()

        #Vérifier que c'est la bonne version

        if int(info[7]) == int(data["vinted"]["version"]):

            print("🆗 Version à jour")

        else:

            print(f"🔃 Vous n'étes pas à jour, téléchargement de la dernière version [ {info[7]} -> {data['vinted']['version']} ] ...")

            if mise_a_jour() == "ECHEC":

                print("❌ Erreur de mise à jour, relance le logiciel pour réessayer, si ça ne marche pas contacte moi sur https://discord.gg/4RgD6WTZAs ")

                sys.exit()

            print("☑️  Mise à jour installer avec succès !")

            info[7] = data["vinted"]["version"]+'\n'

            with open (r"Data\info_user.txt","w") as finish:

                for i in info:

                    finish.write(i)

        

        #START

        os.system(r"py bot.py")



    

    

    else:

        print("❌ Un autre ordinateur est déjà attribuer à cette clé! Veuillez me contactez sur https://discord.gg/4RgD6WTZAs si ce n'est pas le cas.")

        sys.exit()