servidors = [
    "  WEB-01\n",
    "db-01  ",
    "  mail-server  ",
    "weB-01 ",
    "WEB-02\t",
    "  Proxy-01  "
]
servidors_nets = []
for s in servidors:
    s = s.strip()
    s = s.strip('\t')
    s = s.strip('\n')
    s = s.lower()
    if s in servidors_nets:
        print(f"Servidor {s} repetit")
    else:
        servidors_nets.append(s)
print("Llista de servidors -> ")
for s in servidors_nets:
    print(f"\t{s}")
print()