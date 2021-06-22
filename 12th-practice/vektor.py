import math

class Vektor:
    def __init__(self, x=0, y=0):
        self.x = x
        self.y = y
    
    def length(self):
        return math.sqrt(pow((self.x), 2) + pow((self.y), 2))
    
    def angle(self):
        return ((self.y) / (self.x))
    
    def sum(self, vektor):
        return (self.x + vektor.x, self.y + vektor.y)
    
    def diff(self, vektor):
        return (self.x - vektor.x, self.y - vektor.y)

    def scalar(self, vektor):
        return (self.x * vektor.x + self.y * vektor.y)

class VektorInSpace(Vektor):
    def __init__ (self, x=0, y=0, z=0):
        super().__init__(x,y)
        self.z = z

    def length(self):
        return math.sqrt(pow((self.x), 2) + pow((self.y), 2) + pow((self.z), 2))
    
    def angle(self):
        return ((self.y) / (self.x) / (self.z))
    
    def sum(self, vektor):
        return (self.x + vektor.x, self.y + vektor.y, self.z + vektor.z)
    
    def diff(self, vektor):
        return (self.x - vektor.x, self.y - vektor.y, self.z - vektor.z)

    def scalar(self, vektor):
        return (self.x * vektor.x + self.y * vektor.y + self.z + vektor.z)   

    def xOy(self):
        return ((self.y) / (self.x))

    def xOz(self):
        return ((self.z) / (self.x))

    def yOz(self):
        return((self.y) / (self.z))