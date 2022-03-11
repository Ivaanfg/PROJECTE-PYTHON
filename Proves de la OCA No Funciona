def dau():
    import random
    dado = random.randint(1, 6)
    print("Llançant el dau ...", "Ha sortit:", dado)
    return dado


def tauler():
    tablero = {0: ["[START]", "[]", "[]", "[]", "[]", "[🦆]", "[🌉]", "[]", "[]", "[🦆]", "[]",
                   "[]", "[🌉]", "[]", "[🦆]", "[]", "[]", "[]", "[🦆]", "[🏠]", "[]", "[]",
                   "[]", "[🦆]", "[]", "[]", "[🎲]", "[🦆]", "[]", "[]", "[]", "[🕳️]", "[🦆]",
                   "[]", "[]", "[]", "[🦆]", "[]", "[]", "[]", "[]", "[🦆]", "[🐍]", "[]",
                   "[]", "[🦆]", "[]", "[]", "[]", "[]", "[🦆]", "[]", "[]", "[🎲]", "[🦆]",
                   "[]", "[⛓]", "[]", "[💀]", "[🦆]", "[]", "[]", "[]", "[]", "[]", "[END]"]}
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
        fitxa = "🟨"
        print("Turn del JUGADOR:")
    else:
        fitxa = "🟥"
        print("Turn del pc :")
    da = dau()
    posi += da
    casella = tau[0][posi]
    tau[0][posi] = fitxa
    posi_anterior = posi - da
    llista_oca = [5, 9, 14, 18, 23, 27, 32, 36, 41, 45, 50, 54, 59]
    psoicions_buies = [1, 2, 3, 4, 7, 8, 10, 11, 13, 15, 16, 17, 20, 21, 22, 24, 25, 28, 29, 30, 33, 34, 35, 37, 38, 39,
                       40, 43, 44, 46, 47, 48, 48, 51, 52, 53,55, 57, 60, 61, 62, 63, 64]
    if posi_anterior == 0:
        tau[0][posi_anterior] = "[START]"
    if posi_anterior in psoicions_buies:
        tau[0][posi_anterior] = "[]"
    if posi_anterior in llista_oca:
        tau[0][posi_anterior] = "[🦆]"
    if posi_anterior == 6 or posi_anterior == 12:
        tau[0][posi_anterior] = "[🌉]"
    if posi_anterior == 19:
        tau[0][posi_anterior] = "[🏠]"
    if posi_anterior == 31:
        tau[0][posi_anterior] = "[🕳]"
    if posi_anterior == 42:
        tau[0][posi_anterior] = "[🐍]"
    if posi_anterior == 56:
        tau[0][posi_anterior] = "[⛓]"
    if posi_anterior == 26 or posi_anterior == 53:
        tau[0][posi_anterior] = "[🎲]"
    if posi_anterior == 58:
        tau[0][posi_anterior] = "[💀]"
    if posi_anterior == 65:
        tau[0][posi_anterior] = "[END]"

    """OCA (Funciona be)"""
    if fitxa in tau[0][5]:
        tau[0][9] = fitxa
        posi += 4
        tau[0][5] = "[🦆]"
        print("De oca a oca y tiro porque me toca")
        da = dau()
        posi += da
        tau[0][posi] = fitxa
        tau[0][9] = "[🦆]"

    elif fitxa in tau[0][9]:
        tau[0][14] = fitxa
        posi += 5
        tau[0][9] = "[🦆]"
        print("De oca a oca y tiro porque me toca")
        da = dau()
        posi += da
        tau[0][posi] = fitxa
        tau[0][14] = "[🦆]"

    elif fitxa in tau[0][14]:
        tau[0][18] = fitxa
        posi += 4
        tau[0][14] = "[🦆]"
        print("De oca a oca y tiro porque me toca")
        da = dau()
        posi += da
        tau[0][posi] = fitxa
        tau[0][18] = "[🦆]"

    elif fitxa in tau[0][18]:
        tau[0][23] = fitxa
        posi += 5
        tau[0][18] = "[🦆]"
        print("De oca a oca y tiro porque me toca")
        da = dau()
        posi += da
        tau[0][posi] = fitxa
        tau[0][23] = "[🦆]"

    elif fitxa in tau[0][23]:
        tau[0][27] = fitxa
        posi += 4
        tau[0][23] = "[🦆]"
        print("De oca a oca y tiro porque me toca")
        da = dau()
        posi += da
        tau[0][posi] = fitxa
        tau[0][27] = "[🦆]"

    elif fitxa in tau[0][27]:
        tau[0][32] = fitxa
        posi += 5
        tau[0][27] = "[🦆]"
        print("De oca a oca y tiro porque me toca")
        da = dau()
        posi += da
        tau[0][posi] = fitxa
        tau[0][32] = "[🦆]"

    elif fitxa in tau[0][32]:
        tau[0][36] = fitxa
        posi += 4
        tau[0][32] = "[🦆]"
        print("De oca a oca y tiro porque me toca")
        da = dau()
        posi += da
        tau[0][posi] = fitxa
        tau[0][36] = "[🦆]"

    elif fitxa in tau[0][36]:
        tau[0][41] = fitxa
        posi += 5
        tau[0][36] = "[🦆]"
        print("De oca a oca y tiro porque me toca")
        da = dau()
        posi += da
        tau[0][posi] = fitxa
        tau[0][41] = "[🦆]"

    elif fitxa in tau[0][41]:
        tau[0][45] = fitxa
        posi += 4
        tau[0][41] = "[🦆]"
        print("De oca a oca y tiro porque me toca")
        da = dau()
        posi += da
        tau[0][posi] = fitxa
        tau[0][45] = "[🦆]"

    elif fitxa in tau[0][45]:
        tau[0][50] = fitxa
        posi += 5
        tau[0][45] = "[🦆]"
        print("De oca a oca y tiro porque me toca")
        da = dau()
        posi += da
        tau[0][posi] = fitxa
        tau[0][50] = "[🦆]"

    elif fitxa in tau[0][50]:
        tau[0][54] = fitxa
        posi += 4
        tau[0][50] = "[🦆]"
        print("De oca a oca y tiro porque me toca")
        da = dau()
        posi += da
        tau[0][posi] = fitxa
        tau[0][54] = "[🦆]"

    elif fitxa in tau[0][54]:
        tau[0][59] = fitxa
        posi += 5
        tau[0][54] = "[🦆]"
        print("De oca a oca y tiro porque me toca")
        da = dau()
        posi += da
        tau[0][posi] = fitxa
        tau[0][59] = "[🦆]"

    elif fitxa in tau[0][59]:
        tau[0][65] = fitxa
        posi += 6
        tau[0][59] = "[🦆]"


    """PONT(Funciona be)"""
    if fitxa in tau[0][6]:
        tau[0][12] = fitxa
        posi += 6
        tau[0][6] = "[🌉]"
        print("De pont a pont")

    elif fitxa in tau[0][12]:
        tau[0][6] = fitxa
        posi -= 6
        tau[0][12] = "[🌉]"
        print("De pont a pont")

    """LAVERINT (Funciona be"""
    if fitxa in tau[0][42]:
        tau[0][30] = fitxa
        posi -= 12
        tau[0][42] = "[🐍]"
        print("Has caigut al laverint perds 12 posicions")


    """DAUS (Funciona be)"""
    if fitxa in tau[0][26]:
        tau[0][53] = fitxa
        posi += 27
        tau[0][26] = "[🎲]"
        print("De dado a dado y tiro porque me ha tocado")
        da = dau()
        posi += da
        tau[0][posi] = fitxa


    elif fitxa in tau[0][53]:
        tau[0][26] = fitxa
        posi -= 27
        tau[0][53] = "[🎲]"
        print("De dado a dado y tiro porque me ha tocado")
        da = dau()
        posi += da
        tau[0][posi] = fitxa


    """MORT (Funciona Be"""
    if fitxa in tau[0][58]:
        tau[0][0] = fitxa
        posi -= 58
        tau[0][58] = "[💀]"
        print("Has caigut a la mort i tornes a la posició inicial")

    """FI (PENDENT DE REVISIO)"""
    if posi >= 65:
        """Si la fitxa no treu el nombre exacte de caselles per entrar, s'ha de restar el dau a la posició de la fitxa"""
        posi -= da
        tau[0][posi] = fitxa
    elif fitxa == tau[0][65]:
        guanyador = fitxa
        print("Ha guanyat :", guanyador)

    return tau, posi, ID


def partida():
    començar_joc = input("Vols començar el joc? S/N")
    if començar_joc == "S":
        print("Jugador 1 : 🟨")
        print("PC : 🟥")
        f2 = tauler()
        posi1 = 0
        posi2 = 0
        while posi1 != 65 or posi2 != 65:
            if posi1 == 65:
                print("Ha guanyat: 🟨")
                break
            if posi2 == 65:
                print("Ha guanyat: 🟥")
                break
            pregunta = input("tirar S/N")
            if (pregunta == "S"):
                f1, posi1, ID = fitxa(f2, posi1, 1)
                print(posi1)
                print(f1)
                """POSADA"""
                if posi1 == 19:
                    f2, posi2, ID = fitxa(f1, posi2, 2)
                    print("Has caigut a la posada perds 1 ronda")
                    print(f2)
                """POU"""
                if posi1 == 31:
                    f2, posi2, ID = fitxa(f1, posi2, 2)
                    print("Has caigut al pou perds 4 ronda")
                    print(f2)
                """CARCEL"""
                if posi1 == 56:
                    f2, posi2, ID = fitxa(f1, posi2, 2)
                    print("Has caigut a la carcel perds 2 ronda")
                    print(f2)
                f2, posi2, ID = fitxa(f1, posi2, 2)
                print(posi2)
                print(f2)
                """POSADA"""
                if posi2 == 19:
                    f1, posi1, ID = fitxa(f2, posi1, 1)
                    print("Has caigut a la posada perds 1 ronda")
                    print(f1)
                """POU"""
                if posi2 == 31:
                    f1, posi1, ID = fitxa(f2, posi1, 1)
                    print("Has caigut al pou perds 4 ronda")
                    print(f1)
                """CARCEL"""
                if posi2 == 56:
                    f1, posi1, ID = fitxa(f2, posi1, 1)
                    print("Has caigut a la carcel perds 2 ronda")
                    print(f1)



    return f2

print(partida())


