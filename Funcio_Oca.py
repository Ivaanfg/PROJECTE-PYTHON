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


def fitxa1(tau, posi1,casella):
    fitxa = "@"
    inici = input("Vols llançar el dau ? S/N")
    if inici == "S":
        da = dau()
        casella = tau[posi1]
    if da == 1:
        posi1 += 1
        casella = tau[0][posi1]
        tau[0][posi1] = fitxa
    if da == 2:
        posi1 += 2
        casella = tau[0][posi1]
        tau[0][posi1] = fitxa
    if da == 3:
        posi1 += 3
        casella = tau[0][posi1]
        tau[0][posi1] = fitxa
    if da == 4:
        posi1 += 4
        casella = tau[0][posi1]
        tau[0][posi1] = fitxa
    if da == 5:
        posi1 += 5
        casella = tau[0][posi1]
        tau[0][posi1] = fitxa
    if da == 6:
        posi1 += 6
        casella = tau[0][posi1]
        tau[0][posi1] = fitxa
    return tau,posi1,casella


def fitxa2(tau, posi2,casella2):
    fitxa = "#"
    print("Turn del pc :")
    da = dau()
    casella2 = tau[posi2]
    if da == 1:
        posi2 += 1
        casella2 = tau[0][posi2]
        tau[0][posi2] = fitxa
    if da == 2:
        posi2 += 2
        casella2 = tau[0][posi2]
        tau[0][posi2] = fitxa
    if da == 3:
        posi2 += 3
        casella2 = tau[0][posi2]
        tau[0][posi2] = fitxa
    if da == 4:
        posi2 += 4
        casella2 = tau[0][posi2]
        tau[0][posi2] = fitxa
    if da == 5:
        posi2 += 5
        casella2 = tau[0][posi2]
        tau[0][posi2] = fitxa
    if da == 6:
        posi2 += 6
        casella2 = tau[0][posi2]
        tau[0][posi2] = fitxa

    return tau,posi2,casella2


def partida():
    començar_joc = input("Vols començar el joc? S/N")
    if començar_joc == "S":
        f2 = tauler()
        final = "si"
        posi1 = 0
        posi2 = 0
        while final == "si":
            f1,posi1,casella = fitxa1(f2,posi1,casella)
            print(f1)
            f2,posi2,casella2 = fitxa2(f1,posi2,casella2)
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
