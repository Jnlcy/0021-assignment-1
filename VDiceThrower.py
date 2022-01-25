try:
  
  from random import randint
  import random
  random.seed(10)

  #ask input from the user
  x = int(input('Please enter the number of sides of the dice\n'))
  y = int(input('Please enter the number of times to be thrown\n'))
  if x <= 0 or y <= 0:
    raise IndexError
    
  else:

  #initialize the list of size y
    Dice_list = [None]*(y+1)
  #store random values in a list
    for i in range (0,y):
      Dice_list[i] = randint(1,x)
  #count elements of the list 
    for j in range(1,x+1):
      count = Dice_list.count(j)
      print('Number of',j,':',count)
      
#except cases where the      
except ValueError:
  print('Please input integer numbers')
except IndexError:
  print('Inputs has to be positive')
