#!/usr/bin/python

from datetime import datetime
import sys
import csv
import re
import operator

# parsing code from http://www.seehuhn.de/blog/52

def parseLogLine(line):
    parts = [
        r'(?P<host>\S+)',                   # host %h
        r'\S+',                             # indent %l (unused)
        r'(?P<user>\S+)',                   # user %u
        r'\[(?P<time>.+)\]',                # time %t
        r'"(?P<request>.+)"',               # request "%r"
        r'(?P<status>[0-9]+)',              # status %>s
        r'(?P<size>\S+)',                   # size %b (careful, can be '-')
        #r'"(?P<referer>.*)"',               # referer "%{Referer}i"
        #r'"(?P<agent>.*)"',                 # user agent "%{User-agent}i"
    ]
    pattern = re.compile(r'\s+'.join(parts)+r'\s*\Z')

    m = pattern.match(line)

    res = None
    if m != None:
        res = m.groupdict()
    else:
        print "does not match:"
        print line 
        print r'\s+'.join(parts)+r'\s*\Z'
        print "^^^"

    return res

def updateStats(stats, page):
    if page in stats:
        stats[page] += 1
    else:
        stats[page] = 1

def mapper():
    reader = csv.reader(sys.stdin, delimiter='\t')
    # writer = csv.writer(sys.stdout, delimiter='\t', quotechar='"', quoting=csv.QUOTE_ALL)

    stats = {}

    for line in sys.stdin:
        l = parseLogLine(line.strip())

        if l != None:
            request = l["request"]
            request = request.split()[1] # " ".join(request.split()[1:])

            if request.startswith("http") or request.startswith("https"):
                request = "/" + "/".join(request.split("/")[3:])

            #print request

            updateStats(stats, request)

    stats = sorted(stats.iteritems(), key=operator.itemgetter(1))

    for s in stats:
        print s[0], "=>", s[1]

# This function allows you to test the mapper with the provided test string
def main():
    mapper()

main()
