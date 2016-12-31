from django import forms
from lights.models import Light

class LightForm(forms.ModelForm):
	name = forms.CharField(max_length=64, help_text='Name: ')
	ip_address = forms.CharField(max_length=20, help_text='IP Address: ')

	class Meta:
		model = Light
		fields = ('ip_address', 'name') #these are the fields of light form