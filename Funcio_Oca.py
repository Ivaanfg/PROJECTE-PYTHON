def dau():
    import random
    dado = random.randint(1, 6)
    print("Llançant el dau ...", "Ha sortit:", dado)
    return dado


def tauler():

    tablero = {0: ["[]", "[]", "[]", "[]", "2", "__", "[]", "[]", "2", "[]", "[]"],
               1: ["__", "[]", "2", "[]", "[]", "[]", "2", "--", "[]", "[]", "[]"],
               2: ["2", "[]", "[]", "O", "2", "[]", "[]", "[]", "|__|", "2", "[]"],
               3: ["[]", "[]", "2", "[]", "[]", "[]", "[]", "2", "LA", "[]", "[]"],
               4: ["2", "[]", "[]", "[]", "[]", "2", "[]", "[]", "[]", "2", "[]"],
               5: ["||", "[]", "O", "2", "[]", "[]", "[]", ":(", "[]", "[]", "[]"]}

    for x in tablero:
        for y in tablero[x]:
            print(y, end="")
        print()
    print()
    return tablero

def fitxa_persona():
    #començar partida
    fitxa1 = "0"
    fitxa2 = "1"
    da = dau()
    tau = tauler()
    start = input("Vols començar la partida ? S/N")

    while start != "N":

        print("Ara comença la partida...")

        if da == 1:
            tau.update(fitxa1[1])
        if da == 2:
            tau.update(fitxa1[2])
        if da == 3:
            tau.update(fitxa1[3])
        if da == 4:
            tau.update(fitxa1[4])
        if da == 5:
            tau.update(fitxa1[5])
        if da == 6:
            tau.update(fitxa1[6])
    return tau
print(fitxa_persona())



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
