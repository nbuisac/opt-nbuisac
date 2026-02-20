# Creem les llistes
servidors = ["srv-web-01", "srv-db-01", "srv-app-01", "srv-backup-01", "srv-dns-01"]
estats = ["online", "offline", "online", "offline", "online"]
ser_est = {
    "srv-web-01": "online",
    "srv-db-01": "offline",
    "srv-app-01": "online",
    "srv-backup-01": "offline",
    "srv-dns-01": "online"
}

print("Servidors offline")
print("=" * 17)
for i in range(len(servidors)):
    if estats[i] == "offline":
        print(f"⚠️  {servidors[i]} està offline")
print()
print("Servidors offline")
print("=" * 17)
for servidor, estat in zip(servidors, estats):
    if estat == "offline":
        print(f"⚠️ {servidor} està offline")
