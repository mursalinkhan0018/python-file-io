#! /usr/bin/env python3

"A script to macth words and bring line numbers in tabular form."

import sys
import re
from tabulate import tabulate

#lineno=1
#pattern = '^\b(IN)'
#regex = re.compile("^\b(IN)")
with open (sys.argv[1], 'r') as file:
    data = file.read()
#    print(type(data))
#    print(data)
regex = re.compile("(inherit|INHERIT)(\w*)")
results = []
for lineno, line in enumerate(data.split("\n")):
    if regex.search(line):
        output = regex.search(line)
        a = output.group()
        results.append((lineno, a))
#        results.append((lineno, line))
#print(results)
#print(tabulate(results, headers=['Line', 'Match']))
sys.stdout = open("output_table.txt", "w")
print(tabulate(results, headers=['Line', 'Match']))
#print("Hello World")
sys.stdout.close()

#print(__name__)

if __name__ == '__main__':
    if len(sys.argv) < 1:
        print ('You failed to provide input text file')
    sys.exit(1)  # abort because of error

