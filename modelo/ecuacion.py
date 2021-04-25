from .coord import Coord
class Ecuacion:
    def __init__(self,x,y,tipo,resultado):
        self.x=x
        self.y=y
        self.tipo=tipo
        self.resultado=resultado
    def coordx(self):
        return self.resultado/self.x if self.x > 0 else self.resultado
    def coordy(self):
        return self.resultado/self.y if self.y > 0 else self.resultado
    def funcdesp(self):
        #la y no se incluye porque se obvia que se despeja y
        #25x+2y = 600 --- ejemplo
        #y= -15x + 5
        if self.y != 0 and self.x !=0:
            return {
                'x':((-1)*self.x)/ (self.y if self.y >0 else 1),
                'resultado':self.resultado/(self.y if self.y >0 else 1),
                'tipo': 'normal'
            }
        elif self.y==0:
            # 25x = 200
            # x = 200/25 Punto en x
            return {
                'x': self.x/self.x,
                'resultado': self.resultado/self.x,
                'tipo': 'puntx'
            }
        elif self.x==0:
            return {
                'y': self.y/self.y,
                'resultado': self.resultado/self.y,
                'tipo': 'punty'
            }
    def puntCortEcua(self, ecua):
        dicPropio = self.funcdesp() # nuestra funcion despejada
        dicEcua = ecua.funcdesp() # la funcion que nos llega 
        
        #   -15x + 5 = -25x + 8
        if dicPropio['tipo'] == 'normal' and dicEcua['tipo'] == 'normal':
            x = dicPropio['x'] + (-1)*(dicEcua['x'])
            result = (dicPropio['resultado']*(-1) ) + dicEcua['resultado']
            x = result/x
            y = dicPropio['x']*x + dicPropio['resultado']
        elif dicPropio['tipo']=='puntx' or dicEcua['tipo']=='puntx':
            # dicecua = y= 12x + 12
            if dicPropio['tipo'] == 'puntx':
                x = dicPropio['resultado']
                y = dicEcua['x']*x + dicEcua['resultado']
            else:
                x = dicEcua['resultado']
                y = dicPropio['x']*x + dicPropio['resultado']
        elif dicPropio['tipo'] == 'punty' or dicEcua['tipo'] == 'punty':
            # dicecua = x = 12y + 200
            if dicPropio['tipo']=='punty':
                y = dicPropio['resultado']
                x = ((-1)*dicEcua.y*y/ (dicEcua.x if dicEcua.x >0 else 1)) + (dicEcua.resultado/ (dicEcua.x if dicEcua.x >0 else 1))
            else:
                y = dicEcua['resultado']
                x = ((-1)*self.y*y / (self.x if self.x >0 else 1)) + self.resultado/ (self.x if self.x>0 else 1)
        #import pdb; pdb.set_trace()
        return Coord(round(x),round(y))

    def puntCortX(self):
        if self.x == 0:
            return None
        else:
            x=self.resultado/self.x
            return Coord(x,0)
    def puntCortY(self):
        if self.y == 0:
            return None
        else:
            y=self.resultado/self.y
            return Coord(0,y)




