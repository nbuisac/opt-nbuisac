import random
# ============================================================
# CREEM LES DADES INICIALS
# ============================================================
random.seed(10)
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
    ["Monitor Zabbix", 10050, "online", 0]}
]

## modifiquem l'estat d'alguns processos
for e in serveis:
    if random.random() < 0.6:
        e["estat"] = "offline"
    print(e["nom"], e["estat"])

## Comprovem un a un ...
for e in serveis:
    if e["estat"] == "online":
        print(f"✓ {e["nom"]} (port {e["port"]}): OPERATIU")