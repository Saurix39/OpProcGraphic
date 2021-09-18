from modelo.Fila import Fila
from modelo.Matriz import Matriz
import numpy as np

def main():
    a = [1, 5, 12, 1, 0, -1, -1, 0]
    b = [0, 1, 10, 1, 0, 1, 0, 7]
    c = [0, 2, 5, 1, -1, 0, 1, 10]

    ma = [a,b,c]
    head = ['R0', 'x1', 'x2', 'x3', 'S1', 'R1', 'R2', 'Y']

    mA = Matriz(1,head, ma)
    #mA.imprimir()
    #mA.sumar(1, 2)
    mA.column_pivot()
    mA.filaPivote()



    #objA = Fila("prueba", a)

    #res = objA.sumar(b, 2)
    #res = objA.inverso(3)

    #print(objA.a)
    #print(res)


if __name__ == "__main__":
    main()