import sys
import os
sys.path.append(os.getcwd())
import argparse
import audiorecorder

parser = argparse.ArgumentParser(description='Audiorecorder')
parser.add_argument('url', type=str, help='URL des Streams')
parser.add_argument('-f', dest='filename', type=str, required=True, help='Name des Audiofiles')
parser.add_argument('-d', '--duration', required=True, type=int, default=20, help='Bitte geben Sie die Dauer der Aufnahme an!')
parser.add_argument('-b', '--bitrate', required=True, type=int, default=128, help='Bitrate in kBit/s', choices=[128, 64]) #bit 1000/byte 1024
parser.add_argument('-r', '--record', help='Aufnahme') #-r True
parser.add_argument('-a', '--addtodb', help='Eintrag zu Datenbank hinzufuegen')
parser.add_argument('-s', '--showdb', help='zeigt Datenbankeintraege an')
parser.add_argument('-z', '--showrec', help='zeigt alle Aufnahmen an')   
arguments = parser.parse_args()


if(arguments.url, arguments.filename, arguments.bitrate):
	rec = audiorecorder.Record(arguments.url, arguments.duration, arguments.filename, arguments.bitrate)
	if (arguments.record):
		rec.recordStream()
	elif (arguments.addtodb):
		rec.entryDB()
	elif (arguments.showdb):
		print rec.useDB()
	elif (arguments.showrec):
		print rec.showRecords()
	else: 
		print "Please choose between the following actions: --record, --addtodb, --showdb, --showrec"
else:
	"Some required arguments are missing"
