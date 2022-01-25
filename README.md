#ELEC0021 programming assignment


## PROGRAMMING ASSIGNMENT – Part 1A
Virtual Dice Throwing
This is an introductory programming exercise in order to refresh your last year’s knowledge of
programming and get you introduced to Python. The program to write should emulate virtual
dice throwing. It should get from the keyboard the number of sides of the virtual dice and the
number of times to be thrown, the latter should be a multiple of the number of sides. The
program should then throw the dice and print out the number of times each side occurred. Given
that random numbers will be used, you should be able to see that the higher the number of
throws, the closer the results will be towards approximately equal occurrence of all sides (same
probability). The program should deal gracefully with incorrect type of arguments through
checks and exceptions.
This program can be in fact an extension of the coin thrower program which can be found on
the Week 2 Random Number Generation lecture material. 

## PROGRAMMING ASSIGNMENT – Part 1B
Calculating the Mean and Variance of a Data Set – “the Long Way”
This is another introductory programming exercise so that you start getting familiar with some
more sophisticated aspects of Python. “The long way” is mentioned above because the
description of this assignment also serves as a tutorial introduction to various aspects of
structured and object-oriented programming in Python, and for this reason this description is 5
pages long. It also includes a good part of the assignment already implemented in order to show
how things should be done properly. So please go through this description very carefully as it
constitutes in fact an additional lecture.
The program to be developed in this exercise should calculate the mean and variance of a series
of numbers, i.e. “the data set”. This is something that could be easily done in C through a
program that would have the following structure: two C functions mean and variance and a
main program that initialises an array of numbers, invokes the two functions by passing to them
the array as parameter and prints the respective results. The “signature” of the two functions
would be the following:
 float mean (int ndata, float data[])
 float variance (int ndata, float data[])
Note that in C we need to pass the size of the array, i.e. ndata, as a separate parameter, as the
array is effectively only a pointer to its first element, no more than that.
We could write a similar program in Python by mirroring exactly the structure of the C program,
but given that this year you will be exposed to object-oriented (O-O) programming, we will do
it slightly differently. We will create a reusable class for the data set which will include various
functions (or, more precisely, methods in O-O terminology) for initialising the data in a number
of ways: by getting it from the keyboard, by generating random values in a particular specified
range or by reading the data values from a file (although we will leave this last option out).
After the assignment, this class could be put aside and be used in other contexts. 
We will also write the mean and variance functions, which in Python will have the following
simpler signature:
 def mean (data)
 def variance (data)
Finally, we will write a main program which will allow the initialisation of the data set in a
number of ways and will then compute the mean and standard deviation.
We are now ready to implement our first simple object-oriented class and program in Python
in an incremental manner, showing basic parts of it and its overall layout but omitting the
complete implementation, which you should do. 

## PROGRAMMING ASSIGNMENT – Part 1C
Shape Inheritance
This exercise has the purpose first to get you to implement the Shape, Point, Circle and Cylinder
classes as in the lecture notes in order to get to understand better, assimilate and actually code
the inheritance features taught in the lectures. Although you can simply copy the code from the
notes, it would be certainly more beneficial to write the code yourselves by looking at the notes
in order to realise how object-oriented features related to inheritance are exercised and
understand / assimilate the relevant principles. In addition to the classes in the notes, you should
also design and implement the following shape classes exploiting inheritance: Sphere,
Rectangle, Square and Cube.
Having implemented these classes, you should write a which gets input from the user/keyboard
to create an instance of any one of these. The user should be able to create as many of these
shapes and s/he wants. The menu should also allow the user to print out the created objects,
either selecting a particular one or printing them all. The user should also be allowed to
remove/delete an existing shape from the list. Finally, the user could be allowed to modify a
particular shape. The program should print the objects it keeps by using only the Shape
getName(), toString(), getArea() and getVolume() methods, i.e. treating all these objects
“polymorphically” as “shapes”. Note that modifying a shape cannot be done polymorphically,
specific functions will be required to modify each type of shape. The program should deal
gracefully with incorrect type of arguments through checks and exceptions. 

