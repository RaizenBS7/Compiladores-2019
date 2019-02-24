# Los estados del 0 al 11 serán funciones, y dependiendo de la funcion en la que nos encontremos en ese
# momento revisaremos la matriz y le asignaremos el estado que tiene.
# ord() function para sacar el código ascii de un caracter


"""
Salida esperada
[[XYZ -> es un string],
[. -> es un punto],
[8045 -> es un entero],
[400.55 -> es un decimal],
[hola -> es un string]] """

import re
stringFinal = []

matriz = [# Estados iniciales
          [0,1,4,5,6,9,7,8,404,11,10,404,404,404],
          [1,1,200,200,200,200,200,200,200,200,200,200,200,200], # Estados para los números
          [2,3,300,300,300,300,300,300,300,300,300,300,300,300], # Estados para letras
          [3,3,201,201,201,201,201,201,201,201,201,201,201,201], # >
          [4,4,4,202,202,202,202,202,202,202,202,202,202,202], # <
          [5,204,204,204,204,203,204,204,204,204,204,204,204,204], # =
          [6,207,207,206,207,205,207,207,207,207,207,207,207,207], # +
          [7,209,209,209,209,209,208,209,209,209,209,209,209,209], # -
          [8,211,211,211,211,211,211,210,211,211,211,211,211,211], # *
          [9,213,213,213,213,212,213,213,213,213,213,213,213,213], # /
          [10,215,215,215,215,214,215,215,215,215,215,215,215,215], # !
          [11,217,217,217,217,217,217,217,217,216,217,217,217,217] # %
        ] # Los "404" son los vacíos

class cambiaestados(object):
    def estadosiniciales(self, argument):

            method_name = 'estado_' + str(argument)
            method = getattr(self, method_name, lambda: "Estado no existente")
            return method()

    def estado_0(self):
        return "Estas en el estado 0"

    def estado_1(self):
        return "Estas en el estado 1"

    def estado_2(self):
        return "Estas en el estado 2"

    def estado_3(self):
        return "Estas en el estado 3"

    def estado_4(self):
        return "Estas en el estado 4"

    def estado_5(self):
        return "Estas en el estado 5"

    def estado_6(self):
        return "Estas en el estado 6"

    def estado_7(self):
        return "Estas en el estado 7"

    def estado_8(self):
        return "Estas en el estado 8"

    def estado_9(self):
        return "Estas en el estado 9"

    def estado_10(self):
        return "Estas en el estado 10"

    def estado_11(self):
        return "Estas en el estado 11"

def main():


    with open("Lector.txt","r") as f:
        while True:
            if f.mode == "r":
                f.readline()
                EDO = 0
                caracter = 0
                caracter = caracter + 1
                cadena = 0
                cadena = cadena + caracter
                EDO = matriz[EDO][1]
                print(EDO)
                for line in f: # aquí leemos la linea completa
                    for chartr in line: # e iteramos la linea caracter por caracter
                        """ aquí leemos cada caracter de la linea
                        y se empezará el procesamiento de los estados caracter por caracter """
                        ascii = ord(chartr)
                        if ascii >= 48 and ascii <= 57:
                            print("El caracter "+ chartr +" es: dígito")
                        elif ascii >= 65 and ascii <= 90 or ascii >= 97 and ascii <= 122:
                            print("El caracter "+ chartr +" es: letra")
                        elif ascii == 62:
                            print("El caracter "+ chartr +" es: '>'")
                        elif ascii == 60:
                            print("El caracter "+ chartr +" es: '<'")
                        elif ascii == 61:
                            print("El caracter "+ chartr +" es: '='")
                        elif ascii == 43:
                            print("El caracter "+ chartr +" es: '+'")
                        elif ascii == 45:
                            print("El caracter "+ chartr +" es: '-'")
                        elif ascii == 42:
                            print("El caracter "+ chartr +" es: '*'")
                        elif ascii == 47:
                            print("El caracter "+ chartr +" es: '/'")
                        elif ascii == 33:
                            print("El caracter "+ chartr +" es: '!'")
                        elif ascii == 37:
                            print("El caracter "+ chartr +" es: '%'")
                        elif ascii == 35:
                            print("El caracter "+ chartr +" es: '#'")
                        elif ascii == 46:
                            print("El caracter "+ chartr +" es: '.'")
                        elif ascii == 32:
                            print("El caracter '"+ chartr +"' es: 'espacio'")


            break # interrumpe el programa cuando termina de leer las lineas
    f.close() # Cerrar el archivo a leer

if __name__ == "__main__":
    x=cambiaestados()
    x.estadosiniciales(0)
    main()
