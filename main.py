#!/usr/bin/env python3

from random import randint
from sorting import *

done = False

while not done:
	c = C()
	choiceDone = False
	instring = input('How large would you like your list?\n> ')
	length = int(instring)
	print('You inputted ' + instring)
	instring = input('How large would you like the numbers to get?\n> ')
	size = int(instring)
	print('You inputted ' + instring)
	print('Here is your new list:')
	c.generateList(length, size)
	c.printList()	
	while not choiceDone:
		print("Which sort method would you like to use?")
		instring = input("(1)Bubble Sort (2)Insertion Sort (3)Quick Sort (4)Quit\n> ")
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
			c.quickSort()
			c.printList()
			c.freq()
			choiceDone = True
		elif instring is "4":
			choiceDone = True
			done = True
		else: 
			print("Please type a number between 1 and 3.")

