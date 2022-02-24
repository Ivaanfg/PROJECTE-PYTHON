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
                   "[]", "[⛓]", "[]", "💀", "[🦆]", "[]", "[]", "[]", "[]", "[]", "[END]"]}
    for x in tablero:
        for y in tablero[x]:
            print(y, end="")
        print()
    print()
    return tablero


def fitxa(tau, posi, ID):
    fitxa = "codi"
    anterior = 0
    if ID ==1:
        fitxa = "🟨"
    else:
        fitxa ="🟥"
    print("Turn del pc :")
    da = dau()
    posi += da
    casella = tau[0][posi]
    tau[0][posi] = fitxa

    return tau, posi,ID

def partida():

    començar_joc = input("Vols començar el joc? S/N")
    if començar_joc == "S":
        f2 = tauler()
        posi1 = 0
        posi2 = 0
        while posi1 <= 63:
            pregunta = input("tirar S/N")
            if (pregunta == "S"):
                f1, posi1,ID = fitxa(f2, posi1,1)
                print(f1)
                f2, posi2,ID = fitxa(f1, posi2,2)
                print(f2)


"""
def caselles_especials()
    taul = tauler()
    f1 = fi

    ocas = taul(5,9,14,18,23,27,32,36,41,45,50,54,59)
    puente = taul(6,12)
    posada = taul(19)
    pozo = taul(31)
    laberinto = taul(42)
    carcel = taul(56)
    dados = taul(26,53)
    calavera = taul(58)

    forx


"""
