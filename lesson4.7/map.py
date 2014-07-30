#!/usr/bin/python
"""
Your mapper function should print out 10 lines containing longest posts, sorted in
ascending order from shortest to longest.
Please do not use global variables and do not change the "main" function.
"""
from string import punctuation
from collections import Counter
import sys
import csv
import re

def appendToIndex(reverseIndex, localCounter, index):
	for word in localCounter:
		if word in reverseIndex:
			reverseIndex[word].append(index)
		else:
			reverseIndex[word] = [index]

def mapper():
    reader = csv.reader(sys.stdin, delimiter='\t')
    # writer = csv.writer(sys.stdout, delimiter='\t', quotechar='"', quoting=csv.QUOTE_ALL)

    globalCounter = Counter()
    reverseIndex = {}

    for line in reader:
    	try:
    		i = int(float(line[0])) # id
    	except ValueError:
    		print "ValueError:", line[0]
    		continue 
    	s = line[4].lower() # forum post
    	s = re.split(" |\.|,|!|\?|:|;|\"|\(|\)|\<|\>|\[|\]|#|\$|=|\-|\/|\n", s)

    	localCounter = Counter(s)
    	globalCounter.update(localCounter)

    	appendToIndex(reverseIndex, localCounter, i)

    print globalCounter["fantastic"]
    print sorted(reverseIndex["fantastically"])

# This function allows you to test the mapper with the provided test string
def main():
    mapper()

main()
