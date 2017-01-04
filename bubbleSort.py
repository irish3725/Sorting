#!/usr/bin/env python3

from random import randint

mylist = []
for x in range(19):
    mylist.append(randint(0,100))

class C:
	def printList(self):
		print("--------------------------------------------------------------")
		for x in range(19):
    			print(mylist[x], end=", ")
		print("\n--------------------------------------------------------------")

	def bubbleSort(self):
		for x in range(19):
			for y in range(19 - x):
				if(y < 18 and mylist[y] > mylist[y + 1]):
					temp = mylist[y + 1]
					mylist[y + 1] = mylist[y]
					mylist[y] = temp


c = C()
c.printList()
c.bubbleSort()
c.printList()
