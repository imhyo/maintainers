#!/usr/bin/python
import sys

class SubSystemInfo:
	info = {}
	isBeginning = True

	def printInfoItem(self, *keys):
		for key in keys:
			if self.info.has_key(key):
				print self.info[key] + '\t ',
			else:
				print '\t ',

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
			if self.isBeginning:
				self.isBeginning = False
			else:
				self.printInfo()
		elif line[1] != ':':	# SubSystem Tile Line
			self.processTitle(line)
		else:
			self.processInfo(line)


def getMaintainersFileName():
	if len(sys.argv) >= 2:
		return sys.argv[1]
	return 'MAINTAINERS'

def skipHeader(f):
	for line in f:
		if line.find('---') >= 0:
			break

def main():
	subSystemInfo = SubSystemInfo()
	try:
		f = open(getMaintainersFileName())
	except IOError:
		print 'Cannot open the file' 
		exit()

	skipHeader(f)

	for line in f:
		subSystemInfo.processLine(line)

main()

