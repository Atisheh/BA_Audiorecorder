import sys
from django.shortcuts import render
from django.http import HttpResponseRedirect
sys.path.append("C:\\Users\\deso\\Documents\\fh\\4. Semester\\Objektorientierte Sprachen\\")
from newDBForm import NewDBForm
from audiorecorder import *

def new(request):
	if request.method == 'POST':
		form = NewDBForm(request.POST)

		if form.is_valid():
			
			name = form.cleaned_data['name']
			url = form.cleaned_data['url']
			bitrate = form.cleaned_data['bitrate']
			bitrate = int(bitrate) * 64
			type(bitrate)

			rec = Record(url, 0, name, bitrate)
			rec.dbCon = dbEx.StreamList('../dbStream.sqlite')	
			rec.entryDB()

			return HttpResponseRedirect('/start/')

	else:
		form = NewDBForm()

	return render(request, 'newDB.html', {'form':form})