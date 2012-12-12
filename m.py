#!/usr/bin/python
import sys

file = 'Maintainers'
if len(sys.argv) >= 2:
	file = sys.argv[1]

f = open(file)
for line in f:
	print line



