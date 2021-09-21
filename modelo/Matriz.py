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
        renglon = self._matrix[self._renglonPivote] * ((-1) *times)
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
        
        self._renglonPivote = indice + 1

    def column_pivot(self):
        mas_pos = 0
        ind = 1
        for indice, cabecera in enumerate(self._header):
            if('x' in cabecera):
                if(self._matrix[0][indice]>mas_pos):
                    mas_pos=self._matrix[0][indice]
                    ind=indice
        self._columnaPivote = ind
    
    def continua(self):
        cont = False
        for indice, cabecera in enumerate(self._header):
            if('x' in cabecera):
                if(self._matrix[0][indice]>0):
                    cont=True
                    break
        return cont

    def sumarFilas(self):
        for idx, fila in enumerate(self._matrix):
            if(idx != self._renglonPivote):
                self.sumar(idx, self._matrix[idx][self._columnaPivote])

    def setNewColumn(self):
        self.columna_ini[self._renglonPivote] = self._header[self._columnaPivote]

    def eliminarFil(self):
        vec_idx=[]
        for idx, valor in enumerate(self.columna_ini):
            if("R" in valor):               
                vec_idx.append(idx)
        for idx, value in enumerate(vec_idx):
            self.columna_ini.pop(value-idx)
            self._matrix = np.delete(self._matrix,(value-idx),axis=0)

    def eliminarCol(self):
        vec_idx = []
        for idx, valor in enumerate(self._header): 
            if("R" in valor):
                vec_idx.append(idx)
        for idx, value in enumerate(vec_idx):
            self._header.pop(value-idx)
            self._matrix = np.delete(self._matrix,(value-idx),axis=1)

    def ordenar(self):        
        colum_ini_aux = self.columna_ini.copy()
        self.columna_ini = sorted(self.columna_ini)
        #  colum_ini_aux =   [x2, x1] viejo
        #  self.columna_ini = [x1, x2]  nuevo
        #  idx = 0
        #  new_idx = 1
        #  val = x2
        aux = None
        for idx, val in enumerate(colum_ini_aux):
            aux = self._matrix[idx].copy()
            for idx2, val2 in enumerate(self.columna_ini):
                #aux=self._matrix[idx2].copy()
                if(val==val2):
                    self._matrix[idx2]=self._matrix[idx].copy()
            self._matrix[idx]=aux.copy()

                                        
            #new_idx = self.columna_ini.index(val)
            #aux = self._matrix[new_idx].copy()
            #self._matrix[new_idx] = self._matrix[idx].copy()
            #self._matrix[idx] = aux
            #import pdb; pdb.set_trace()

    def imprimir(self):
        print(self._matrix)
        print(self.columna_ini)
        print(self._header)
        