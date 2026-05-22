import sqlite3
conn = sqlite3.connect(r"C:\Users\nbuisac\Desktop\APUNTS\opt-nbuisac\csv\gestio_vendes.db")
## SELECT d'una fila: Quantes comandes tenim
sql = "select count(*) from comanda"
c = conn.cursor()
resultat = c.execute(sql)
fila = resultat.fetchone()
print(f"{sql} -> {fila[0]}")

## SELECT de totes les comanes on total > 300 (variable)
sql = "select * from comanda where total > ?"
valor = 300
c = conn.cursor()
resultat = c.execute(sql, (valor,))
files = resultat.fetchall()
for f in files:
    print(f)

conn.commit()
conn.close()
