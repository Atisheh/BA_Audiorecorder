#-*- encoding: utf-8 -*-
import sys
import os
sys.path.append(os.getcwd())


import urllib
import dbEx


class Record(object):

	#Konstruktor
	def __init__(self, link, length, filename, bitrate):

#vars		
		self.link = link
		self.length = length
		self.filename = filename + '.mp3'
		self.bitrate = bitrate
		self.format = 'mp3'

		self.dbCon = dbEx.StreamList('dbStream.sqlite')		

# setter
	def setLink(self, link):
		self.link = link

	def setLength(self, length):
		self.length = length

	def setFilename(self, filename):
		self.filename = filename + '.mp3'

	def setBitrate(self, bitrate):
		self.bitrate = bitrate

# getter   
	def getLink(self):
		return self.link

	def getLength(self):
		return self.length

	def getFilename(self):
		return self.filename

	def getBitrate(self):
		return self.bitrate

#functions
	def recordStream(self):
		'''record stream while chunking files'''

		src = urllib.urlopen(self.getLink(), proxies={'http': "http://proxy.fh-brandenburg.de:3128", 'https': "http://proxy.fh-brandenburg.de:3128"})

		#src = urllib.urlopen(self.getLink())

		if not os.path.exists('C:\\records'):
			os.makedirs('C:\\records')

		#chunking now

		chunk = 1
		newFilename = self.filename[:self.filename.rfind('.')]
		extension = self.filename[self.filename.rfind('.'):]
		
		dest = open('C:\\records\\' + newFilename + str(chunk) + extension, 'wb')  #nutzer darf kein.mp3 eingeben --> gui
		for x in range(self.length):
			if (x % 60 == 0) & (x > 0):
				chunk += 1
				dest.close()
				dest = open('C:\\records\\' + newFilename + str(chunk) + extension, 'wb')
			dest.write(src.read((self.bitrate * 1000) / 8))
		dest.close()

		print "done"

	def entryDB(self):
		''' new db entry '''
		self.dbCon.insertEntry(self.link, self.filename, self.bitrate, self.format)

	def useDB(self):
		''' get db data to use later'''
		database = []
		database = self.dbCon.getEntries()
		return database

	def showRecords(self):
		dirList = os.listdir('C:\\records\\')
		return dirList


if __name__ == '__main__':
	pass

	# recordOne = Record('http://www.fluxfm.de/stream-berlin', 10, 'test', 128)
	# recordOne.recordStream()
	# recordOne.useDB()
	# recordOne.showRecords()

	#TAGS RAUS!
