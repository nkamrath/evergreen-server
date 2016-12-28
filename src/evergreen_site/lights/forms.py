from django import forms

class LightsForm(forms.Form):
	name = forms.CharField(max_length=64)
	ipAddress = forms.Charfield(max_length=20)
	currentState = forms.CharField(max_length=10)
	autoOffTimeSeconds = forms.CharField(max_length=10)
	lastBeaconTime = forms.DateField()