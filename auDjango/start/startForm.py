from django import forms

class StartForm(forms.Form):

	START = ((1, "Record a Stream"), (2, "Make a new database entry"))

	getStarted = forms.ChoiceField(choices=START, required=True, label='What do you want to do?')
