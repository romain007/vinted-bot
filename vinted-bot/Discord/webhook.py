# -*- coding: utf-8 -*-
from discordwebhook import Discord
import datetime

def discord_send(item,webhook):

    discord = Discord(url=webhook)

    result = item["recherche"]
    title = item["titre"] 
    price = item["price"]
    devise = item["devise"]
    url = item["url"]
    photo = item["photo"]
    marque = item["marque"]
    date = item["date"]
    auteur = item["auteur"]
    auteur_photo = item["auteur_photo"]
    taille = item["taille"]
    prix_moyen = item["prix_moyen"]
    print("↗️  L'item a été envoyé ---------")
    discord.post(
        username="BOT VINTED",
        avatar_url= "https://static.vecteezy.com/ti/vecteur-libre/p3/4437510-text-reading-bot-glyph-icon-screen-reader-application-virtual-assistant-robot-with-book-software-app-speech-synthesizer-silhouette-symbol-negative-space-vector-isolated-illustration-vectoriel.jpg",
        embeds=[{
            "title": f"{title}",
            "fields": [
                {"name": "💸Prix","value": f"{price} {devise}","inline": True},
                {"name": "📈Prix_moyen","value": f"{prix_moyen} {devise}","inline": True},
                {"name": "👟Marque","value": f"{marque}","inline": True},
                {"name": "📏Taille","value": f"{taille}","inline": True},
                {"name": "👤Vendeur","value": f"{auteur}","inline": True},
                {"name":"🔎Recherche associé","value":f"{result}","inline": True},
                {"name":"📅Date","value":f"{datetime.datetime.fromtimestamp(date).isoformat()}","inline": True},
                {"name":"🤖Obtenez votre propre bot vinted ici :","value":"https://discord.gg/4RgD6WTZAs"},
            ],
            "image": {
                "url": f"{photo}"
            },
            "thumbnail": {"url": f"{auteur_photo}","name":"vendeur","value":f'{auteur}'},
            "footer": {
                "text": "Powered by 𝙎𝙐𝙋𝙀𝙍𝘽𝙊𝙏-🛒Achat et 💸Revente 💰Business, logiciel sous license tout droit réservé ©",
            },
            "author": {
                "name": "CLIQUER ICI POUR VOIR LE PRODUIT",
                "url": f"{url}",
            "icon_url": "https://news.chastin.com/wp-content/uploads/2021/05/vinted.jpg",
            }
        }],
    )