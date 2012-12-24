#!/usr/bin/python
import sys

class SubSystemInfo:
	info = {}
	isBeginning = True
	labels = (('!', 'Name'), \
		('M', 'Maintainers'), \
		('L', 'Mailing List'), \
		('W', 'Web Page'), \
		('Q', 'Patchwork Site'), \
		('T', 'SCM Type/Location'), \
		('S', 'Status'), \
		('F', 'Files'), \
		('X', 'Files not Maintained'), \
		('K', 'Perl Matching Keyword'), \
		('t', 'Type'))

	
	def printLabels(self):
		for e in self.labels:
			print e[1] + '\t',
		print

	def printInfoItem(self):
		for e in self.labels:
			if self.info.has_key(e[0]):
				print self.info[e[0]] + '\t',
			else:
				print '\t',

	def printInfo(self):
		self.printInfoItem()
		print

		self.info.clear()

	def setType(self, t):
		if not self.info.has_key('t'):
			self.info['t'] = t
		elif self.info['t'].find(t) < 0:
			self.info['t'] += ', ' + t
		
	def checkType(self, line):
		if line[1] != ':':
			if line[:-1].rfind('DRIVER') >= 0 or line[:-1].rfind('DRIVERS') >= 0:
				self.setType('Driver')
		elif line[0] == 'F':
			if line.find('drivers/') >= 0:
				self.setType('Driver')
			elif line.find('arch/') >= 0:
				self.setType('Arch')

	def processTitle(self, line):
		self.checkType(line)
		self.info['!'] = line[:-1]

	def processInfo(self, line):
		self.checkType(line)
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
	subSystemInfo.printLabels()

	for line in f:
		subSystemInfo.processLine(line)

main()

