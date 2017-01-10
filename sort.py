#!/usr/bin/env python3

from random import randint
from bubbleSort import *

done = False

while not done:
	c = C()
	choiceDone = False
	instring = input('How large would you like your list?\n> ')
	length = int(instring)
	print('You inputted ' + instring)
	print('Here is your new list:')
	c.generateList(length)
	c.printList()
#	myList = []
#	for i in range(length):
#		myList.append(randint(0,100))
#	c.printList(myList)
#	print("-----------------------------")
#	for i in range(length):
#		print(myList[i], end=' ')
#	print("\n-----------------------------\n")
	
	while not choiceDone:
		print("Which sort method would you like to use?")
		instring = input("(1)BubbleSort (2)CoctailShakerSort (3)Quit\n> ")
		if instring is "1":
			print("You chose BubbleSort")
			c.bubbleSort(length)
			c.printList()
			choiceDone = True
		if instring is "2":
			print("you chose CoctailShakerSort")
			choiceDone = True
		if instring is "3":
			choiceDone = True
			done = True
#		else 
#			print("type either 1 or 2")

