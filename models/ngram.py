#! /usr/bin/env python

from collections import Counter

class Ngram:

	def __init__(self, n):
		if not isinstance(n, int):
			raise Exception('N should be an integer')
		if n < 0:
			raise Exception('Negative n is not allowed')
		self.n = n


	def getNext(self, items):
		length = len(items)

		if length <= self.n:   
			return -1

		nextChoices = []
		lastN = items[-self.n:]             # last n items
		for i in range(length - self.n):
			currN = items[i:i+self.n] 
			if  currN == lastN:
				nextChoices.append(items[i+self.n]) # for every sequence equal to the last n items, save the next item in a list
		
		if nextChoices: 
			frequencies = Counter(nextChoices)            # get the frequency for each distinct saved item
			return max(frequencies, key=frequencies.get)  # return the item with the highest frequency
		else:
			return -1
	