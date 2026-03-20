import csv

with open('contactes_exportats.csv', 'w', newline='') as csvfile:
    writer = csv.writer(csvfile, delimiter=';', quotechar='"', quoting=csv.QUOTE_STRINGS)
    q =0
    writer.writerow(['Nom', 'Telefon', q])
    q = q + 1
    writer.writerow(['mare', '666-555-444', q])
    q = q + 1
    writer.writerow(['pare', '678-123-456', q])
    q = q + 1
    writer.writerow(['germana', '654-321-098', q])
    q = q + 1
    writer.writerow(['amic', '675-483-921', q])
    q = q + 1
    writer.writerow(['avi, avia', '612-345-678', q])
    q = q + 1