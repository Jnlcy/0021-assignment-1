import random
class NumberList:
    def __init__(self):
        self._data=[] #initialise the data private instance variable to an empty list

    def getData(self):
        return self._data

    def setData(self,data):
        self._data = data #intialis the list with  externally created data

    def _getNDataFromKeyboard (self): # private method names should start with _
        print("Enter the number of data set elements: ")
        ndata = 0
        gotNDataCorrectly = False # a flag to loop until we get ndata correctly
        while gotNDataCorrectly == False:
            try:
                ndata = float(input()) # read from the keyboard, accept also strings & convert
                if ndata % 1 == 0 and ndata >= 2: # check for integer input >= 2
                    gotNDataCorrectly = True
                else:
                    print("_getNDataFromKeyboard: ndata should be >=2")
            except (NameError, SyntaxError,ValueError):
                print("_getNDataFromKeyboard: ndata should be an integer!")
         # end while loop
        return int(ndata) # we accept float numbers but "floor" them to int 
    
    def getDataFromKeyboard(self):
        ndata = self._getNDataFromKeyboard() 
        mydata=[]
        
        for n in range (0,ndata):    
        
            gotDataCorrectly = False #a Flag to loop until getting data correctly
            while gotDataCorrectly == False:
                try:
                    print("Enter data element "+ str(n+1)+":")
                    datainput = float(input())#read from the keyboard
                    mydata.append(datainput)
                    gotDataCorrectly = True 

                except(NameError,SyntaxError,ValueError):
                    print("getDataFromKeyboard: data should be a float number")        
            #endwhile          
        #endforloop
        NumberList.setData(self,mydata)
        
    def getRandomData(self,ndata,range1,range2=0):
        if ndata % 1 == 0 and ndata >= 2:
            if range1 > range2:#set two variables low and high according to the range1 and range2 values
                high = range1
                low = range2

            elif range1 < range2:
                high = range2
                low =range1
            else:
                print("The range should not be the same")
            mydata=[] #initialise an empty list

            for i in range (0,ndata):
                mydata.append(random.random() *(high-low) + low)
            #end of for loop
            NumberList.setData(self,mydata)
        else:
            print("getRandomData:Number of data should be >=2")
    
    

