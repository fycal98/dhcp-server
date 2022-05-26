from parametres import * 
def configure() : 
    # verifier si il existe un fichier de configuration sinon crée un avec les parametres par default
    try : 
        f = open("dhcp.conf", "x")
        f.write("""ip_debut = 192.168.0.2
ip_fin = 192.168.0.254
gateway = 192.168.0.1
dns1 = 8.8.8.8
dns2 = 8.8.4.4
mask = 255.255.255.0
temps_allocation = 3600""")
        f.close()
    except : 
        pass
    f = open("dhcp.conf", "r")
    list = f.readlines()
    f.close()

    # initialiser les variables dans la class parametres
    params.ip_debut = list[0].split('=')[1]
    params.ip_fin = list[1].split('=')[1].strip()
    params.gateway = list[2].split('=')[1].strip()
    params.dns1 = list[3].split('=')[1].strip()
    params.dns2 = list[4].split('=')[1].strip()
    params.mask = list[5].split('=')[1].strip()
    params.temps_allocation = int(list[6].split('=')[1].strip())



    #initier la list des addresses ip disponibles
    i = 0
    while True :
        ip = params.ip_debut.split('.')[0] + '.'+ params.ip_debut.split('.')[1] + '.'+ params.ip_debut.split('.')[2] + '.'+ str(int(params.ip_debut.split('.')[3])+i)
        params.addresses_disponible.append(ip.strip())
        i +=1
        if ip == params.ip_fin or i > 255: break
        
       