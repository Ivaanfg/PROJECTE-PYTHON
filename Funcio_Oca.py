def dau():
    import random
    dado = random.randint(1, 6)
    llancar = print("Llançant el dau ...", "Ha sortit:", dado )
    return llancar


def tauler():
    for x in tauler:
        for y in tauler[x]:
            print(y, end="")
        print()
    print()
    return tauler


def modtauler(taul, fila, columna, producto):
    if taul[fila][columna] == "-":
            taul[fila][columna] = "X"

    tablero = {0: ["", "-", "-", "-", "-"],
               1: ["-", "-", "-", "-", "-"],
               2: ["-", "-", "-", "-", "-"],
               3: ["-", "-", "-", "-", "-"],
               4: ["-", "-", "-", "-", "-"],
               5: ["-", "-", "-", "-", "-"]}

    tauler(tablero)
    modtauler(tablero, 2, 3, "s")
    tauler(tablero)
    
