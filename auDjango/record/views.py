import sys
import threading
from django.shortcuts import render
from django.http import HttpResponseRedirect
sys.path.append("C:\\Users\\deso\\Desktop\\Audiorecorder")
from recordForm import RecordForm
from audiorecorder import *

def rec(request):
	if request.method == 'POST':
		form = RecordForm(data=request.POST)

		if form.is_valid():

			filename = form.cleaned_data['fileName']
			url = form.cleaned_data['url']
			bitrate = form.cleaned_data['bitrate']
			bitrate = int(bitrate) * 64
			duration = form.cleaned_data['duration']
			duration = int(duration)

			rec = Record(url, duration, filename, bitrate)

			t = threading.Thread(target = rec.recordStream())
			t.start()

			return HttpResponseRedirect('/start/')

	else:
		form = RecordForm()

	return render(request, 'newRecord.html', {'form':form}) 