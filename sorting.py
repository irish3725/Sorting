#!/usr/bin/env python3

from random import randint

myList = []
length = 0;

class C:
    def generateList(self, n, size):
        global myList
        myList = []
        length = n
        for i in range(0, length):
            myList.append(randint(0, size))

    def printList(self):
        print("--------------------------------------------------------------")
        print(myList)
        print("--------------------------------------------------------------")

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

    def quickSort(self, start, end):
        global length
        global myList
        if(start == -1)
            start = 0;
            end = length - 1
        last = end
        first = start
        pivot = randint(start, end)		
        temp = myList[pivot]
        myList[pivot] = myList[end]
        myList[end] = temp
        pivot = end
        end = end - 1
		
        while(start < end):
            if(myList[start] > pivot):
                while(myList[end] > pivot):
                    end = end - 1
                temp = myList[start]
                myList[start] = myList[end]
                myList[end] = temp
            elif(myList[end] <= pivot):
                while(myList[start] <= pivot)
                    start = start + 1 
                temp = myList[start]
                myList[start] = myList[end]
                myList[end] = temp
            end = end - 1
            start = start + 1
        temp = myList[pivot]
        myList[pivot] = myList[start]
        myList[start] = temp
        quickSort(first, start)
        quickSort(start + 1, last)
	
        print("not yet implimented")

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
        print("The value that showed up the least was " 
                + str(minval) + ", and it showed up " 
                + str(mincount) + " times.")
        print("The value that showed up the most was " 
                + str(maxval) + ", and it showed up " 
                + str(maxcount) + " times.")
