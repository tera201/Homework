import math
class ConvexFigure:
    def getArea(self):
        pass
    def getPerimeter(self):
        pass
class Circle(ConvexFigure):
    def __init__(self,r):
        self.r=r
    def P(self):
        return 2*math.pi*self.r
    def S(self):
        return math.pi*(self.r**2)
class Rectangle(ConvexFigure):
    def __init__(self,l,w):
        self.l=l
        self.w=w
    def S(self):
        return self.l*self.w

a=Circle(float(input("задайте радиус ")))
print("Circle P=", a.P())
print("Circle S=",a.S())
print("Rectangle S=",Rectangle(float(input("задайте длину ")),float(input("задайте ширину "))).S())