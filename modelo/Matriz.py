import numpy as np

class Matriz:
    def __init__(self, columna_ini, header, matrix):
        self._header = header
        self._matrix = np.array(matrix)
        self.columna_ini = columna_ini
        self._renglonPivote = None
        self._columnaPivote = None

    def sumaR0(self):
        filas=[]
        for idx, file in enumerate(self.columna_ini):
            if('R' in file):
                filas.append(self._matrix[idx].copy())
        self._matrix[0]=np.apply_along_axis(sum,0,filas)

    def sumar(self, fila, times = 1):
        #renglon = self._matrix[self._renglonPivote] * ((-1) *times)
        #self._matrix[fila] = np.add(self._matrix[fila], renglon)
        #print("###################################")
        #print(self._matrix[fila])
        #print(self._matrix[self._renglonPivote])
        for idx, value in enumerate(self._matrix[fila]):
            self._matrix[fila][idx] = round(value,10) + round((self._matrix[self._renglonPivote][idx] * ((-1) *times)),10)

    def inverso(self):
        celdaPivote = self._matrix[self._renglonPivote][self._columnaPivote]  
        a = self._matrix[self._renglonPivote] * float(1/celdaPivote)
        self._matrix[self._renglonPivote, :] = a    

    def filaPivote(self,fase2=False):
        if(fase2):
            columnaPivote = self._matrix[0:, self._columnaPivote]
            y = self._matrix[0:,-1]
        else:
            columnaPivote = self._matrix[1:, self._columnaPivote]
            y = self._matrix[1:,-1]
        print(columnaPivote)
        print(y)
        res = np.divide(y, columnaPivote, out=np.zeros_like(y), where=columnaPivote!=0)
        print("Se imprime res")
        print(res)
        valorMax = np.where(res==np.max(res))[0]
        indice = int(valorMax[0] if np.size(valorMax) > 1 else valorMax)

        for i, e in enumerate(res):
            if (e < res[indice] and e > 0):
                indice = i
        if(fase2):
            self._renglonPivote = indice
        else:
            self._renglonPivote = indice + 1

    # Selecciona el mas positivo del R0 para escoger la columna pivote
    def column_pivot(self):
        mas_pos = 0
        ind = 1
        for indice, cabecera in enumerate(self._header):
            if('x' in cabecera or 'H' in cabecera or 'S' in cabecera):
                if(self._matrix[0][indice]>mas_pos):
                    mas_pos=self._matrix[0][indice]
                    ind=indice
        self._columnaPivote = ind
    
    def continua(self):
        cont = False
        for indice, cabecera in enumerate(self._header):
            if('x' in cabecera or 'H' in cabecera or 'S' in cabecera):
                if(self._matrix[0][indice]>0):
                    cont=True
                    break
        return cont

    def continuaFaseDosMax(self):
        # inicio = len(self.columna_ini)
        # control = False
        # for idx in range(inicio,len(self._matrix[0])):
        #     if(self._header[idx]!='Y' and self._matrix[0][idx] < 0):
        #         control= True
        #         break
        control = False
        for idx in range(0,len(self._matrix[0])):
           if(self._header[idx] not in self.columna_ini and self._header[idx]!='Y' and self._matrix[0][idx] < 0):
               control= True
               break
        return control
    
    def continuaFaseDosMin(self):
        control = False
        # inicio = len(self.columna_ini)
        # for idx in range(inicio,len(self._matrix[0])):
        #    if(self._header[idx]!='Y' and self._matrix[0][idx] > 0):
        #        control= True
        #        break
        for idx in range(0,len(self._matrix[0])):
            if(self._header[idx] not in self.columna_ini and self._header[idx]!='Y' and self._matrix[0][idx] > 0):
                control= True
                break
        return control

    def columnaPivoteFaseDosMax(self):
        masNeg = 0
        idx_global = None
        for idx in range(0,len(self._matrix[0])):
            if(self._header[idx] not in self.columna_ini and self._header[idx]!='Y' and self._matrix[0][idx] < masNeg):
                masNeg = self._matrix[0][idx]
                idx_global = idx
        self._columnaPivote=idx_global

    def columnaPivoteFaseDosMin(self):
        masPos = 0
        idx_global = None
        for idx in range(0,len(self._matrix[0])):
            if(self._header[idx] not in self.columna_ini and self._header[idx]!='Y' and self._matrix[0][idx] > masPos):
                masPos = self._matrix[0][idx]
                idx_global = idx
        self._columnaPivote=idx_global
        
    def sumarFilas(self):
        for idx, fila in enumerate(self._matrix):
            if(idx != self._renglonPivote):
                self.sumar(idx, self._matrix[idx][self._columnaPivote])

    def setNewColumn(self):
        print(self._columnaPivote)
        print(self._renglonPivote)
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
        mat_aux = self._matrix.copy()
        for idx, val in enumerate(colum_ini_aux):                 
            new_idx = self.columna_ini.index(val)
            mat_aux[new_idx] = self._matrix[idx].copy()
        self._matrix= mat_aux.copy()

    def agreCabe(self):
        self._header=['Z']+self._header
    
    def agregarZ(self, zfile):
        iter = len(self._header) - len(zfile)
        for i in range(0,iter):
            zfile.append(float(0))
        zfile=np.array(zfile)
        self._matrix = np.insert(self._matrix, [0] ,zfile,axis = 0)
        self.columna_ini = ['Z'] + self.columna_ini
    
    def agregColumnZ(self):
        zeros_vec = np.zeros(1)
        self._matrix = np.insert(self._matrix, [0] ,zeros_vec,axis = 1)

    def restarEnZ(self):
        for idx, celda in enumerate(self._matrix[0]):
            if(self._header[idx] !="Z" and self._header[idx] in self.columna_ini and celda !=0):
                print(self._header[idx])
                indiceDeFila = self.columna_ini.index(self._header[idx])
                self._renglonPivote=indiceDeFila
                self.sumar(0,celda)
        # for idx in range(1,len(self._matrix)):
        #     self._renglonPivote=idx
        #     for idx2 in range(1, len(self._matrix[idx])):
        #         if(self._matrix[idx][idx2]==1):
        #             self._columnaPivote=idx2
        #             break
        #     self.sumar(0,self._matrix[0][self._columnaPivote])

    def imprimir(self):
        print(self._matrix)
        print(self.columna_ini)
        print(self._header)
        