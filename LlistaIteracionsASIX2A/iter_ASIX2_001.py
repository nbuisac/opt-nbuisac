# Verifiquem l'estat dels servidors.
# Tenim una llista de servidors i el seu estat (online/offline).
# Mostra només els que estan offline
# Creem les llistes
servidors = ["srv-web-01", "srv-db-01", "srv-app-01", "srv-backup-01", "srv-dns-01"]
estats = ["online", "offline", "online", "offline", "online"]

for i in range(len(servidors)):
    if estats[i] == "offline":
        print(f"⚠️ {servidors[i]} està offline")
print()
for servidor, estat in zip(servidors, estats):
    if estat == "offline":
        print(f"⚠️ {servidor} està offline")