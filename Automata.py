import re
import numpy as np
def main():
    #Inicio la lectura del archivo txt

    with open("Lector.txt", "r") as f:
        while True:
            D = '^[(0-9)]' #digitos
            L = '^[(a-z)]' #letras
            MY = '^[(>)]'
            MN = '^[(<)]'
            IG = '^[(=)]'
            MAS = '^[(+)]'
            MEN = '^[(-)]'
            POR = '^[(*)]'
            BAR = '^[(/)]'
            EXC = '^[(!)]'
            PCT = '^[(%)]'
            ESP = '^[(' ')]' #espacio
            PUN = '^[(.)]'
            EDO = 0
            #Columnas:D, L, >, <, =, +, -, *,  /,  !, %, #, .
            EDOMat=[                                                       #Estados
                    [ 1, 4, 5, 6, 9, 7, 8, 0, 11, 10, 0, 0, 0],                 #0
                    [1,200,200,200,200,200,200,200,200,200,200,200,200],        #1
                    [3,300,300,300,300,300,300,300,300,300,300,300,300],        #2
                    [3,201,201,201,201,201,201,201,201,201,201,201,201],        #3
                    [4,4,202,202,202,202,202,202,202,202,202,202,202],          #4
                    [204,204,204,204,203,204,204,204,204,204,204,204,204],      #5
                    [207,207,206,207,205,207,207,207,207,207,207,207,207],      #6
                    [209,209,209,209,209,208,209,209,209,209,209,209,209],      #7
                    [211,211,211,211,211,211,210,211,211,211,211,211,211],      #8
                    [213,213,213,213,212,213,213,213,213,213,213,213,213],      #9
                    [215,215,215,215,214,215,215,215,215,215,215,215,215],      #10
                    [217,217,217,217,217,217,217,217,216,217,217,217,217]       #11
                    ]
            if f.mode == "r":
                f.readline()
                for line in f: #Leo linea por linea
                    for char in line: #Leyendo caracter por caratcer

                        if re.match(D, char):
                            caracter = char
                            char = 0
                        elif re.match(L, char):
                            caracter = char
                            char = 1
                        elif re.match(MY, char):
                            caracter = char
                            char = 2
                        elif re.match(MN, char):
                            caracter = char
                            char = 3
                        elif re.match(IG, char):
                            caracter = char
                            char = 4
                        elif re.match(MAS, char):
                            caracter = char
                            char = 5
                        elif re.match(MEN, char):
                            caracter = char
                            char = 6
                        elif re.match(POR, char):
                            caracter = char
                            char = 7
                        elif re.match(BAR, char):
                            caracter = char
                            char = 8
                        elif re.match(EXC, char):
                            caracter = char
                            char = 9
                        elif re.match(PCT, char):
                            caracter = char
                            char = 10
                        elif re.match(ESP, char):
                            caracter = char
                            char = 11
                        elif re.match(PUN, char):
                            caracter = char
                            char = 12
                        elif re.match('', char): #necesario para el ultimo caracter el cual es un nulo por defoult
                            caracter = char
                            char = 0

                        EDO = EDOMat[EDO][char]
                        if EDO > 11:
                            print('Estado final: ' + str(EDO) + ' con caracter "' + caracter + '"')
                            EDO = 0

            break
        f.close()

if __name__ == "__main__":
    main()
