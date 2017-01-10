#!/usr/bin/env python3

from random import randint

myList = []
length = 0;
#for i in range(0, n)
#	myList.append(randint(0,100))

class C:
	def generateList(self, args):
		length = args
		for i in range(0, length):
			myList.append(randint(0,100))
	def printList(self):
		print("--------------------------------------------------------------")
		for x in myList:
 			print(x, end=" ")
		print("\n--------------------------------------------------------------")

	def bubbleSort(self, n):
		print(n)
		for x in myList:
			n = n - 1
			i = 0
			for y in myList:
				if(i < n):
					if (myList[i] > myList[i + 1]):
						temp = myList[i + 1]
						myList[i + 1] = myList[i]
						myList[i] = temp
				i = i + 1
		return myList
