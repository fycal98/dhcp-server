from parametres import * 
def ligne_commande() : 
    aide = """cette ligne de commande permet de consulter létat du serveur, les adresses IP libres ou allouées et toutes autres informations . taper  : 
    'voir config' pour voir la configuration du servuer
    'voir ip disponible' pour voir la list des addresse disponible
    'voir ip servis' pour voir les addres servis
    'ip_debut' pour configurer la premier addresse
    'ip_fin' pour configurer le derinere addresse
    'dns1' pour configurer le premier dns
    'dns2' pour configurer le deuxieme dns
    'mask' pour configurer le mask du reseau
    'temps_allocation' pour configurer le temps d'allocation
    'aide' pour revoir ce guide de ligne de commande"""
    print(aide)
    while True :
        
        commande = input('dhcp-sorbonne> ')
        if commande == 'voir ip disponible' : print('\n'.join(params.addresses_disponible))
        if commande == 'voir ip servis' : print(params.addresses_utiliser)

        if commande == 'aide' : print(aide)
        if commande == 'voir config' : print('ip de debut : ' + params.ip_debut + '\n'+ 'ip de fin : ' + params.ip_fin + '\n'+ 'gateway : ' + params.gateway + '\n'+ 'serveur dns : ' + params.dns1  + '/'+ params.dns2 + '\n' + 'mask : ' + params.mask + '\n'+ 'temps d\'allocation : ' + str(params.temps_allocation))
        if commande.split(' ')[0].strip() == 'ip_debut' :params.edit(0,commande.split(' ')[1].strip()) 
        if commande.split(' ')[0].strip() == 'ip_fin' :params.edit(1,commande.split(' ')[1].strip()) 
        if commande.split(' ')[0].strip() == 'gateway' :params.edit(2,commande.split(' ')[1].strip()) 
        if commande.split(' ')[0].strip() == 'dns1' :params.edit(3,commande.split(' ')[1].strip()) 
        if commande.split(' ')[0].strip() == 'dns2' :params.edit(4,commande.split(' ')[1].strip()) 
        if commande.split(' ')[0].strip() == 'mask' :params.edit(5,commande.split(' ')[1].strip()) 
        if commande.split(' ')[0].strip() == 'temps_allocation' :params.edit(6,int(commande.split(' ')[1].strip())) 

        