#!/usr/bin/python

from datetime import datetime
import sys
import csv
import re


def updateStats(stats, money):
    if stats != {}:
        stats[0][0] += 1
        stats[0][1] += money
        #print stats
    else:
        stats[0] = [1, money]

def mapper():
    reader = csv.reader(sys.stdin, delimiter='\t')
    # writer = csv.writer(sys.stdout, delimiter='\t', quotechar='"', quoting=csv.QUOTE_ALL)

    stats = {}

    for line in reader:
        money = float(line[4])

        updateStats(stats, money)

    print stats

# This function allows you to test the mapper with the provided test string
def main():
    mapper()

main()
