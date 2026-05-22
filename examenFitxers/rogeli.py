elements = int(input("Quants elements vols registrar?"))
a=elements
b=[]

linia = []

while a!=0:
    b.append(a)
    a=a-1
with open ("inventari.txt", "w+t", encoding= "utf8") as write:
    
    for j in b:
        tipus= input("Quin tipus de producte es?  ")
        marca= input("De quina marca es?   ")
        numero= input("QUin es el numero de serie?  ")
        linia.append(tipus)
        linia.append(marca)
        linia.append(numero)
        
        write.writelines(linia)
        
        print (a, tipus, marca, numero)