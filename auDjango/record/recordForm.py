from django import forms

class RecordForm(forms.Form):

	DUR = ((1,64), (2, 128))

	fileName = forms.CharField(required=True)
	url = forms.URLField(label='URL', required=True)
	bitrate = forms.ChoiceField(choices=DUR, required=True, initial=2)
	duration = forms.IntegerField(required=True)
	
