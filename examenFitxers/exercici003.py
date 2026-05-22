nom_fitxer_input = "server.log"
nom_fitxer_output = "errors_critics.txt"

with open(nom_fitxer_input, "r", encoding="utf-8") as fl:
    with open(nom_fitxer_output, "a", encoding="utf-8") as fe:
        qt = 0
        qe = 0
        for linia in fl:
            qt = qt + 1
            # if linia[22:27] == "ERROR":
            if "ERROR" in linia:
                qe = qe + 1
                fe.write(linia)
    print(f"{qe} errors crítics en {qt} linies llegides")
