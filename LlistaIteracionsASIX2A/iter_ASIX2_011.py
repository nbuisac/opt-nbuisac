# ============================================================
# CREEM LES DADES INICIALS
# ============================================================
import random
serveis = [
    {"nom": "Apache Web Server", "port": 80, "estat": "online", "intents_reinici": 0},
    {"nom": "MySQL Database", "port": 3306, "estat": "online", "intents_reinici": 0},
    {"nom": "DNS Bind", "port": 53, "estat": "online", "intents_reinici": 0},
    {"nom": "Correu Postfix", "port": 25, "estat": "online", "intents_reinici": 0},
    {"nom": "Monitor Zabbix", "port": 10050, "estat": "online", "intents_reinici": 0}
]

llista_serveis = [
    ["Apache Web Server", 80, "online", 0],
    ["MySQL Database", 3306, "online", 0],
    ["DNS Bind", 53, "online", 0],
    ["Correu Postfix", 25, "online", 0],
    ["Monitor Zabbix", 10050, "online", 0]
]
# random.seed(2)
for e in serveis:
    if random.random() < 0.7:
        e["estat"] = "offline"

