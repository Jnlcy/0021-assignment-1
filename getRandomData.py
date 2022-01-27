import random
class NumberList:
    def __init__(self):
        self._data=[] #initialise the data private instance variable to an empty list

    def getData(self):
        return self._data

    def setData(self,data):
        self._data = data #intialis the list with  externally created data

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
    nlist.getRandomData(5, 10)
  
    print("Numbers: " + str(nlist.getData()))
    print("Mean: " + str(mean(nlist.getData())))
    print("Variance: " + str(variance(nlist.getData()))) 

if __name__ == "__main__":
    main() 