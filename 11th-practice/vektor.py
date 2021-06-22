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