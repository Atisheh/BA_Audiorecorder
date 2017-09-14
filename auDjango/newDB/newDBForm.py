from django import forms

class NewDBForm(forms.Form):

	DUR = ((1, 64), (2, 128))

	name = forms.CharField(required=True)
	url = forms.URLField(label='URL', required=True)
	bitrate = forms.ChoiceField(choices=DUR, required=True, initial= 2)
