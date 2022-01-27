import random # for Random class methods in the full version
class NumberList:
    def __init__ (self): # the class constructor
        self._data = [] # initialises the _data “private” instance variable to an empty list
    def getData (self):
        return self._data# returns the contained data list to users of the class

    def setData (self, data):
        self._data = data # initialises the list with “externally-created” data
# end class
def mean (data):
    return sum(data)/len(data)
 # function implementation goes here

def variance (data):
    m = sum(data)/len(data)
    var = sum((x-m)**2 for x in data) / len(data)
    return var
 # function implementation goes here

def main ():
    mydata = [0.1, 1.1, 2.1, 3.1, 4.1] # hardcoded data set values, list with 5 elements
    nlist = NumberList() # create new empty NumberList object instance
    nlist.setData(mydata) # fill it in with the data set
    print("Numbers: " + str(nlist.getData())) # print the data set
    print("Mean: " + str(mean(nlist.getData()))) # calculate and print mean
    print("Variance: " + str(variance(nlist.getData()))) # calculate and print variance

if __name__ == "__main__":
    main()
