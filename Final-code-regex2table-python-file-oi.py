#! /usr/bin/env python3


import sys
import re
from tabulate import tabulate

#lineno=1
#pattern = '^\b(IN)'
#regex = re.compile("^\b(IN)")
with open ("origin.txt", 'r') as file:
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
