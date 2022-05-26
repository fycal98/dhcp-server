from struct import * 
import binascii
import struct

#cette class permet de cree un objet d'un packet dhcp pour simplifier le controle des requet et reponces dhcp 
class dhcp_packet :
    #la list des varible suivant est la list des champ d'un message dhcp
    op_code = ''
    hw_type = ''
    hw_addresse_lenght = ''
    hops = ''
    transaction_id = ''
    seconds = ''
    broadcast_flags = ''
    c_ip = ''
    y_ip = ''
    s_ip = ''
    g_ip = ''
    chaddr = ''
    client_mac_padding = ''
    server_name = ''
    filename = ''
    magic_cookie = '63825363'
    options = []
    
    #cette fonction est un constructeur qui repmli les valeur des champs a partir d'une requet recue 
    def __init__(self , data : str):
        self.op_code = data[0:2]
        self.hw_type = data[2:4]
        self.hw_addresse_lenght = data[4:6]
        self.hops = data[6:8]
        self.transaction_id = data[8:16]
        self.seconds = data[16:20]
        self.broadcast_flags = data[20:24]
        self.c_ip = data[24:32]
        self.y_ip = data[32:40]
        self.s_ip = data[40:48]
        self.g_ip = data[48:56]
        self.chaddr = data[56:68]
        self.client_mac_padding = data[68:88]
        self.server_name = data[88:216]
        self.filename = data[216:472]
        self.options = self._get_options(data[480:])
    
    #cette fonction permet d'obtenir les differntes options d'un message dhcp et les transformer a un dictionnere
    def _get_options(self,data : str) : 
        options = {}
        while not data.startswith('ff') : 
            options[data[0:2]] = data[4:(int(data[2:4],16))*2+4]
            #options.append({data[0:2]:data[4:(int(data[2:4],16))*2+4]})
            data = data[4+(int(data[2:4],16)*2):]
        return options
    
    #cette fonction permet d'obtenir un message dhcp pret a envoyer a partir des champs deja remplis
    def get_packet(self) : 
        packet = self.op_code + self.hw_type + self.hw_addresse_lenght + self.hops + self.transaction_id + self.seconds + self.broadcast_flags + self.c_ip + self.y_ip + self.s_ip + self.g_ip + self.chaddr + self.client_mac_padding + self.server_name + self.filename + self.magic_cookie
        for key, value  in self.options.items() : 
            if str(value.__len__()/2).__len__() % 2 == 0 : 
                packet = packet + key + str(int(value.__len__()/2)) + value
            else : 
                packet = packet + key + '0' +str(int(value.__len__()/2)) + value
        packet = packet + 'ff'
        packet = binascii.unhexlify(packet)
        return packet

