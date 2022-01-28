
class NumberList:
    def __init__ (self): # the class constructor
        self._data = [] # initialises the _data “private” instance variable to an empty list
    def getData (self):
        return self._data# returns the contained data list to users of the class

    def setData (self, data):
        self._data = data # initialises the list with “externally-created” data

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

# end class

from NumberList import NumberList
def mean (data):
    return sum(data)/len(data)
 # function implementation goes here

def variance (data):
    m = sum(data)/len(data)
    var = sum((x-m)**2 for x in data) / len(data)
    return var
 # function implementation goes here


def main ():
    nlist = NumberList()
    nlist.getDataFromKeyboard()
  
    print("Numbers: " + str(nlist.getData()))
    print("Mean: " + str(mean(nlist.getData())))
    print("Variance: " + str(variance(nlist.getData()))) 

if __name__ == "__main__":
    main() 
