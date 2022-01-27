from NumberList import NumberList # NumberList class is in file NumberList.py
import sys # for sys.argv and sys.exit() 


def main():
    nlist = NumberList()

    nargs = len(sys.argv) # argv contains the program name and arguments, as in C
    if nargs == 1: # no arguments, actually only the program name hence value 1
        nlist.getDataFromKeyboard()
    elif nargs == 2: # filename argument, get data from file
        print("get data set from file option not yet implemented!")
        sys.exit() # terminate program
    elif nargs == 3 or nargs == 4: # produce data set randomly
        if nargs == 3:
            nlist.getRandomData(sys.argv[1], sys.argv[2])
        else: # nargs = 4
            nlist.getRandomData(sys.argv[1], sys.argv[2], sys.argv[3])
    else:
        print("incorrect number of arguments, try again");
        sys.exit() # terminate program

    print("Numbers: " + str(nlist.getData())) 
    print("Mean: " + str(mean(nlist.getData())))
    print("Variance: " + str(variance(nlist.getData()))) 
