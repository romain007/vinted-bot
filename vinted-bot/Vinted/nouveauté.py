# -*- coding: utf-8 -*-
import time
def isNew(objet,temps):
    """Temps en minute"""
    return (time.time() - int(objet["date"])) < temps*60