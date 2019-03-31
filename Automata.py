import re
import numpy as np
def main():
    #Inicio la lectura del archivo txt
    Cadena = ''
    with open("Lector.txt", "r") as f:
        while True:
            D = '^[(0-9)]' #digitos
            L = '^[(a-z)]' #letras
            MY = '^[(>)]'
            MN = '^[(<)]'
            MAS = '^[(+)]'
            MEN = '-'
            IG = '^[(=)]'
            BAR = '^[(/)]'
            EXC = '^[(!)]'
            PCT = '^[(%)]'
            ESP = '^[('')]' #espacio
            EDO = 0
            #N°Colum  0  1  2  3  4  5  6  7  8   9  10  11
            #Columnas:D, L, >, <, =, +, -, /, !,  %,  #,  .
            EDOMat=[                                                       #Estados
                    [1, 4, 5, 6, 9, 7, 8, 11, 10, 300, 300, 300],           #0
                    [1,200,200,200,200,200,200,200,200,200,200,2],          #1
                    [3,300,300,300,300,300,300,300,300,300,300,300],        #2
                    [3,201,201,201,201,201,201,201,201,201,201,201],        #3
                    [4,4,202,202,202,202,202,202,202,202,202,202],          #4
                    [204,204,204,204,203,204,204,204,204,204,204,204],      #5
                    [207,207,206,207,205,207,207,207,207,207,207,207],      #6
                    [209,209,209,209,209,208,209,209,209,209,209,209],      #7
                    [211,211,211,211,211,211,210,211,211,211,211,211],      #8
                    [213,213,213,213,212,213,213,213,213,213,213,213],      #9
                    [215,215,215,215,214,215,215,215,215,215,215,215],      #10
                    [217,217,217,217,217,217,217,216,217,217,217,217]       #11
                    ]
            if f.mode == "r":
                f.readline()
                for line in f: #Leo linea por linea
                    for char in line: #Leyendo caracter por caratcer
                        Characterantes = str(char)
                        if char == '.':
                            char = 11
                        elif re.match(D, char):
                            char = 0
                        elif re.match(L, char):
                            char = 1
                        elif re.match(MY, char):
                            char = 2
                        elif re.match(MN, char):
                            char = 3
                        elif re.match(IG, char):
                            char = 4
                        elif re.match(MAS, char):
                            char = 5
                        elif re.match(MEN, char):
                            char = 6
                        elif re.match(BAR, char):
                            char = 7
                        elif re.match(EXC, char):
                            char = 8
                        elif re.match(PCT, char):
                            char = 9
                        elif re.match(ESP, char):
                            char = 10
                        elif re.match('', char): #necesario para el ultimo caracter el cual es un nulo por defoult
                            char = 10

                        EDO = EDOMat[EDO][char]
                        #print(EDO)
                        #print(char)
                        if EDO > 11:
                            if EDO < 300:
                                print('Estado final: ' + str(EDO) + ' con la cadena: "' + Cadena + '"')
                                EDO = 0
                                Cadena = ''
                                Cadena = Characterantes
                                Characterantes = ''
                            else:
                                #print('error' + str(EDO))
                                EDO = 0
                                Cadena = ''
                        else:
                            Cadena = Cadena + Characterantes

            break
        f.close()

if __name__ == "__main__":
    main()
