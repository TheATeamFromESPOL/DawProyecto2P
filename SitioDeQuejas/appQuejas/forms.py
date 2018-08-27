from django import forms
from .models import *

class ContactForm(forms.Form):
    subject = forms.CharField(max_length=100)
    name = forms.CharField(max_length=100, required=False)
    email = forms.EmailField()
    content = forms.CharField(widget=forms.Textarea)

class QuejaForm(forms.ModelForm):
	class Meta:
		model = Queja
		fields = '__all__'
