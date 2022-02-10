
  
from random import randint
import random


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
        print("getNSidefromKeyboard: The dice should have positive number of sides,try again!")
    except(NameError,ValueError):
        print("getNSidefromKeyboard: Number of sides should be interger, try again!")
  #end of while loop     
  return int(nside) 

#function to get number of times to throw the dice from the user
def getNThrowfromKeyboard(nside):
  print("Enter number of times to throw:")
  gotThrowCorrectly = False #set a flag to loop until getting correct input
  while gotThrowCorrectly == False:
    try:
      nthrow = int(input())
      if nthrow > 0 and nthrow% nside == 0:
        gotThrowCorrectly =True
      else:
         print("getNThrowfromKeyboard: Number of throw should be interger and should be the multiple of the number of sides,try again!")
    except(NameError,ValueError,TypeError):
      print("getNThrowfromKeyboard: Number of throwe should be interger,try again!")
  #end of while loop
  return int(nthrow) 

def main():
  nside = getNSidefromKeyboard()
  nthrow = getNThrowfromKeyboard(nside)

  
  Dice_list = [None]*nthrow#initialize the list of size y
  

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

