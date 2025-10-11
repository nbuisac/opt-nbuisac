diners = float(input("Quants diners? "))
diners = int(diners * 100)

q = diners // 50000
if q > 0:
    print(q, "bitllets de 500 euros")
diners = diners % 50000

q = diners // 20000
if q > 0:
    print(q, "bitllets de 200 euros")
diners = diners % 20000

q = diners // 10000
if q > 0:
    print(q, "bitllets de 100 euros")
diners = diners % 10000

q = diners // 5000
if q > 0:
    print(q, "bitllets de 50 euros")
diners = diners % 5000

q = diners // 2000
if q > 0:
    print(q, "bitllets de 20 euros")
diners = diners % 2000

q = diners // 1000
if q > 0:
    print(q, "bitllets de 10 euros")
diners = diners % 1000

q = diners // 500
if q > 0:
    print(q, "bitllets de 5 euros")
diners = diners % 500

q = diners // 200
if q > 0:
    print(q, "monedes de 2 euros")
diners = diners % 100

q = diners // 100
if q > 0:
    print(q, "monedes de 1 euro")
diners = diners % 100

q = diners // 50
if q > 0:
    print(q, "monedes de 50 cents")
diners = diners % 50

q = diners // 20
if q > 0:
    print(q, "monedes de 20 cents")
diners = diners % 20

q = diners // 10
if q > 0:
    print(q, "monedes de 10 cents")
diners = diners % 10

q = diners // 5
if q > 0:
    print(q, "monedes de 5 cents")
diners = diners % 5

q = diners // 2
if q > 0:
    print(q, "monedes de 2 cents")
diners = diners % 2

## Aquest darrer no cal ja que és de 1
#  podem escriure directament diners
q = diners // 1
if q > 0:
    print(q, "monedes de 1 cent")
diners = diners % 1