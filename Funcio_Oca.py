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

    da = dau()
    tau = tauler()
    fitxa = 0

    if da == 1:
        fitxa + 1
    if da == 2:
        fitxa + 2
    if da == 3:
        fitxa + 3
    if da == 4:
        fitxa + 4
    if da == 5:
        fitxa + 5
    if da == 6:
        fitxa + 6

    for fitxa in range(tau):
        tau.update([0,fitxa])

print(fitxa1())



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
