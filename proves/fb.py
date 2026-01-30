import struct
# 1. Preparació: La llibreria struct
# La funció struct.pack(format, dades) converteix les dades en bytes segons un codi de format:
    # c	char	bytes de longitud 1	1 byte
    # s	char[]	bytes (string)	n bytes
    # ?	_Bool	bool	1 byte
    # h	short	int	2 bytes
    # i	int	int	4 bytes
    # q	long long	int	8 bytes
    # f	float	float	4 bytes
    # d	double	float	8 bytes

nom = "Usuari1"  # Cadena
edat = 25        # Integer
alcada = 1.75    # Float

format_registre = "10s i f"
# Calculem automàticament quants bytes ocupa aquest format
mida_esperada = struct.calcsize(format_registre)
print(f"El format requereix {mida_esperada} bytes")


# Codifiquem el nom a bytes (obligatori per a binari)
nom_bytes = nom.encode('utf-8')

nf = "binari.dat"
with open(nf, "bw") as fb:
    # Format: 10s (string de 10), i (int), f (float)
    # Nota: Si el nom és més curt de 10, struct l'omplirà amb bytes buits
    dades_binaries = struct.pack(format_registre, nom_bytes, edat, alcada)
    fb.write(dades_binaries)
print("Final Escriptura")

with open(nf, "rb") as f:
    # Llegim el bloc de bytes (10 + 4 + 4 = 18 bytes)
    contingut = f.read(mida_esperada)
    
    # Desempaquetem segons el format original
    nom_b, edat, alcada = struct.unpack(format_registre, contingut)
    
    # El nom vindrà amb bytes buits al final (\x00), els netegem i decodifiquem
    nom = nom_b.decode('utf-8').strip('\x00')
    
    print(f"Nom: {nom}, Edat: {edat}, Alçada: {alcada:.2f}")
print("Final Lectura")