import mechanize
import time
from urllib.error import HTTPError

def encode_formated(str):  
    str = str.encode(encoding='latin1').decode()
    str_encoded = str.encode()
    str_decode = str_encoded.decode("utf-8")
    return str_decode

def search(url):
    """titre,price,url,photo,marque,devise,taille,date,hauteur,auteur_photo,id"""
    #Recherche
    br=mechanize.Browser()
    try:
        br.open(url)
        content = br.response().read().decode('utf-8', 'ignore')
    except HTTPError as e:
        print("⚠️  ERREUR NON FATALE // MAXIMUM DE REQUETE :",e)
        time.sleep(10)
        content = "ERROR"
    except :
        print("⚠️  ERREUR NON FATALE // URL NON VALIDE : ",url)
        content = "ERROR"
    br.close()
    return content