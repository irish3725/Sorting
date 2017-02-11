#!/usr/bin/env python3

from random import randint

myList = []
length = 0;

""" 
"   This class contains all of the sorting methods used by
"   the main class in sorting. I could have put all of the 
"   code into one file, but I wanted to learn how to call 
"   methods from different files.
"""
class C:

    """
    "   generateList() generates a random list and prints it out.
    "
    "   parameter n is the maximum value that each value in the list can be.
    "   parameter size is the number of values that will be in the list.
    """
	def generateList(self, n, size):
		global myList
		myList = []
		length = n
		for i in range(0, length):
			myList.append(randint(0, size))

    """
    "   printList() prints the list preceded and followed by a line to
    "   make it more readable.
    """
    def printList(self):
		print("--------------------------------------------------------------")
		print(myList)
		print("--------------------------------------------------------------")

    """
    "   bubbleSort() sorts the global list myList using the bubble 
    "   sort algorithm
    "
    "   parameter n is the size of the list.
    """
	def bubbleSort(self, n):
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

    """
    "   insertionSort() sorts the global list myList using the 
    "   insertion sort algorithm
    """
	def insertionSort(self):
		global myList
		fList = []
		for i in myList:
			inserted = False
			if not fList:
				fList.append(i)
			else:
				index  = -1
				for j in fList:
					index = index + 1
					if(i < j):
						fList.insert(index, i)
						inserted = True
						break
				if not inserted:
					fList.append(i)
		myList = fList

    """
    "   freq() finds the value that shows up the most in the randomly
    "   generated list and the value that shows up the least. It then
    "   prints these values and tells you how often they showed up.
    """
	def freq(self):
		count = 0
		minval = 0
		mincount = -1
		maxval = 0
		maxcount = -1
		val = 0
		tempcount = 0
		for i in myList:
			if(i == val):
				tempcount = tempcount + 1
			elif(mincount == -1):
				maxcount = tempcount
				maxval = val
				mincount = tempcount
				minval = val
				tempcount = 1
				val = i
				count = count + 1
			elif(tempcount > maxcount):
				maxcount = tempcount
				maxval = val
				tempcount = 1
				val = i
				count = count + 1
			elif(tempcount < mincount or mincount == -1):
				mincount = tempcount
				minval = val
				tempcount = 1
				val = i
				count = count + 1
			else:
				tempcount = 1
				val = i
				count = count + 1
			if(count < val):
				mincount = 0
				minval = count
				count = val
		if(tempcount > maxcount):
			maxcount = tempcount
			maxval = val
		if(tempcount < mincount):
			mincount = tempcount
			minval = val
		print("The value that showed up the least was " + str(minval) + ", and it showed up " + str(mincount) + " times.")
		print("The value that showed up the most was " + str(maxval) + ", and it showed up " + str(maxcount) + " times.")
