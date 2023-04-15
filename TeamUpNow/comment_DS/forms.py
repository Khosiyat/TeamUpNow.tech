from django import forms
from comment_DS.models import Comment_DS
from OptionField_DS.models import *

class CommentForm_DS(forms.ModelForm):
	body = forms.CharField(widget=forms.Textarea(attrs={'class': 'textarea'}), initial='My note: ', required=False)
	
	request_talents=forms.ChoiceField(widget=forms.RadioSelect, choices=REQUEST_TALENTS, required=True)
	sdls_phase=forms.ChoiceField(widget=forms.Select, choices=SDLC_PHASES, required=True)
	ocuppation=forms.ChoiceField(widget=forms.Select, choices=OCCUPATION, required=True)


	class Meta:
		model = Comment_DS
		exclude = ['user', 'body', 'post']
		fields = '__all__'



# request_talents,database_and_SQL, language_backend, framework_frontend, framework_backend, cloud_comuting, web_development, containers,

# request_talents
# database_and_SQL
# language_backend
# framework_frontend
# framework_backend
# cloud_comuting
# web_development
# containers
