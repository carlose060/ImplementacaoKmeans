class Ponto:
    def __init__(self,x,y,z,w):
        self.x = x
        self.y = y
        self.z = z
        self.w = w
    
    def __eq__(self, other):
        if self.x == other.x and self.y == other.y and self.z == other.z and self.w == other.w:
            return True
        return False
        
    def __repr__(self):
        return f'({self.x},{self.y},{self.z},{self.w})'

    @staticmethod
    def distancia(cls, other):
        
    # distancia = sqrt( (xa - xb)^2 + (ya - yb)^2 ) 
        x = pow( (cls.x - other.x) , 2)
        y = pow( (cls.y - other.y) , 2)
        z = pow( (cls.z - other.z) , 2)
        w = pow( (cls.w - other.w) , 2)
        return pow( (x + y + z + w) , 1/2)