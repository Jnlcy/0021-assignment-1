from abc import abstractmethod
import math
from re import L


class Shape(object):
    # the following methods constitute a shape’s “interface”
    # and should be redefined in all derived classes
    @abstractmethod
    def getName (self):
        pass #This method will return the name of the shape
    @abstractmethod
    def getArea (self):
        pass#This method will return the area of the shape
    @abstractmethod
    def getVolume (self):
        pass#This mathod will return the volume of the shape


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

class Square(Rectangle):#code is reusable as the square is a special case of the square
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
    def getLength (self): # get/set radius methods return self._a
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

#This function prints all the shapes in the list when called
def printAllShape(shapes):
    for s in range(0,len(shapes)): #print all shapes using index
        print(str(s+1) +". "+ shapes[s].getName() + " " + str(shapes[s]) + " Area: " + str(shapes[s].getArea()) +  " Volume: " + str(shapes[s].getVolume())) 

#This function allows the user to print all shapes or single shape
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
    
#This function take user input and create new shape        
def getShapeFromKeyboard(shapes):#use this function to get input information from the key board  
    getShapeCorrectly =False #create a flag to loop until the shape is correct
    while getShapeCorrectly ==False:
        print("Please select a shape from the following list:\nPoint -- Enter 1\t2.Circle -- Enter 2\tCylinder -- Enter 3\tSphere -- Enter 4\nRectangle -- Enter 5\tSquare -- Enter 6\tCube -- Enter 7\t")
        shapeType = int(input())
        try:
            if shapeType in range(1,8):
                try:
                    if shapeType == 1: #create point
                        x = float(input("Enter x values of the point: "))
                        y = float(input("Enter y values of y: "))
                        point=Point(x,y)
                        shapes.append(point)
                    

                    elif shapeType == 2:#create circle
                        x=float(input("Enter x: "))
                        y=float(input("Enter y: "))
                        r=float(input("Enter r: "))
                        circle=Circle(x,y,r)
                        shapes.append(circle)
                   

                    elif shapeType == 3:#create cylinder
                        x = float(input("Enter x value: "))
                        y = float(input("Enter y value: "))
                        r =float(input("Enter r: "))
                        h =float(input("Enter h: "))
                        cylinder = Cylinder(x,y,r,h)
                        shapes.append(cylinder)
                    

                    elif shapeType == 4:#create sphere
                        x = float(input("Enter x value: "))
                        y = float(input("Enter y value: "))
                        r =float(input("Enter r: "))
                        sphere = Sphere(x,y,r)
                        shapes.append(sphere)
                    

                    elif shapeType == 5:#create rectangle
                        x = float(input("Enter x value: "))
                        y = float(input("Enter y value: "))
                        a = float(input("Enter a: "))
                        b = float(input("Enter b: "))
                        rectangle = Rectangle(x,y,a,b)
                        shapes.append(rectangle)                 


                    elif shapeType == 6:#create square
                        x = float(input("Enter x value: "))
                        y = float(input("Enter y value: "))
                        a = float(input("Enter a: "))
                        square = Square(x,y,a)
                        shapes.append(square)
                    

                    elif shapeType == 7:#create cube
                        x = float(input("Enter x value: "))
                        y = float(input("Enter y value: "))
                        a = float(input("Enter a: "))
                        cube = Cube(x,y,a)
                        shapes.append(cube)
                    
                    #end of all cases
                    print("Shape added")  
                    getShapeCorrectly =True
                except(ValueError,NameError,TypeError):
                    print("getShapeFromKeyboard:Please enter numbers for the parameter, try again.")

            else:
                print("getShapeFromKeyboard:Please enter options on the menu, try again")
            #end of if
    #End of while loop
        except(ValueError,NameError,TypeError):
            print("getShapeFromKeyboard:Please enter numbers for the options, try again")
       
#This fucntion deletes selected shape        
def deleteShape(shapes):
    if not shapes:
        print("modifyShape: There isn't any created shape")
    else:
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
        #End of while loop
    
#This function allows the user to modify existed shape
def modifyShape(shapes):
    if not shapes:
        print("modifyShape: There isn't any created shape")
    else:
        
        EnterShapeCorrectly =False
        while EnterShapeCorrectly ==False:
            printAllShape(shapes)
            print("Please select a shape to modify: ")
            try:
                i = int(input())-1#The list of shapes start from 1 but element index starts from 
                if i >=0 & i<=len(shapes):
                    name = shapes[i].getName()
                    try:
                        if name== "Point":
                            x = float(input("Enter x value: "))
                            y = float(input("Enter y value: "))
                            shapes[i] =Point(x,y)           
                        

                        elif name == "Circle":
                            x=float(input("Enter x: "))
                            y=float(input("Enter y: "))
                            r=float(input("Enter r: "))
                            shapes[i] = Circle(x,y,r)
                        

                        elif name == "Cylinder":
                            x = float(input("Enter x value : "))
                            y = float(input("Enter y value : "))
                            r =float(input("Enter r: "))
                            h =float(input("Enter h: "))
                            shapes[i] = Cylinder(x,y,r,h)

                        elif name == "Sphere":
                            x = float(input("Enter x value : "))
                            y = float(input("Enter y value : "))
                            r =float(input("Enter r: "))
                            shapes[i] = Sphere(x,y,r)

                        elif name == "Rectangle":
                            x = float(input("Enter x value : "))
                            y = float(input("Enter y value : "))
                            a = float(input("Enter a: "))
                            b = float(input("Enter b: "))
                            shapes[i] = Rectangle(x,y,a,b)
                    
                        elif name == "Square":
                            x = float(input("Enter x value : "))
                            y = float(input("Enter y value : "))
                            a = float(input("Enter a: "))
                            shapes[i] = Square(x,y,a)

                        elif name == "Cube":
                            x = float(input("Enter x value: "))
                            y = float(input("Enter y value: "))
                            a = float(input("Enter a: "))
                            shapes[i] = Cube(x,y,a)

                        print("modifyShape: Shape modified")
                        EnterShapeCorrectly =True
                    except(ValueError,NameError,TypeError):
                        print("getShapeFromKeyboard:Please enter numbers for the parameter, try again.")
                    
                else:
                    print("modifyShape: shape dosen't exsit, try again")
            except(TypeError,ValueError,IndexError):
                print("modifyShape: Please select shape from the list and enter interger value,try again.")
            #end of while loop


def main():
    shapes = []#create an empyt list of shapes
    
    
    """
    Hard coded shapes used to test the code--PLEASE IGNORE

    point = Point(10, 20)
    circle = Circle(30, 40, 5)
    cylinder = Cylinder(50, 60, 10, 20) 
    shapes.append(point)
    shapes.append(circle)
    shapes.append(cylinder)
    """
    getOptionCorrectly =False #create a flag to loop until the correct option is entered
    while getOptionCorrectly ==False:
        print("Menu:\nPrint shapes -- Enter 1\t  Create new shape -- Enter 2\t  Delete shape -- Enter 3\tModify shape -- Enter 4\t Exit -- Enter 5")
        
        try:
            option = int(input())#ask input from user
            if option ==1:
                printShapes(shapes)
                             
            elif option ==2:
                getShapeFromKeyboard(shapes)
                
            elif option ==3:
                
                deleteShape(shapes)

            elif option ==4:
                modifyShape(shapes)

            elif option ==5:#The program keeps runing until the user selected to exit
                getOptionCorrectly =True

            else:
                print("Please enter options on the menu")
            
        except (TypeError,NameError,ValueError):
            print("Please enter options on the menu")
    

if __name__ =="__main__":
        main()
