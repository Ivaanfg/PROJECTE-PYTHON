def dau():
    import random
    dado = random.randint(1, 6)
    print("LlanΓ§ant el dau ...", "Ha sortit:", dado)
    return dado


def tauler():
    tablero = {0: ["[START]", "[]", "[]", "[π(coa)]", "[]", "[π(coa)]", "[]", "[]", "[πͺ(baix)]", "[]", "[]",
                   "[]", "[πͺ(baix)]", "[]", "[]", "[]", "[]", "[]", "[]", "[]", "[]", "[]",
                   "[π(coa)]", "[]", "[]", "[]", "[]", "[]", "[]", "[]", "[]", "[π(cap)]", "[πͺ(baix)]",
                   "[]", "[]", "[]", "[]", "[]", "[πͺ(dalt)]", "[πͺ(dalt)]", "[]", "[π(cap)]", "[]", "[π(coa)]",
                   "[πͺ(baix)]", "[]", "[]", "[πͺ(dalt)]", "[]", "[]", "[]", "[π(cap)]", "[]", "[]", "[]",
                   "[]", "[]", "[]", "[]", "[]", "[π(cap)]", "[πͺ(dalt)]", "[]", "[]", "[END]"]}
    for x in tablero:
        for y in tablero[x]:
            print(y, end="")
        print()
    print()
    return tablero


def fitxa(tau, posi, ID):
    guanyador = ""
    fitxa = "codi"
    anterior = 0
    if ID == 1:
        fitxa = "π¨"
        print("Turn del JUGADOR:")
    else:
        fitxa = "π₯"
        print("Turn del pc :")
    da = dau()
    posi += da
    if posi >= 65:
        print("Ha guanyat:", fitxa)
        posi = 65
    else:
        casella = tau[0][posi]
        tau[0][posi] = fitxa
        posi_anterior = posi - da


        psoicions_buies = [1, 2,4, 6,7,9,10, 11, 13,14, 15, 16, 17,18,19, 20, 21,23, 24, 25,26,27, 28, 29, 30, 33, 34, 35,36, 37,
                           40, 42, 45, 46,48, 49, 50, 52, 53,54, 55,56, 57,58,59,62, 63, 64]
        llista_escales_dalt = [38,39,47,61]
        llista_escales_baix = [8,12,32,44]
        llista_serps_dalt = [31,41,51,60]
        llista_serps_baix = [3,5,22,43]


        if posi_anterior == 0:
            tau[0][posi_anterior] = "[START]"

        if posi_anterior in psoicions_buies:
            tau[0][posi_anterior] = "[]"

        if posi_anterior in llista_serps_baix:
            tau[0][posi_anterior] = "[π(coa)]"

        if posi_anterior in llista_serps_dalt:
            tau[0][posi_anterior] = "[π(cap)]"

        if posi_anterior in llista_escales_baix:
            tau[0][posi_anterior] = "[πͺ(baix)]"

        if posi_anterior in llista_escales_dalt:
            tau[0][posi_anterior] = "[πͺ(dalt)]"

        if posi_anterior == 64:
            tau[0][posi_anterior] = "[END]"



        """ESCALES"""
        if fitxa in tau[0][8]:
            tau[0][39] = fitxa
            posi = 39
            tau[0][6] = "[πͺ(baix)]"
            print("Pujes fins la posiciΓ³ 39")


        elif fitxa in tau[0][12]:
            tau[0][38] = fitxa
            posi = 28
            tau[0][12] = "[πͺ(baix)]"
            print("Pujes fins la posiciΓ³ 38")

        elif fitxa in tau[0][32]:
            tau[0][47] = fitxa
            posi = 47
            tau[0][32] = "[πͺ(baix)]"
            print("Pujes fins la posiciΓ³ 47")

        elif fitxa in tau[0][44]:
            tau[0][61] = fitxa
            posi = 61
            tau[0][44] = "[πͺ(baix)]"
            print("Pujes fins la posiciΓ³ 61")

        """SERPS"""
        if fitxa in tau[0][31]:
            tau[0][3] = fitxa
            posi = 3
            tau[0][31] = "[π(coa)]"
            print("Baixes fins la posiciΓ³ 3")

        elif fitxa in tau[0][41]:
            tau[0][22] = fitxa
            posi = 22
            tau[0][41] = "[π(coa)]"
            print("Baixes fins la posiciΓ³ 22")

        elif fitxa in tau[0][51]:
            tau[0][5] = fitxa
            posi = 5
            tau[0][51] = "[π(coa)]"
            print("Baixes fins la posiciΓ³ 5")


        elif fitxa in tau[0][60]:
            tau[0][43] = fitxa
            posi = 43
            tau[0][60] = "[π(coa)]"
            print("Baixes fins la posiciΓ³ 43")





    return tau, posi, ID


def partida():
    comenΓ§ar_joc = input("Vols comenΓ§ar el joc? S/N")
    if comenΓ§ar_joc == "S":
        print("Jugador 1 : π¨")
        print("PC : π₯")
        f2 = tauler()
        posi1 = 0
        posi2 = 0
        while posi1 < 65:
            if posi1 == 65 or posi2 == 65:
                break
            pregunta = input("tirar S/N")
            if (pregunta == "S"):
                f1, posi1, ID = fitxa(f2, posi1, 1)
                print(posi1)
                print(f1)
                if posi1 == 65:
                    break
                f2, posi2, ID = fitxa(f1, posi2, 2)
                print(posi2)
                print(f2)
                if posi2 == 65:
                    break
