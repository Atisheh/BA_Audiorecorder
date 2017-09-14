import sqlite3

class StreamList(object):
	
	def __init__(self, dbFile):
		self.__db = sqlite3.connect(dbFile) #__db private
		self.__cursor = self.__db.cursor()

	def insertEntry(self, url, name, bitrate, format):
		sql = '''INSERT INTO Record VALUES ('{}', '{}', '{}', '{}')'''.format (name, url, bitrate, format)
		self.__cursor.execute(sql)
		self.__db.commit()

	def deleteEntry(self, name):
		sql = '''DELETE FROM Record WHERE name = ('{}')'''.format(name)
		self.__cursor.execute(sql)
		self.__db.commit()

	def getEntries(self):
		sql = ''' SELECT * FROM Record '''
		self.__cursor.execute(sql)
		self.__db.commit()
		return self.__cursor.fetchall()

	def getName(self):
		sql = ''' SELECT name FROM Record '''
		self.__cursor.execute(sql)
		self.__db.commit()
		return self.__cursor.fetchall()

if __name__ == '__main__':
	pass
	#sl = StreamList('dbDatei.sqlite3')
	#sl.createGbTable() #bereits angelegt
	# sl.insertEntry('hallo')
	# sl.insertEntry('ich habe einen namen', 'heinz')
	# sl.deleteEntry('heinz')
	# for e in sl.getEntries():
	# 	print e