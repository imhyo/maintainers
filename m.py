#!/usr/bin/python
import sys

class SubSystemInfo:
	info = {}

	def printInfoItem(self, *keys):
		for key in keys:
			if self.info.has_key(key):
				print self.info[key] + '\t',

	def printInfo(self):
		self.printInfoItem('!', 'M', 'L', 'W', 'Q', 'T', 'S', 'F')
		print

		self.info.clear()

	def processTitle(self, line):
		self.info['!'] = line[:-1]

	def processInfo(self, line):
		if self.info.has_key(line[0]):
			self.info[line[0]] += ", " + line[3:-1]
		else:
			self.info[line[0]] = line[3:-1]

	def processLine(self, line):
		if len(line) < 2:	# Empty Line
			self.printInfo()
		elif line[1] != ':':	# SubSystem Tile Line
			self.processTitle(line)
		else:
			self.processInfo(line)


def getMaintainersFileName():
	if len(sys.argv) >= 2:
		return sys.argv[1]
	return 'Maintainers'

def main():
	subSystemInfo = SubSystemInfo()
	f = open(getMaintainersFileName())

	for line in f:
		subSystemInfo.processLine(line)

main()

