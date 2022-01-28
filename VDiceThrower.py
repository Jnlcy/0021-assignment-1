
  
from random import randint
import random
random.seed(10)

#function to get input side of the dice from the key board
def getNSidefromKeyboard():
  print("Enter number of side: ")#ask input from user
  gotSideCorrectly = False #set a flag to loop until getting correct input
  while gotSideCorrectly == False:
    try:
      nside = int(input())
      if nside > 0:
        gotSideCorrectly =True
      else:
        print("getNSidefromKeyboard: The dice should have positive number of sides.")
    except(NameError,ValueError):
        print("getNSidefromKeyboard: Number of sides should be interger!")
  #end of while loop     
  return int(nside) 

#function to get number of times to throw the dice from the user
def getNThrowfromKeyboard():
  print("Enter number of times to throw:")
  gotThrowCorrectly = False #set a flag to loop until getting correct input
  while gotThrowCorrectly == False:
    try:
      nthrow = int(input())
      if nthrow > 0:
        gotThrowCorrectly =True
      else:
         print("getNThrowfromKeyboard: Number of throwe should be interger.")
    except(NameError,ValueError,TypeError):
      print("getNThrowfromKeyboard: Number of throwe should be interger!")
  #end of while loop
  return int(nthrow) 

def main():
  nside = getNSidefromKeyboard()
  nthrow = getNThrowfromKeyboard()
#initialize the list of size y
  Dice_list = [None]*nthrow

  #store random values in a list
  for i in range (0,nthrow):
    Dice_list[i] = randint(1,nside)
  #end of for loop
  print("Results:")
  print(Dice_list)
  #count elements of the list 
  for j in range(1,nside+1):
    count = Dice_list.count(j)
    print('Number of',j,':',count)
  #end of for loop

if __name__ == "__main__":
  main() 

