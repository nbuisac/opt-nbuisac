import sqlite3

conn = sqlite3.connect('./empresa_hospital.db')
c = conn.cursor()

for nom, cognom, sou, departament in c.execute('SELECT first_name, last_name, salary, department_id FROM EMPLOYEES'):
    print(nom, cognom)
    d = conn.cursor()
    if departament != None:
        for nom_departament in d.execute(f"SELECT department_name from departments where department_id = {departament}"):
            print("Nom dept -> ", nom_departament[0])

for v in c.execute('SELECT first_name, last_name, salary, department_id FROM EMPLOYEES'):
    nom, cognom, sou, departament = v
    nom = v[0]
    cognom = v[1]
    sou = v[2]
    departament = v[3]