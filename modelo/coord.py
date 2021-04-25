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
        