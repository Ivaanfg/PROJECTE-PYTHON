import random

tableropc = {'Ivan': ["home", "pel curt", "pel negre", "ulls blaus","no porta ulleres","nas petit","té barba","no té anelleta"],
             'Joan': ["home", "pel curt", "pel roig", "ulls negres","no porta ulleres","nas gran", "té barba","no té anelleta"],
             'Arnau': ["home", "pel curt", "pel negre", "ulls negres", "porta ulleres", "nas gran", "té barba","no té anelleta"],
             'Teresa': ["dona", "pel llarg", "pel roig", "ulls negres","no porta ulleres", "nas petit","no té barba","té anelleta"],
             'Maria': ["dona", "pel llarg", "pel roig", "ulls blaus", "porta ulleres", "nas gran","no té barba","té analleta"],
             'Susana': ["dona", "pel llarg", "pel negre", "ulls negres","no porta ulleres", "nas petit","no té barba","no té anelleta"],
             'Ramon': ["home", "pel llarg", "pel roig", "ulls blaus", "porta ulleres", "nas gran","no té barba","no té anelleta"],
             'Elisabeth': ["dona", "pel curt", "pel negre", "ulls negres", "porta ulleres", "nas petit","no té barba","no té anelleta"]}

tablerouser = {'Ferran': ["home", "pel curt", "pel roig", "ulls blaus", "nas petit", "té barba","no té anelleta"],
               'Miquel': ["home", "pel curt", "pel roig", "ulls negres", "nas gran","no té barba","no té anelleta"],
               'Llorenç': ["home", "pel curt", "pel negre", "ulls negres", "porta ulleres", "nas gran", "té barba","no té anelleta"],
               'Ramona': ["dona", "pel llarg", "pel roig", "ulls negres", "nas petit","no té barba","no té anelleta"],
               'Alicia': ["dona", "pel llarg", "pel negre", "ulls negres", "porta ulleres", "nas gran","porta anelleta"],
               'Abril': ["dona", "pel llarg", "pel negre", "ulls blaus", "nas petit","no té barba","no té anelleta"],
               'Albert': ["home", "pel llarg", "pel roig", "ulls blaus", "porta ulleres", "nas gran", "té barba","no té anelleta"],
               'Toni': ["dona", "pel curt", "pel negre", "ulls negres", "porta ulleres", "nas petit","no té barba","porta anelleta"]}

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

buclePc()
