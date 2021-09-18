import numpy as np

class Matriz:
    def __init__(self, columna_ini, header, matrix):
        self._header = header
        self._matrix = np.array(matrix)
        self.columna_ini = columna_ini
        self._renglonPivote = None
        self._columnaPivote = None

    def sumaR0(self):
        self._matrix[0]=np.apply_along_axis(sum,0,self._matrix)

    def sumar(self, fila, times = 1):
        renglon = self._matrix[self._renglonPivote] * times
        self._matrix[fila] = np.add(self._matrix[fila], renglon)

    def inverso(self):
        matriz = self._matrix
        print(type(self._renglonPivote))
        Pivote = matriz[self._renglonPivote]

        print(Pivote)  
        #a = self._matrix[self._renglonPivote] * float(1/1)
        #self._matrix[self._renglonPivote, :] = a    

    def filaPivote(self):
        columnaPivote = self._matrix[1:, self._columnaPivote]
        y = self._matrix[1:,-1]
        res = np.divide(y, columnaPivote)
        indice = 0

        for i, e in enumerate(res):
            if (e < res[indice] and e > 0):
                indice = i
        
        self._filaPivote = indice + 1
        print(self._filaPivote)

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
    
    def continua(self):
        cont = False
        for indice, cabecera in enumerate(self._header):
            if('x' in cabecera):
                if(self._matrix[0][indice]>0):
                    cont=True
                    break
        return cont

    def imprimir(self):
        print(self._matrix)
        