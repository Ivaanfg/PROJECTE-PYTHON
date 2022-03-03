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
                   "[]", "[⛓]", "[]", "[💀]", "[🦆]", "[]", "[]", "[]", "[]", "[]", "[END]"]}
    for x in tablero:
        for y in tablero[x]:
            print(y, end="")
        print()
    print()
    return tablero


def fitxa(tau, posi, ID):
    guanyador = ""
    fitxa = "codi"
    anterior = 0
    if ID ==1:
        fitxa = "🟨"
        print("Turn del JUGADOR:")
    else:
        fitxa ="🟥"
        print("Turn del pc :")
    da = dau()
    posi += da
    casella = tau[0][posi]
    tau[0][posi] = fitxa
    posi_anterior = posi - da
    llista_oca = [5,9,14,18,23,27,32,36,41,45,50,54,59]
    psoicions_buies  = [1,2,3,4,7,8,10,11,13,15,16,17,20,21,22,24,25,28,29,30,33,34,35,37,38,39,40,43,44,46,47,48,48,51,52,53,57,60,61,62,63,64]
    if posi_anterior == 0:
       tau[0][posi_anterior]="[START]"
    if posi_anterior in psoicions_buies:
       tau[0][posi_anterior]="[]"
    if posi_anterior in llista_oca:
       tau[0][posi_anterior]="[🦆]"
    if posi_anterior == 6 or posi_anterior == 12:
       tau[0][posi_anterior]="[🌉]"
    if posi_anterior == 19:
       tau[0][posi_anterior]="[🏠]"
    if posi_anterior == 31:
       tau[0][posi_anterior]="[🕳]"
    if posi_anterior == 42:
       tau[0][posi_anterior]="[🐍]"
    if posi_anterior == 56:
       tau[0][posi_anterior]="[⛓]"
    if posi_anterior == 26 or posi_anterior == 53:
       tau[0][posi_anterior]="[🎲]"
    if posi_anterior == 58:
       tau[0][posi_anterior]="[💀]"
    if posi_anterior == 65:
       tau[0][posi_anterior]="[END]"
    

       
    """OCA"""    
    if fitxa  in tau[0][5]:
        fitxa = tau[0][9]
        posi += 4
        print(da)
    if fitxa  in tau[0][9]:
        fitxa = tau[0][14]
        posi += 5
        print(da)
    if fitxa  in tau[0][14]:
        fitxa = tau[0][18]
        posi += 4
        print(da)
    if fitxa  in tau[0][18]:
        fitxa = tau[0][23]
        posi += 5
        print(da)
    if fitxa  in tau[0][23]:
        fitxa = tau[0][27]
        posi += 4
        print(da)
    if fitxa  in tau[0][27]:
        fitxa = tau[0][32]
        posi += 5
        print(da)
    if fitxa  in tau[0][32]:
        fitxa = tau[0][36]
        posi += 4
        print(da)
    if fitxa  in tau[0][36]:
        fitxa = tau[0][41]
        posi += 5
        print(da)
    if fitxa  in tau[0][41]:
        fitxa = tau[0][45]
        posi += 4
        print(da)
    if fitxa  in tau[0][45]:
        fitxa = tau[0][50]
        posi += 5
        print(da)
    if fitxa  in tau[0][50]:
        fitxa = tau[0][54]
        posi += 4
        print(da)
    if fitxa  in tau[0][54]:
        fitxa = tau[0][59]
        posi += 5
        print(da)
    if fitxa  in tau[0][59]:
        fitxa = tau[0][65]
        posi += 6
        print(da)
    
    """PONT"""  
    if fitxa in tau[0][6]: 
        fitxa = tau[0][12]
        posi += 6
        
    if fitxa in tau[0][12]:
       fitxa = tau[0][6]
       posi -= 6
    
    """POSADA""" 
    if fitxa tau[0][19]:
        
    """POU""" 
    if fitxa tau[0][31]:
        
    """LAVERINT""" 
    if fitxa tau[0][42]:
        
    """CARCEL""" 
    if fitxa tau[0][56]:
        
    """DAUS""" 
    if fitxa tau[0][26]:
        fitxa = tau[0][53]
        posi += 27
        
    if fitxa tau[0][53]:
        fitxa = tau[0][26]
        posi -= 27
        
    """MORT""" 
    if fitxa tau[0][58]:
        fitxa = tau[0][0]
        posi -= 58
        
    """FI""" 
    if fitxa == tau[0][65]:
        guanyador = fitxa 
        print("Ha guanyat :",  guanyador)
        break
    
    return tau, posi,ID
    

    
    
def partida():

    començar_joc = input("Vols començar el joc? S/N")
    if començar_joc == "S":
        print("Jugador 1 : 🟨")
        print("PC : 🟥")
        f2 = tauler()
        posi1 = 0
        posi2 = 0
        while posi1 <= 65:
            pregunta = input("tirar S/N")
            if (pregunta == "S"):
                f1, posi1,ID = fitxa(f2, posi1,1)
                print(f1)
                f2, posi2,ID = fitxa(f1, posi2,2)
                print(f2)
        
       
    return f2
