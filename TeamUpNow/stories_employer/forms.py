from django import forms

from stories_employer.models import Story_employer


from django.forms import ClearableFileInput

class NewStoryForm_employer(forms.ModelForm):
	content = forms.FileField(widget=forms.ClearableFileInput(attrs={'multiple': True}), required=True)
	caption = forms.CharField(widget=forms.Textarea(attrs={'class': 'input is-medium'}), required=True)

	class Meta:
		model = Story_employer
		fields = ('content', 'caption')