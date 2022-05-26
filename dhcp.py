from socket import *
import threading
from commandes import *
from parametres import *
from liberer_ip import * 
from threading import Thread
from config import * 
from ligne_de_commande import * 

#initier les parametres de configuration
configure()

# demarerer une socket on mode datagrame sur le port 67
s = socket(AF_INET,SOCK_DGRAM)
s.bind(('',67))
s.setsockopt(SOL_SOCKET, SO_BROADCAST, 1)

# passer la socket en argument dans la fonction gerer_connections qui sera executer dans un autre thread
threading.Thread(target=gerer_commandes,args=(s,)).start()

# executer la fonction verifier dans un autre thread , cett fonction rend les addresse qui ont depasse leur temps de services disponible
threading.Thread(target=verifier).start()

# executer la fonction ligne_commande qui gere les commandes en ligne de commande permettront de configurer et consulter l’état du serveur
ligne_commande()










