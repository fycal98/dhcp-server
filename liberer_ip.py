from sqlite3 import Timestamp
from parametres import * 
from time import sleep
from datetime import datetime

#cette function sera executer dans un autre thread , elle sert verrifier le temps de fin de services de addresse ip deja servis donc elle boocle chaque instant au cours de l'execution du programme
def verifier():
    while True :
        for ip in params.addresses_utiliser : 
            if ip['fin'] < datetime.timestamp(datetime.now()) : 
                params.addresses_utiliser.remove(ip)
                params.addresses_disponible.append(ip['addresse'])

        sleep(1)