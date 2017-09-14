from django.shortcuts import render
from django.http import HttpResponseRedirect
from startForm import StartForm

def start(request):
	if request.method == 'POST':
		form = StartForm(request.POST)

		started = request.POST['getStarted']

		if started == "1":
			return HttpResponseRedirect('/record/')
		elif started == "2":
			return HttpResponseRedirect('/new/')
		else:
			form = StartForm()
	else:
		form = StartForm()

	return render(request, 'start.html', {'form':form})
