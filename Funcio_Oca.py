def dau():
    import random
    dado = random.randint(1, 6)
    print("Llançant el dau ...", "Ha sortit:", dado)
    return dado


def tauler():

    tablero = {0: ["[]", "[]", "[]", "[]", "2", "__", "[]", "[]", "2", "[]", "[]"],
               1: ["__", "[]", "2", "[]", "[]", "[]", "2", "--", "[]", "[]", "[]"],
               2: ["2", "[]", "[]", "O", "2", "[]", "[]", "[]", "|_|", "2", "[]"],
               3: ["[]", "[]", "2", "[]", "[]", "[]", "[]", "2", "LA", "[]", "[]"],
               4: ["2", "[]", "[]", "[]", "[]", "2", "[]", "[]", "[]", "2", "[]"],
               5: ["||", "[]", "O", "2", "[]", "[]", "[]", ":(", "[]", "[]", "[]"]}


    for x in tablero:
        for y in tablero[x]:
            print(y, end="")
        print()
    print()


print(tauler())

def fitxa_persona():
    #començar partida
    start = input("Vols començar la partida ? S/N")
    fitxa1 = "0"
    fitxa2 = "1"
    da = dau()

    tau = tauler()
    while start != "N":
        if start == "S":
            print("Ara comença la partida...")
        if da == 1:
            tau.update(fitxa1[0]=[1])
        if da == 2:
            tau.update(fitxa1[0]=[2])
        if da == 3:
            tau.update(fitxa1[0]=[3])
        if da == 4:
            tau.update(fitxa1[0]=[4])
        if da == 5:
            tau.update(fitxa1[0]=[5])
        if da == 6:
            tau.update(fitxa1[0]=[6])
    return tau
print(fitxa_persona())





