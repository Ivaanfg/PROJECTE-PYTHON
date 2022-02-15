def dau():
    import random
    dado = random.randint(1, 6)
    print("Llançant el dau ...", "Ha sortit:", dado)
    return dado


def tauler():

    tablero = {0: ["[]", "[]", "[]", "[]", "[]", "[]", "[]", "[]", "[]", "[]", "[]",
                   "[]", "[]", "[]", "[]", "[]", "[]", "[]", "[]", "[]", "[]", "[]",
                   "[]", "[]", "[]", "[]", "[]", "[]", "[]", "[]", "[]", "[]", "[]",
                   "[]", "[]", "[]", "[]", "[]", "[]", "[]", "[]", "[]", "[]", "[]",
                   "[]", "[]", "[]", "[]", "[]", "[]", "[]", "[]", "[]", "[]", "[]",
                   "[]", "[]", "[]", "[]", "[]", "[]", "[]", "[]", "[]", "[]", "[]"]}
    for x in tablero:
        for y in tablero[x]:
            print(y, end="")
        print()
    print()
    return tablero

def fitxa1():

    tau = tauler()
    fitxa = "@"
    posi = 0
    casella = "[]"
    tirar = input("Vols tirar? S/N")

    while tirar != "N":
        da = dau()
        if da == 1:
            posi += 1
            casella = tau[0][posi]
            tau[0][posi] = fitxa
        elif da == 2:
            posi += 2
            casella = tau[0][posi]
            tau[0][posi] = fitxa
        elif da == 3:
            posi += 3
            casella = tau[0][posi]
            tau[0][posi] = fitxa
        elif da == 4:
            posi += 4
            casella = tau[0][posi]
            tau[0][posi] = fitxa
        elif da == 5:
            posi += 5
            casella = tau[0][posi]
            tau[0][posi] = fitxa
        elif da == 6:
            posi += 6
            casella = tau[0][posi]
            tau[0][posi] = fitxa
        else:
            print("D'acord")
    return tau



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
