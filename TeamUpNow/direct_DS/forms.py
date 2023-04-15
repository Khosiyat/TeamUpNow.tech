from django import forms

from post_DS.models import Post_DS


from skills_TaggingField.models import (
						BehaviouralChallange,
						)


from django.contrib.auth.models import User

from direct_DS.models import Message_DS

from OptionField_DS.models import *


from bootstrap_datepicker_plus.widgets import DatePickerInput, TimePickerInput, DateTimePickerInput, MonthPickerInput, YearPickerInput


# class MessageSendForm_DS(forms.ModelForm):

# 	STATUS_CHOICE = [
# 	('PAIR CODING', 'PAIR CODING'),
# 	('INDIVIDUAL CODING', 'INDIVIDUAL CODING'),
# 	('BEHAVORIAL INTERVIEW', 'BEHAVORIAL INTERVIEW'),
# 	('SIMULATED PROJECTS', 'SIMULATED PROJECTS'),
# 	('ASSIGNMENT CHECKING', 'ASSIGNMENT CHECKING'),
	
# 	]

# 	#PROBLEM SOLVING SKILL
# 	body=forms.ChoiceField(widget=forms.RadioSelect, choices=STATUS_CHOICE)
	
# 	class Meta:
# 		model = Message_DS
# 		exclude = ['user', 'sender', 'recipient', 'body', 'is_read']
# 		fields = ('body',)



class MessageSendForm_DS(forms.ModelForm):

	EXAM_TYPE = [
	('PAIR CODING', 'PAIR CODING'),
	('INDIVIDUAL CODING', 'INDIVIDUAL CODING'),
	('BEHAVORIAL INTERVIEW', 'BEHAVORIAL INTERVIEW'),
	('SIMULATED PROJECTS', 'SIMULATED PROJECTS'),
	('ASSIGNMENT CHECKING', 'ASSIGNMENT CHECKING'),
	
	]

	SCHEDULE_STATUS = [
	('can be changed', 'can be changed'),
	('can not be changed', 'can not be changed'),
	]

	#PROBLEM SOLVING SKILL
	body=forms.ChoiceField(widget=forms.RadioSelect, choices=EXAM_TYPE)
	body2=forms.ChoiceField(widget=forms.RadioSelect, choices=SCHEDULE_STATUS)
	# start_date=forms.DateField(widget=DatePickerInput().start_of('event days'))
	# end_date=forms.DateField(widget=DatePickerInput().end_of('event days'))
	# start_time=forms.DateField(widget=TimePickerInput().start_of('party time'))
	# end_time=forms.DateField(widget=TimePickerInput().end_of('party time'))

	task_choice=forms.ChoiceField(widget=forms.RadioSelect, choices=TASK_CHOICE)
	project_choice=forms.ChoiceField(widget=forms.RadioSelect, choices=PROJECT_CHOICE)
	examine_types=forms.ChoiceField(widget=forms.RadioSelect, choices=EXAMINE_TYPE)
	task_method=forms.ChoiceField(widget=forms.RadioSelect, choices=INTERVIEW_METHOD)
	task_completion=forms.ChoiceField(widget=forms.RadioSelect, choices=TASK_COMPLETION)
	sdls_phase=forms.ChoiceField(widget=forms.RadioSelect, choices=SDLC_PHASES)
	evaluation_duration=forms.ChoiceField(widget=forms.RadioSelect, choices=EVALUATION_DURATION)
	
	class Meta:
		model = Message_DS
		exclude = ['user', 'sender', 'recipient', 'is_read']
		fields = ['body', 'body2', "project_choice", "task_choice", "project_choice", "examine_types", "task_method", "task_completion", "sdls_phase", "evaluation_duration",  'start_date', 'end_date', 'start_time', 'end_time']
		widgets = {
            'start_date':DatePickerInput(),
            'end_date':DatePickerInput(),
            'start_time':TimePickerInput(),
            'end_time':TimePickerInput(),
        }

