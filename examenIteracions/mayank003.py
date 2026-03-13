#Tenim dues llistes que representen els paquets instal·lats en dos servidors diferents:
srv_a = ["apache2", "mysql", "php", "ufw", "openssh-server"]

srv_b = ["php","apache2","postgresql",  "openssh-server",  "nginx"]
#Fes un programa que calculi i mostri:
#Quins paquets estan instal·lats a tots dos servidors 
#Quins paquets estan al srv_b però no al srv_a 
dos_servidors=[]
si_no=[]
for i in srv_a:
    if i in srv_b:
        dos_servidors.append(i)
for i in srv_b:
    if i not in srv_a:
        si_no.append(i)
if len(dos_servidors)>0:
    print(f"Paquets estan instal·lats a tots dos servidors son->{dos_servidors}")
if len(si_no)>0:
    print(f"Paquets estan al srv_b però no al srv_a->{si_no}")

        