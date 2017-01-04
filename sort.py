#!/usr/bin/env python3

from random import randint

done = False
while not done:
	input = input('How large would you like your list?\n> ')
	length = int(input)
	print('You inputted ' + input)
	print('here is your new list:')
	list = []
	for i in range(length):
		list.append(randint(0,100))
	print("-----------------------------")
	for i in range(length):
		print(list[i], end=' ')
	print("\n-----------------------------")
