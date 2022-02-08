def dau():
    import random
    dado = random.randint(1, 6)
    print("Llançant el dau ...", "Ha sortit:", dado)
    return dado


def tauler():
    tirada = dau() 
    print("Turn del pc:", tirada)
    pc = "X"
    user = "O"
    tablero = {0: ["-", "-", "-", "-", "-", "-", "-", "-"],
               1: ["-", "-", "-", "-", "-", "-", "-", "-"],
               2: ["-", "-", "-", "-", "-", "-", "-", "-"],
               3: ["-", "-", "-", "-", "-", "-", "-", "-"],
               4: ["-", "-", "-", "-", "-", "-", "-", "-"],
               5: ["-", "-", "-", "-", "-", "-", "-", "-"],
               6: ["-", "-", "-", "-", "-", "-", "-", "-"],
               7: ["-", "-", "-", "-", "-", "-", "-", "-"]}
    if tirada == 1:
        tablero.
        
    
    return tablero

#Funcio Tablero 
def mostrar_tablero():
    tablero = {0: ["-", "-", "-", "-", "-"],
               1: ["-", "-", "-", "-", "-"],
               2: ["-", "-", "-", "-", "-"],
               3: ["-", "-", "-", "-", "-"],
               4: ["-", "-", "-", "-", "-"],
               5: ["-", "-", "-", "-", "-"]}
    for x in tablero:
        for y in tablero[x]:
            print(y, end="")
        print()
    print()
#Print per mostrar la funcio del tablero com funciona.
print(mostrar_tablero())
