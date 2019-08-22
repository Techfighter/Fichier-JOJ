"""
NE PAS OUBLIER DE MODIFIER LA SOURCE DU FICHIER.
Ce code Ouvre (prog.txt) et commence a la lecture ligne par ligne.
Si les caractère spéciaux apparaisse au debut ou a la fin d'une chaine,
elles n'apparaiteront pas et fera un simple display.
Exemple: A=Hello world!}
Sur "A=" en début de ligne Donne
"Hello world!" dans la variable A & Ordonne une sortie du compilateur sur "}"
Exemple2: [A) Oui, B) Non]
Sur "[" en début de ligne Donne
"[A) Oui, B) Non]" en display & Ouvre un input key ">?"
Si A et B n'est pas definis, tout entré input retournera une message d'erreur:
"Ce n'est pas une réponse valide!"
Celles-ci se doivent d'être correctement édité les lignes (précédante)
En entrant une lettre dans le input un message correspondant A, B s'affiche.
Ca fonction jusqu'a F
"""
import os.path
import glob
#import sys

#try:
#color = sys.stdout.shell
#except AttributeError: raise RuntimeError("Use IDLE")

Compile = 1
Choix = 1
key = ""
A = ""
B = ""
C = ""
D = ""
E = ""
F = ""
source = 'E:/PERSONNEL/python_2/python/histoires/joj/'
affiche = 1
Log = ""
action = 0

def verrification():
    global Compile, action
    Compile = 0
    action = 0
    #exit()
    
repertoir = []
direct = []
repertoir = os.listdir(source)
rep = 0
txt = 0
print("Dans le Répertoire:", source)
#mes = "Dans le Répertoire:"+source+"\n"
#color.write(mes,"KEYWORD")
for x in repertoir:
    rep = rep + 1
    if (repertoir[rep - 1][-3:].upper() == "TXT" and repertoir[rep - 1][-7:-4].upper() == "JOJ"):
        #color.write(repertoir[rep - 1][:-8].upper()+"\n","STRING")
        print(repertoir[rep - 1][:-8].upper())
        txt = txt + 1
#mes = str(txt)+" élément trouvé.\n"
#color.write(mes,"COMMENT")
print(txt, " élément trouvé.")
sourcefile = input("Ouvrir >")
if (sourcefile == ""):
    sourcefile = "menu"
if (sourcefile == ".."):
    direct = source.split("/")
    del direct[-1]
    direct = "/".join(direct)
    source = direct
if (sourcefile == "cd"):
    direct = source.split("/")
    direct.append(key)
    direct = "/".join(direct)
    source = direct
    
while Compile == 1:
    if (sourcefile[-8:].upper != ".JOJ.TXT"):
        file = open(sourcefile + ".joj.txt".upper(), "r")
    else:
        file = open(sourcefile.upper(), "r")
    for line in file:
        affiche = 1
        attend = 0
        #for x in range(0, len(line)):
#Je crois que FOR n'est pas nécésaire ici, Il est tres facile de cadré avec []
        if (line[0:2].upper() == "A="):
            #A = ""
            affiche = 0
            #for y in range(2, len(line)):
                #A = A + line[y]
            A = line[2:]
        if (line[0:2].upper() == "B="):
            B = ""
            affiche = 0
            B = line[2:]
        if (line[0:2].upper() == "C="):
            C = ""
            affiche = 0
            C = line[2:]
        if (line[0:2].upper() == "D="):
            D = ""
            affiche = 0
            D = line[2:]
        if (line[0:2].upper() == "E="):
            D = ""
            affiche = 0
            E = line[2:]
        if (line[0:2].upper() == "F="):
            D = ""
            affiche = 0
            F = F + line[y]
        if (line[0] == "["):
            Choix = 1
            while Choix == 1:
                print(line)
                affiche = 0
                key = input("? >")
                Log = Log + key + ","
                if (key.upper() == "A"):
                    if ((A[len(A)-2:len(A)-1]) == "}"):
                        print(A[:len(A)-2])
                        verrification()
                    else:
                        print(A)
                    Choix = 0
                elif (key.upper() == "B"):
                    if ((B[len(B)-2:len(B)-1]) == "}"):
                        print(B[:len(B)-2])
                        verrification()
                    else:
                        print(B)
                    Choix = 0
                elif (key.upper() == "C"):
                    if ((C[len(C)-2:len(C)-1]) == "}"):
                        print(C[:len(C)-2])
                        verrification()
                    else:
                        print(C)
                    Choix = 0
                elif (key.upper() == "D"):
                    if ((D[len(D)-2:len(D)-1]) == "}"):
                        print(D[:len(D)-2])
                        verrification()
                    else:
                        print(D)
                    Choix = 0
                elif (key.upper() == "E"):
                    if ((E[len(E)-2:len(E)-1]) == "}"):
                        print(E[:len(E)-2])
                        verrification()
                    else:
                        print(E)
                    Choix = 0
                elif (key.upper() == "F"):
                    if ((F[len(F)-2:len(F)-1]) == "}"):
                        print(F[:len(F)-2])
                        verrification()
                    else:
                        print(F)
                    Choix = 0
                else:
                    print("Ce n'est pas un choix valide")
        if (affiche == 1):
            print(line)
            if (attend == 1):
                key = input("Enter pour continué")
        action = action + 1
    Compile = 0
    action = 0
    print(Log)
