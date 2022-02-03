from abc import abstractmethod
import math
from re import L


class Shape(object):
    # the following methods constitute a shape’s “interface”
    # and should be redefined in all derived classes
    @abstractmethod
    def getName (self):
        pass # could also put return but this “implies” implementation
    @abstractmethod
    def getArea (self):
        pass
    @abstractmethod
    def getVolume (self):
        pass


class Point(Shape):
    def __init__(self,x,y):
        self._x = x 
        self._y = y
    def getName(self):
        return "Point"

    def __str__(self):
        return "["+str(self._x)+","+str(self._y)+"]" #"goString method"
    def getX (self): 
        return self._x
    def getY (self): 
        return self._y
    def setX (self, x): 
        self._x = x
    def setY (self, y): 
        self._y = y
# get/set coordinates methods 
    

class Circle(Point):
    def __init__(self,x,y,r):
        super().__init__(x,y)
        self._r = 0
        self.setRadius(r)
    def getName (self): 
        return "Circle"
    def getArea (self):
        return math.pi*self._r*self._r
    def __str__ (self):
        return "C = " + super().__str__() + "; R = " + str(self._r)
    def getRadius (self): # get/set radius methods return self._r
        return self._r
    def setRadius (self, r): 
        if r > 0:
            self._r = r

class Cylinder(Circle):
    def __init__(self,x,y,r,h):
        super().__init__(x,y,r)
        self._h =0
        self.setHeight(h)

    def getName(self):
        return "Cylinder"
    def __str__(self):
        return super().__str__() + "; H = " + str(self._h)
    def getArea(self):
        return 2.*super().getArea()+2.*math.pi*self.getRadius()*self._h
    def getVolume(self):
        return super().getArea()*self._h

    def getHeigh(self): #ge /set height method
        return self._h
    def setHeight (self, h):
        if h > 0:
            self._h = h

class Sphere(Point):
    def __init__(self, x,y, r):
        super().__init__(x,y)
        self._r = 0
        self.setRadius(r)
    def getName(self):
        return("Sphere")
    def getVolume(self):
        return 1.33 *math.pi * self._r * self._r * self._r
    def __str__ (self):
        return "C = " + super().__str__() + "; R = " + str(self._r)
    def getRadius (self): # get/set radius methods return self._r
        return self._r
    def setRadius (self, r): 
        if r > 0:
            self._r = r

class Rectangle(Point):
    def __init__(self, x,y,a,b):
        super().__init__(x,y)
        self._a = 0
        self._b = 0
        self.setA(a)
        self.setB(b)
    def getName(self):
        return("Rectangle")
    def getArea (self):
        return self._a *self._b
    def __str__ (self):
        return "C = " + super().__str__() + "; a = " + str(self._a)+ "; b = "+str(self._b)
    def getA (self): 
        return self._a
    def getB (self): 
        return self._b
    def setA (self, a): 
        if a>0:
            self._a = a
    def setB (self, b): 
        if b>0:
            self._b = b

class Square(Rectangle):
    def __init__(self,x,y,a):
        super().__init__(x,y,a,a)
        self._l = 0
        self.setLength(a)
    def getName (self): 
        return "Square"
    def getArea (self):
        return self._a * self._a
    def __str__ (self):
        return "C = " + super().__str__() + "; L = " + str(self._a)
    def getLength (self): # get/set radius methods return self._r
        return self._a
    def setLength (self, a): 
        if a > 0:
            self._a = a

class Cube(Square):
    def __init__(self,x,y,a):
        super().__init__(x,y,a)
    def getName (self): 
        return "Cube"
    def getArea(self):
        return super().getArea()
    def getVolume(self):
        return super().getArea()*super().getLength()
    def __str__ (self):
        return super().__str__()

def printAllShape(shapes):
    for s in range(0,len(shapes)): 
        print(str(s+1) +". "+ shapes[s].getName() + " " + str(shapes[s]) + " Area: " + str(shapes[s].getArea()) +  " Volume: " + str(shapes[s].getVolume())) 


def printShapes(shapes):
    if not shapes:
        print("printShapes: There isn't any created shape")
    else:
        print("Print all shapes -- Enter 1\t Print particular shape -- Enter 2")
        getInputCorrectly =False #create a flag to loop until the correct option is entered
        while getInputCorrectly == False:
            I= int(input())
            try:
                if I == 1:
                    printAllShape(shapes)
                    getInputCorrectly =True
                if I ==2:
                    print("Please Enter name of the shape:")
                    shapeName = str(input())
                    count= 0
                    for s in shapes: #compare the entered string and the name of all elements in the list
                        if s.getName() == shapeName:
                            print(s.getName() + " " + str(s) + " Area: " + str(s.getArea()) + 
                            " Volume: " + str(s.getVolume())) 
                            print("\n")
                            count+=1
                    if count ==0:
                        print("printShapes: Can't find the shape")
                    getInputCorrectly =True
            except (TypeError,NameError,ValueError):
                print("printShapes: Please enter options on the menu")
    

        
def getShapeFromKeyboard(shapes):#use this function to get input information from the key board
    print("Please select a shape from the following list:\nPoint -- Enter 1\t2.Circle -- Enter 2\tCylinder -- Enter 3\tSphere -- Enter 4\nRectangle -- Enter 5\tSquare -- Enter 6\tCube -- Enter 7\t")
    getShapeCorrectly =False
    while getShapeCorrectly ==False:
        shapeType = int(input())
        try:
            if shapeType in range(1,8):
                if shapeType == 1: 
                    x = input("Enter x values of the point: ")
                    y = input("Enter y values of y: ")
                    point=Point(x,y)
                    shapes.append(point)
                    

                elif shapeType == 2:
                    x=input("Enter x: ")
                    y=input("Enter y: ")
                    r=int(input("Enter r: "))
                    circle=Circle(x,y,r)
                    shapes.append(circle)
                    #print("Circle "+ str(circle) + " Area "+ circle.getArea())

                elif shapeType == 3:
                    x,y=input("Enter x and y: ").split()
                    r =int(input("Enter r: "))
                    h =int(input("Enter h: "))
                    cylinder = Cylinder(x,y,r,h)
                    shapes.append(cylinder)
                    

                elif shapeType == 4:
                    x,y,= input("Enter x, yof the sphere: ").split()
                    r =int(input("Enter r: "))
                    sphere = Sphere(x,y,r)
                    shapes.append(sphere)
                    

                elif shapeType == 5:
                    x,y= input("Enter x, y: ").split()
                    a = int(input("Enter a: "))
                    b = int(input("Enter b: "))
                    rectangle = Rectangle(x,y,a,b)
                    shapes.append(rectangle)
                    


                elif shapeType == 6:
                    x,y=input("Enter x,y : ").split()
                    a = int(input("Enter a: "))
                    square = Square(x,y,a)
                    shapes.append(square)
                    

                elif shapeType == 7:
                    x,y=input("Enter x,y : ").split()
                    a = int(input("Enter a: "))
                    cube = Cube(x,y,a)
                    shapes.append(cube)
                    
                #end of all cases
                print("Shape added")  
                getShapeCorrectly =True
            else:
                print("Please enter options on the menu, try again")
        
        except(ValueError,NameError):
            print("getShapeFromKeyboard:Please enter the required number of parameters")
        except(TypeError):
            print("getShapeFromKeyboard:Please enter interger")
       
        
def deleteShape(shapes):
    printAllShape(shapes)
    print("Please select a shape to delete: ")
    EnterShapeCorrectly =False
    while EnterShapeCorrectly ==False:
        try:
            i = int(input())#The list of shapes start from 1 but element index starts from 
            if i >=1 & i<=len(shapes)+1:
                shapes.remove(shapes[i-1])
                print("deleteShape: Shape removed")
                EnterShapeCorrectly =True
            else:
                print("deleteShapes: shape dosen't exsit, try again")
        except(TypeError,ValueError):
            print("deleteShape: Please select shape from the list, try again")




def main():
    shapes = []#create an empyt list of shapes
    point = Point(10, 20)
    circle = Circle(30, 40, 5)
    cylinder = Cylinder(50, 60, 10, 20)
    square=Square(1,1,1)
    cube = Cube(1,1,1)
    shapes.append(point)
    shapes.append(circle)
    shapes.append(cylinder)
    shapes.append(square)
    shapes.append(cube)
    
    
    getOptionCorrectly =False #create a flag to loop until the correct option is entered
    while getOptionCorrectly ==False:
        print("Menu:\nPrint shapes -- Enter 1\t  Create new shape -- Enter 2\t  Edit shapes -- Enter 3\t Exit -- Enter 4")
        try:
            option = int(input())

            if option ==1:
                printShapes(shapes)
                
               
            elif option ==2:
                getShapeFromKeyboard(shapes)
                
            elif option ==3:
                
                deleteShape(shapes)

            elif option ==4:
                getOptionCorrectly =True

            else:
                print("Please enter options on the menu")
            
        except (TypeError,NameError,ValueError):
            print("Please enter options on the menu")
    

if __name__ =="__main__":
        main()


        


