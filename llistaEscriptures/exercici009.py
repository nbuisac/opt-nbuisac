diners = float(input("Quants diners? "))
diners = int(diners * 100)

q = diners // 50000
if q > 0:
    print(q, "bitllets de 500")
diners = diners % 50000

q = diners // 20000
if q > 0:
    print(q, "bitllets de 200")
diners = diners % 20000

q = diners // 10000
if q > 0:
    print(q, "bitllets de 100")
diners = diners % 10000

q = diners // 5000
if q > 0:
    print(q, "bitllets de 50")
diners = diners % 5000

q = diners // 2000
if q > 0:
    print(q, "bitllets de 20")
diners = diners % 2000

q = diners // 1000
if q > 0:
    print(q, "bitllets de 10")
diners = diners % 1000

q = diners // 500
if q > 0:
    print(q, "bitllets de 5")
diners = diners % 500

q = diners // 100
if q > 0:
    print(q, "bitllets de 1")
diners = diners % 100

q = diners // 50
if q > 0:
    print(q, "monedes de 50")
diners = diners % 50

q = diners // 20
if q > 0:
    print(q, "monedes de 20")
diners = diners % 20

q = diners // 10
if q > 0:
    print(q, "monedes de 10")
diners = diners % 10

q = diners // 5
if q > 0:
    print(q, "monedes de 5")
diners = diners % 5

q = diners // 2
if q > 0:
    print(q, "monedes de 2")
diners = diners % 2

q = diners // 1
if q > 0:
    print(q, "monedes de 1")
diners = diners % 1

