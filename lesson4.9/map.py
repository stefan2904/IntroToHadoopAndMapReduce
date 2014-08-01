#!/usr/bin/python

from datetime import datetime
import sys
import csv
import re


def updateStats(stats, weekday, money):
    if weekday in stats:
        stats[weekday][0] += money
        stats[weekday][1] += 1
    else:
        stats[weekday] = [money, 1]

def mapper():
    reader = csv.reader(sys.stdin, delimiter='\t')
    # writer = csv.writer(sys.stdout, delimiter='\t', quotechar='"', quoting=csv.QUOTE_ALL)

    stats = {}

    for line in reader:
    	date = line[0]
        money = float(line[4])

        weekday = datetime.strptime(date, "%Y-%m-%d").weekday()

    	updateStats(stats, weekday, money)

    print stats

    for s, m in stats.iteritems():
        print s, (m[0] / m[1])

# This function allows you to test the mapper with the provided test string
def main():
    mapper()

main()
