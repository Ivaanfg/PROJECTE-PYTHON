def dau():
    import random
    dado = random.randint(1, 6)
    print("Llançant el dau ...", "Ha sortit:", dado)
    return dado


def tauler():

    tablero = {0: ["[START]", "[]", "[]", "[]", "[]", "[]", "[]", "[]", "[]", "[]", "[]",
                   "[]", "[]", "[]", "[]", "[]", "[]", "[]", "[]", "[]", "[]", "[]",
                   "[]", "[]", "[]", "[]", "[]", "[]", "[]", "[]", "[]", "[]", "[]",
                   "[]", "[]", "[]", "[]", "[]", "[]", "[]", "[]", "[]", "[]", "[]",
                   "[]", "[]", "[]", "[]", "[]", "[]", "[]", "[]", "[]", "[]", "[]",
                   "[]", "[]", "[]", "[]", "[]", "[]", "[]", "[]", "[]", "[]", "[END]"]}
    for x in tablero:
        for y in tablero[x]:
            print(y, end="")
        print()
    print()
    return tablero

def fitxa1(tau):

    fitxa = "@"
    posi = 0
    inici = input("Vols llançar el dau ? S/N")
    if inici == "S":
        da = dau()
        casella = "[]"
    if da == 1:
        posi += 1
        casella = tau[0][posi]
        tau[0][posi] = fitxa
    if da == 2:
        posi += 2
        casella = tau[0][posi]
        tau[0][posi] = fitxa
    if da == 3:
        posi += 3
        casella = tau[0][posi]
        tau[0][posi] = fitxa
    if da == 4:
        posi += 4
        casella = tau[0][posi]
        tau[0][posi] = fitxa
    if da == 5:
        posi += 5
        casella = tau[0][posi]
        tau[0][posi] = fitxa
    if da == 6:
        posi += 6
        casella = tau[0][posi]
        tau[0][posi] = fitxa
    return tau


def fitxa2(tau):

    fitxa = "#"
    posi = 0
    casella = "[]"
    print("Turn del pc :")
    da = dau()
    if da == 1:
        posi += 1
        casella = tau[0][posi]
        tau[0][posi] = fitxa
    if da == 2:
        posi += 2
        casella = tau[0][posi]
        tau[0][posi] = fitxa
    if da == 3:
        posi += 3
        casella = tau[0][posi]
        tau[0][posi] = fitxa
    if da == 4:
        posi += 4
        casella = tau[0][posi]
        tau[0][posi] = fitxa
    if da == 5:
        posi += 5
        casella = tau[0][posi]
        tau[0][posi] = fitxa
    if da == 6:
        posi += 6
        casella = tau[0][posi]
        tau[0][posi] = fitxa

    return tau

def partida():
    tab = tauler()
    f1 = fitxa1(tab)
    f2 = fitxa2(tab)
    començar_joc = input("Vols començar el joc? S/N")
    if començar_joc == "S":
        fa = input("Vols començar el joc? S/N")
        while fa != "N":
            print(f1)
            print(f2)
    else:
        print("Vale adeu...")



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
    
                 Start
start = input("Vols començar la partida ? S/N")

    while start != "N":

        print("Ara comença la partida...")
"""
