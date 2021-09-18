import numpy as np

class Matriz:
    def __init__(self, header, matrix, renglonPivote, columnaPivote):
        self._header = header
        self._matrix = np.array(matrix)
        self._renglonPivote = renglonPivote
        self._columnaPivote =  columnaPivote

    def sumar(self, fila, times = 1):
        renglon = self._matrix[self._renglonPivote] * times
        self._matrix[fila] = np.add(self._matrix[fila], renglon)

    def inverso(self):
        celdaPivote = self._matrix[self._renglonPivote][self._columnaPivote]  
        a = self._matrix[self._renglonPivote] * float(1/celdaPivote)
        self._matrix[self._renglonPivote, :] = a    

    def filaPivote(self):
        columnaPivote = self._matrix[1:, self._columnaPivote]
        y = self._matrix[1:,-1]
        res = np.divide(y, columnaPivote)
        indice = 0

        for i, e in enumerate(res):
            if (e < res[indice] and e > 0):
                indice = i
        
        self.filaPivote = indice + 1
        print(indice+1)

    def column_pivot(self):
        mas_pos = 0
        ind = 1
        for indice, cabecera in enumerate(self._header):
            if('x' in cabecera):
                if(self._matrix[0][indice]>mas_pos):
                    mas_pos=self._matrix[0][indice]
                    ind=indice
        self._columnaPivote = ind
        print(ind)

    def imprimir(self):
        print(self._matrix)
        