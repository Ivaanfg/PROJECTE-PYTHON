def tauler():
    taulerr = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10,
               11, 12, 13, 14, 15, 16, 17, 18, 19, 20,
               21, 22, 23, 24, 25, 26, 27, 28, 29, 30,
               31, 32, 33, 34, 35, 36, 37, 38, 39, 40,
               41, 42, 43, 44, 45, 46, 47, 48, 49, 50,
               51, 52, 53, 54, 55, 56, 57, 58, 59, 60,
               61, 62, 63]


def dau():
    import random
    llançar = print("Llançant el dau ...", "Ha sortit:", random.randint(1, 6))
    return llançar
#Exercici cultius per agafar de referencia per fer el taulell:
def printdici(printdici):
    for x in printdici:
        for y in printdici[x]:
            print(y, end="")
        print()
    print()


def cult(joan, fila, columna, producto):
    if joan[fila][columna] == "-":
        joan[fila][columna] = "X"
    else:
        print("ja hi ha un cultiu alla. ")
#from funcion import printdici,cult
campo = {0:["","-","-","-","-"],
        1:["-","-","-","-","-"],
        2:["-","-","-","-","-"],
        3:["-","-","-","-","-"],
        4:["-","-","-","-","-"],
        5:["-","-","-","-","-"]}

printdici(campo)
cult(campo,2,3,"s")
printdici(campo)
