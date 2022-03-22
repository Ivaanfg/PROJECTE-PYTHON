print("La Oca = 1")
print("Escales i serps = 2")
print("Quien es quien = 3")
triar = int(input("A quin joc vols jugar? (1,2 o 3): "))
if triar == 1:
    from Funcio_Oca import dau,tauler,fitxa,partida
    print(partida())
if triar == 2:
    from escales_serps import dau,tauler,fitxa,partida
    prin(partida())
if triar == 3:
    from Quien_es_quien import pregunta,buclePc
    print(buclePc())
