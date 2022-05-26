class params : 
    addresses_disponible = []
    addresses_utiliser = []
    #les parametres configurable
    ip_debut = '192.168.1.2'
    ip_fin = '192.168.1.254'
    gateway = '192.168.1.1'
    dns1 = '8.8.8.8'
    dns2 = '8.8.4.4'
    mask = '255.255.255.0'
    temps_allocation = 3600
    @staticmethod
    def edit(option : int , value) : 
        if option == 0 : params.ip_debut = value
        if option == 1 : params.ip_fin = value
        if option == 2 : params.gateway = value
        if option == 3 : params.dns1 = value
        if option == 4 : params.dns2 = value
        if option == 5 : params.mask = value
        if option == 6 : params.temps_allocation = int(value)
        f = open("dhcp.conf", "w")
        f.write("ip_debut = " +  params.ip_debut + "ip_fin = " +  params.ip_fin + '\n' + "gateway = " +  params.gateway + '\n' + "dns1 = " +  params.dns1 + '\n' + "dns2 = " +  params.dns2 + '\n' + "mask = " +  params.mask + '\n' + "temps_allocation = " +  str(params.temps_allocation))
        f.close()