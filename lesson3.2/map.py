
#!/usr/bin/python

from datetime import datetime
import sys
import csv
import re


def updateStats(stats, cat, money):
    if cat in stats:
        stats[cat] += money
    else:
        stats[cat] = money

def mapper():
    reader = csv.reader(sys.stdin, delimiter='\t')
    # writer = csv.writer(sys.stdout, delimiter='\t', quotechar='"', quoting=csv.QUOTE_ALL)

    stats = {}

    for line in reader:
        cat = line[3]
        money = float(line[4])

        updateStats(stats, cat, money)

    print stats

    for s, m in stats.iteritems():
        print s, m

# This function allows you to test the mapper with the provided test string
def main():
    mapper()

main()
