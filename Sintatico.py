from CompiladorMax import *
# from Matriz import *

def sintatico(tokens):
    # 1 es corrimiento
    # 2 es retorno
    # 3 es aceptar
    x = -len(tokens)
    TOP = tokens.pop(x)
    EDO2 = 0
    token = TOP[1]
    MatrizAcciones = [
            [0, 501, 1, 2],
            [1, 4, 3, 0], #ACEPTAS LA CADENA DE TEXTO E IMPRIMES UN ACEPTADO
            [2, 516, 1, 7],
            [3, 516, 1, 4],
            [4, 507, 1, 23], [4, 508, 1, 58], [4, 509, 1, 78], [4, 510, 1, 85], [4, 511, 1, 96], [4, 2000, 1, 93], [4, 517, 2, 13]
            ]
    i=0
    while True:
        if MatrizAcciones[i][0] == EDO2:
            if (str(MatrizAcciones[i][1]) == str(token)):
                EDO2 =(MatrizAcciones[i][3])
                print("Haces un corrimeinto a " + str(EDO2))
                break
        i+= 1
        if(i == len(MatrizAcciones)):
            break

if __name__ == '__main__':
    Lexico = main()
    sintatico(Lexico)
