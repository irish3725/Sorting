#!/usr/bin/env python3

from random import randint
from bubbleSort import *

# done keeps track of wheter or not the program should be running.
done = False

"""
"   This while loop is the UI that tells the user what is happening
"   and allows the user to choose the size of the list, the range
"   of values in the list, and which algorithm to use to sort it. 
"""
while not done:
	c = C()
	choiceDone = False
    
    # ask for size of list
	instring = input('How large would you like your list?\n> ')
	length = int(instring)
	print('You inputted ' + instring)
    
    # ask for range of values
	instring = input('How large would you like the numbers to get?\n> ')
	size = int(instring)
	print('You inputted ' + instring)
    
    # generate and print list
	print('Here is your new list:')
	c.generateList(length, size)
	c.printList()	
    
    # gives user choice of sorting algorithm
	while not choiceDone:
		print("Which sort method would you like to use?")
		instring = input("(1)Bubble Sort (2)Insertion Sort (3)Quit\n> ")
		if instring is "1":
			print("You chose Bubble Sort")
			c.bubbleSort(length)
			c.printList()
			c.freq()
			choiceDone = True
		elif instring is "2":
			print("you chose Insertion Sort")
			c.insertionSort()
			c.printList()
			c.freq()
			choiceDone = True
		elif instring is "3":
			choiceDone = True
			done = True
		else: 
			print("Please type a number between 1 and 3.")

