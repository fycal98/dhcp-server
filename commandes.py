from asyncio.log import logger
import imp
from operator import add
from socket import *
from struct import *
import sys
import binascii
import dhcp_packet as dhcp
import copy
import scapy.all
from parametres import *
from datetime import datetime
import logging

#cette fonction gere les request dhcp et envois les reponces
def gerer_commandes(s : socket):
    print('le serveur est demaré')
    #initialiser les configuration des log
    logging.basicConfig(filename='dhcp.log',
                            filemode='a',
                            format='%(asctime)s,%(msecs)d %(name)s %(levelname)s %(message)s',
                            datefmt='%H:%M:%S',
                            level=logging.DEBUG)
    while True :
    
        #recevoir les request et les converter en hexadimal
        message, address = s.recvfrom(1024)
        hexvalue = binascii.hexlify(message).decode()  
        [hexvalue[i:i+2] for i in range(0, len(hexvalue), 2)]

        #converter le message du format hexadimal vers un object dhcp_packet
        packet = dhcp.dhcp_packet(hexvalue)
        
        # verifier si il saggit d'un message discover
        if packet.options['35'] == '01': 
            # envoyer un message offer
            offer = copy.deepcopy(packet)
            offer.op_code = '02'
            offer.y_ip = binascii.hexlify(inet_aton(params.addresses_disponible[0])).decode()
            offer.options = {}
            offer.options['35'] = '02'
            offer.options['01'] = binascii.hexlify(inet_aton(params.mask)).decode()
            offer.options['03'] = binascii.hexlify(inet_aton(params.gateway)).decode()
            offer.options['06'] = binascii.hexlify(inet_aton(params.dns1)).decode() + binascii.hexlify(inet_aton(params.dns2)).decode()
            offer.options['33'] = '{:x}'.format(params.temps_allocation).rjust(8,'0')
            offer.options['36'] = binascii.hexlify(inet_aton(s.getsockname()[0])).decode()
            scapy.all.sendp(scapy.all.Ether(dst=":".join(offer.chaddr[i:i+2] for i in range(0, len(offer.chaddr), 2)))/scapy.all.IP(dst="255.255.255.255")/scapy.all.UDP(dport=68,sport=67)/ offer.get_packet(),verbose= 0)
            

        # verifier si il saggit d'un message request
        if packet.options['35'] == '03':
            ack = copy.deepcopy(packet)
            ack.op_code = '02'
            try : 
                ack.y_ip = ack.options['32']
            except : 
                 pass
            ack.options = {}
            ack.options['35'] = '05'
            ack.options['01'] = binascii.hexlify(inet_aton(params.mask)).decode()
            ack.options['03'] = binascii.hexlify(inet_aton(params.gateway)).decode()
            ack.options['06'] = binascii.hexlify(inet_aton(params.dns1)).decode() + binascii.hexlify(inet_aton(params.dns2)).decode()
            ack.options['33'] = '{:x}'.format(params.temps_allocation).rjust(8,'0')
            
            ack.options['36'] = binascii.hexlify(inet_aton('0.0.0.0')).decode()
            scapy.all.sendp(scapy.all.Ether(dst=":".join(ack.chaddr[i:i+2] for i in range(0, len(ack.chaddr), 2)))/scapy.all.IP(dst="255.255.255.255")/scapy.all.UDP(dport=68,sport=67)/ ack.get_packet(),verbose=0,)
            #nous engistront l'evenement dans le fichier dhcp.log
            logging.info('nouvelle addresse attribuer au client : ' + ":".join(ack.chaddr[i:i+2] for i in range(0, len(ack.chaddr), 2))).__str__()
            # retirer l'addresse de la table des addresse disponible et l'ajouté a les addresse utiliser avec son temps de fin de services
            try : params.addresses_disponible.remove('.'.join(str(int(i, 16)) for i in ([ack.y_ip[i:i+2] for i in range(0, len(ack.y_ip), 2)]))) 
            except : pass
            params.addresses_utiliser.append({'addresse' :'.'.join(str(int(i, 16)) for i in ([ack.y_ip[i:i+2] for i in range(0, len(ack.y_ip), 2)])),'fin' : int(datetime.timestamp(datetime.now())) + params.temps_allocation})
            
        
        pass
    