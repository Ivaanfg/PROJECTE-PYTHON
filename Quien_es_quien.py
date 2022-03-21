import random

tableropc = {'Ivan': ["home", "pel curt", "pel negre", "ulls blaus", "nas petit","té barba"],
             'Joan': ["home", "pel curt", "pel roig", "ulls negres", "nas gran","té barba"],
             'Arnau': ["home", "pel curt", "pel negre", "ulls negres", "porta ulleres", "nas gran","té barba"],
             'Teresa': ["dona", "pel llarg", "pel roig", "ulls negres", "nas petit","té anelleta"],
             'Maria': ["dona", "pel llarg", "pel roig", "ulls blaus", "porta ulleres", "nas gran","té analleta"],
             'Susana': ["dona", "pel llarg", "pel negre", "ulls negres", "nas petit"],
             'Ramon': ["home", "pel llarg", "pel roig", "ulls blaus", "porta ulleres", "nas gran"],
             'Elisabeth': ["dona", "pel curt", "pel negre", "ulls negres", "porta ulleres", "nas petit"]}

tablerouser = {'Ferran': ["home", "pel curt", "pel roig", "ulls blaus", "nas petit","té barba"],
               'Miquel': ["home", "pel curt", "pel roig", "ulls negres", "nas gran"],
               'Llorenç': ["home", "pel curt", "pel negre", "ulls negres", "porta ulleres", "nas gran","té barba"],
               'Ramona': ["dona", "pel llarg", "pel roig", "ulls negres", "nas petit"],
               'Alicia': ["dona", "pel llarg", "pel negre", "ulls negres", "porta ulleres", "nas gran","porta anelleta"],
               'Abril': ["dona", "pel llarg", "pel negre", "ulls blaus", "nas petit"],
               'Albert': ["home", "pel llarg", "pel roig", "ulls blaus", "porta ulleres", "nas gran","té barba"],
               'Toni': ["dona", "pel curt", "pel negre", "ulls negres", "porta ulleres", "nas petit","porta anelleta"]}

preguntes = ["1 : ÉS HOME?","2 : PEL LLARG?", "3 : PEL NEGRE?","5 : ULLS NEGRES?",
             "6 : PORTA ULLERES?", "7 : NAS GRAN?","TÉ BARBA?","9 : PORTA ANELLETA?"]

respostesSi = ["home","pel llarg","pel negre","ulls negres","porta ulleres","nas gran","té barba","porta anelleta"]

respostesNo = ["dona","pel curt","pel roig","ulls blaus","no porta ulleres","nas petit"]


def pregunta(var,preg):

    if preg == "si":
        rem_key = {n_key: n_val for n_key, n_val in tablerouser.items() if n_val != respostesSi[var]}
        tablerouser.clear()
        tablerouser.update(rem_key)
        print([*tablerouser])
    else:
        rem_key = {n_key: n_val for n_key, n_val in tablerouser.items() if n_val == respostesNo[var]}
        tablerouser.clear()
        tablerouser.update(rem_key)
        print([*tablerouser])

def buclePc():

    while len(tablerouser) != 1:
        pregunta_num = random.randint(1, len(preguntes) -1)
        pregunta_pc = preguntes[pregunta_num]
        preguntes.pop(pregunta_num)
        print(pregunta_pc)
        resposta = input()
        pregunta(pregunta_num, resposta)

        if resposta == "si" in preguntes[0]: 
            for x in tablerouser:
                for y in tablerouser[x]:
                    if tablerouser[y] == "dona":
                        tablerouser.pop(x)

        if resposta == "si" in preguntes[1]:
            
        if resposta == "si" in preguntes[2]:
            
        if resposta == "si" in preguntes[3]:
            
        if resposta == "si" in preguntes[4]:
            
        if resposta == "si" in preguntes[5]:
            
        if resposta == "si" in preguntes[6]:
            
        if resposta == "si" in preguntes[7]:
            
        print(tablerouser)



buclePc()
