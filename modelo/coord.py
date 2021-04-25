class Coord:
    def __init__(self,x,y):
        self.x=x
        self.y=y
    def ecuaCordCord(self, coord):
        pass
    def __eq__(self,coord):
        return coord.x == self.x and coord.y == self.y
    def __str__(self):
        return f"({self.x}, {self.y})"
    def coord_restric(self, restric):
        for res in restric:
            resizc = self.x*res.x + self.y*res.y
            if self.x < 0 or self.y < 0:
                return False
            if res.tipo == '<=':
                if resizc > res.resultado:
                    return False
            elif res.tipo == '>=':
                if resizc < res.resultado:
                    return False
            elif res.tipo == '=':
                if resizc != res.resultado:
                    return False
        return True