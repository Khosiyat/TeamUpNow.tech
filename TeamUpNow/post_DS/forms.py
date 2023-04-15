from django import forms
from django.forms import ModelForm
from django.contrib.auth.models import User

from post_DS.models import Experience_chart, Post_DS

from django.forms import ClearableFileInput


from OptionField_DS.models import *


from skills_TaggingField.models import *




# ################################################################################################ CHOICES


# ##################################-----> create field | CHOOSE ONE ---->ManyToMany

# PROJECT_EXPERICE=[
# 	('Naive ', 'Naive '),
# 	('Experienced ', 'Experienced '),
# 	('Expert ', 'Expert '),
# ]


# SOLVING_APPROACH_SPECIFIC =[
# 	('Naive ', 'Naive '),
# 	('Experienced ', 'Experienced '),
# 	('Expert ', 'Expert '),
# ]


# SOLVING_APPROACH_GENERAL = [
# 	('Naive ', 'Naive '),
# 	('Experienced ', 'Experienced '),
# 	('Expert ', 'Expert '),
# ]



# FOCUS_STYLE = [
# 	('Naive ', 'Naive '),
# 	('Experienced ', 'Experienced '),
# 	('Expert ', 'Expert '),

# ]


# BEHAVIORAL_CHALLENGE = [
# 	('Naive ', 'Naive '),
# 	('Experienced ', 'Experienced '),
# 	('Expert ', 'Expert '),
# ]




# ###################################-----> FORMS | CHOOSE MULTIPLE




# ################################################### METHOD INFO OPTION

# TASK_TYPE=[
# 	("General Task","General Task"),
# 	("Multistage tasks","Multistage tasks"),
# ]

# CHALLANGE_TYPE=[
# 	("Tech Language","Tech Language"),
# 	("Tech Framework","Tech Framework"),
# ]

# EVALUATION_DURATION  = [
# 	('1 day', '1 day'),
# 	('2 days', '2 days'),
# 	('3 days', '3 days'),
# 	('4 days', '4 days'),
# 	('5 days', '5 days'),
# 	('6 days', '6 days'),
# 	('1 week', '1 week'),
# 	('1-2 weeks', '1-2 weeks'),
# 	('2-3 weeks', '2-3 weeks'),
# ]

# 	# SDLC_PHASES
# SDLC_PHASES = [
# 	('Planning', 'Planning'),
# 	('Defining', 'Defining'),
# 	('Designing', 'Designing'),
# 	('Building', 'Building'),
# 	('Testing', 'Testing'),
# 	('Building', 'Building'),
# 	('Deployment', 'Deployment'),
# ]


# 	# TASK TYPE
# EXAMINE_TYPE = [
# 	('CODING', 'CODING'),
# 	('ORAL', 'ORAL'),
# 	('CODING & ORAL', 'CODING & ORAL'),

# ]

# 	# TASK METHOD
# INTERVIEW_METHOD = [
# 	('LIVE INTERVIEW', 'LIVE INTERVIEW'),
# 	('HOME ASSIGNMENT', 'HOME ASSIGNMENT'),
# 	('LIVE & HOME ASSIGNMENT', 'LIVE & HOME ASSIGNMENT'),

# ]


# TASK_COMPLETION = [
# 	('PAIR PROGRAMMING', 'PAIR PROGRAMMING'),
# 	('INDIVIDUAL PROGRAMMING', 'INDIVIDUAL PROGRAMMING'),
# ]


# 	# TASK CHOICE
# TASK_CHOICE = [
# 	('GENERAL TASK', 'GENERAL TASK'),
# 	('SPECIFIC TASK', 'SPECIFIC TASK'),
# ]

# 	# TASK CHOICE
# PROJECT_CHOICE = [
# 	('SPECIFIC PROJECT', 'SPECIFIC PROJECT'),
# 	('GRENERAL PROJECT', 'GRENERAL PROJECT'),
# ]


# ################################################### DEGREE OPTION

# GENERAL_DEGREE_OF_THE_CANDIDATE = [
# 	('Junior', 'Junior'),
# 	('Middle', 'Middle'),
# 	('Senior', 'Senior'),
# ]


# DEGREE_OF_THE_CANDIDATE_TO_THIS_SPECIFIC_PROJECT = [
# 	('Junior ', 'Junior '),
# 	('Middle ', 'Middle '),
# 	('Senior ', 'Senior '),
# ]


# ################################################### SKILL SETS OPTION
# ############## TECH SKILLS

# 	# DATA_STRUCTURES_AND_AGLORITHMS
# DATA_STRUCTURES_AND_AGLORITHMS = [
# 	('Naive ', 'Naive '),
# 	('Experienced ', 'Experienced '),
# 	('Expert ', 'Expert '),
# ]


# 	# CODING_QUALITY
# CODING_QUALITY = [
# 	('Naive ', 'Naive '),
# 	('Experienced ', 'Experienced '),
# 	('Expert ', 'Expert '),
# ]

# 	# DATABASE_AND_SQL_OPTION
# DATABASE_AND_SQL_OPTION = [
# 	('Naive ', 'Naive '),
# 	('Experienced ', 'Experienced '),
# 	('Expert ', 'Expert '),
# ]

# 	# LANGUAGES_BACKEND_OPTION
# LANGUAGES_BACKEND_OPTION = [
# 	('Naive ', 'Naive '),
# 	('Experienced ', 'Experienced '),
# 	('Expert ', 'Expert '),
# ]

# 	# LANGUAGES_FRONTEND_OPTION
# LANGUAGES_FRONTEND_OPTION = [
# 	('Naive ', 'Naive '),
# 	('Experienced ', 'Experienced '),
# 	('Expert ', 'Expert '),
# ]

# 	# FRAMEWORK_FRONTEND_OPTION
# FRAMEWORK_FRONTEND_OPTION = [
# 	('Naive ', 'Naive '),
# 	('Experienced ', 'Experienced '),
# 	('Expert ', 'Expert '),
# ]

# 	# IDEs_OPTION
# IDEs_OPTION = [
# 	('Naive ', 'Naive '),
# 	('Experienced ', 'Experienced '),
# 	('Expert ', 'Expert '),
# ]


# 	# TEXT_EDITORS_OPTION
# TEXT_EDITORS_OPTION = [
# 	('Naive ', 'Naive '),
# 	('Experienced ', 'Experienced '),
# 	('Expert ', 'Expert '),
# ]

# 	# CLOUD_COMPUTING_OPTION
# CLOUD_COMPUTING_OPTION = [
# 	('Naive ', 'Naive '),
# 	('Experienced ', 'Experienced '),
# 	('Expert ', 'Expert '),
# ]


# 	# WEB_DEVELOPMENT_OPTION
# WEB_DEVELOPMENT_OPTION = [
# 	('Naive ', 'Naive '),
# 	('Experienced ', 'Experienced '),
# 	('Expert ', 'Expert '),
# ]

# 	# CONTAINERS_OPTION
# CONTAINERS_OPTION = [
# 	('Naive ', 'Naive '),
# 	('Experienced ', 'Experienced '),
# 	('Expert ', 'Expert '),
# ]


# ############## SOFT SKILLS

# 	# LEADERSHIP
# LEADERSHIP = [
# 	('Naive ', 'Naive '),
# 	('Experienced ', 'Experienced '),
# 	('Expert ', 'Expert '),
# ]


# 	# COMMUNICATIN_SKILLS
# COMMUNICATIN_SKILLS = [
# 	('Naive ', 'Naive '),
# 	('Experienced ', 'Experienced '),
# 	('Expert ', 'Expert '),
# ]



# 	# TIME_MANAGEMENT
# TIME_MANAGEMENT = [
# 	('Naive ', 'Naive '),
# 	('Experienced ', 'Experienced '),
# 	('Expert ', 'Expert '),
# ]


# 	# LEARNING_CAPACITY
# LEARNING_CAPACITY = [
# 	('Naive ', 'Naive '),
# 	('Experienced ', 'Experienced '),
# 	('Expert ', 'Expert '),
# ]


# 	# JOB_PERFORMENCE
# JOB_PERFORMENCE = [
# 	('Naive ', 'Naive '),
# 	('Experienced ', 'Experienced '),
# 	('Expert ', 'Expert '),
# ]


# 	# TEAMWORK
# TEAMWORK = [
# 	('Naive ', 'Naive '),
# 	('Experienced ', 'Experienced '),
# 	('Expert ', 'Expert '),
# ]


# ###################################-----> MANYTOMANY (CHOICE IN THE MODELS) | CHOOSE MULTIPLE


# BEHAVIORAL_CHALLENGE_MANYTOMANYFIELD_CLASS = [
# 	('Works under pressure', 'Works under pressure'),
# 	('Can not work under pressure', 'Can not work under pressure'),
# 	]

# SOLVING_APPROACH_GENERAL_MANYTOMANYFIELD_CLASS = [
# 	('Creative & Problem Solver', 'Creative & Problem Solver'),
# 	('Uncreative', 'Uncreative'),
# 	]

# SOLVING_APPROACH_SPECIFIC_MANYTOMANYFIELD_CLASS =[
# 	('regurgitated the solution the candidate already knew','regurgitated the solution the candidate already knew'),
# 	('managed to piece together a similar solution that is correct','managed to piece together a similar solution that is correct'),
# 	('happens to have an interest in the field related to the problem domain','happens to have an interest in the field related to the problem domain')
# 	]

# PROJECT_EXPERICE_MANYTOMANYFIELD_CLASS=[
# 	('has seen this exact problem before','has seen this exact problem before'),
# 	('has seen this similar problem before','has seen this exact problem before'),
# 	('has not seen the problem and field at all','has not seen the problem and field at all'),
# 	]


# CODING_QUALITY_MANYTOMANYFIELD_CLASS = (
# 	('Existing programming knowledge are put together to solve the task at hand.', 'Existing programming knowledge are put together to solve the task at hand.'),
# 	('A script is debugged that it is entirely objective.', 'A script is debugged that it is entirely objective.'),
# 	('Deep and nuanced subjective view is given', 'Deep and nuanced subjective view is given'),
# 	('Tasks are designed with multiple possible approaches.', 'Tasks are designed with multiple possible approaches.'),
# 	('Clean code.', 'Clean code.'),
# 	('well documented.', 'well documented.'),
# 	('The code is discussed with the team.', 'The code is discussed with the team.'),
# 	('The code is analyzed', 'The code is analyzed'),
# 	('Code is debuged with other team members.', 'Code is debuged with other team members.'),
# 	('The code is refactored.', 'The code is refactored.'),
# 	('Arbitrary problems and constraints are reasoned', 'Arbitrary problems and constraints are reasoned'),
# 	)



# DATA_STRUCTURES_ALGORITHMS_MANYTOMANYFIELD_CLASS = (
# 		('Primitive Types ', 'Primitive Types '),
# 		('Convert base ', 'Convert base '),
# 		('Arrays', 'Arrays'),
# 		('Compute the max difference ', 'Compute the max difference '),
# 		('Strings', 'Strings'),
# 		('Interconvert strings and integers', 'Interconvert strings and integers'),
# 		('Reverse all the words in a sentence', 'Reverse all the words in a sentence'),
# 		('Linked Lists ', 'Linked Lists '),
# 		('Test for cyclicity', 'Test for cyclicity'),
# 		('Stacks and Queues ', 'Stacks and Queues '),
# 		('Implement a stack with max API ', 'Implement a stack with max API '),
# 		('Print a binary tree in order of increasing depth ', 'Print a binary tree in order of increasing depth '),
# 		('Binary Trees', 'Binary Trees'),
# 		('Test if a binary tree is balanced', 'Test if a binary tree is balanced'),
# 		('Heaps', 'Heaps'),
# 		('Merge sorted files', 'Merge sorted files'),
# 		('Searching', 'Searching'),
# 		('Search a sorted array for first occurrence of k', 'Search a sorted array for first occurrence of k'),
# 		('Hash Tables ', 'Hash Tables '),
# 		('Test if an anonymous letter is constructible', 'Test if an anonymous letter is constructible'),
# 		('Sorting', 'Sorting'),
# 		('Compute the intersection of two sorted arrays', 'Compute the intersection of two sorted arrays'),
# 		('Binary Search Trees ', 'Binary Search Trees '),
# 		('Test if a binary tree satisfies the BST property', 'Test if a binary tree satisfies the BST property'),
# 		('Recursion', 'Recursion'),
# 		('Enumerate the power set', 'Enumerate the power set'),
# 		('Dynamic Programming ', 'Dynamic Programming '),
# 		('Count the number of ways to traverse a 2D array ', 'Count the number of ways to traverse a 2D array '),
# 		('Greedy Algorithms and Invariants ', 'Greedy Algorithms and Invariants '),
# 		('The 3-sum problem', 'The 3-sum problem'),
# 		('Graphs', 'Graphs'),
# 		('Paint a Boolean matrix', 'Paint a Boolean matrix'),
# 		('Parallel Computing', 'Parallel Computing'),
# 		('Implement a Timer class ', 'Implement a Timer class '),
# 		('Design Problems ', 'Design Problems '),
# 		('Design a system for detecting copyright infringement', 'Design a system for detecting copyright infringement'),
# 	)


# DATABASE_AND_SQL_MANYTOMANYFIELD_CLASS=[
# 	('RDMS | MySQL', 'RDMS | MySQL'),
# 	('DBMS | NoSQL', 'DBMS | NoSQL'),
# 	('DBMS | MongoDB', 'DBMS | MongoDB'),
# 	]


# LANGUAGES_BACKEND_MANYTOMANYFIELD_CLASS =[

# 	('C','C'),
# 	('C++','C++'),
# 	('Java','Java'),
# 	('Python','Python'),
# 	('GO','GO'),
# 	('Ruby', 'Ruby'),
# 	('Scala','Scala'),
# 	('JADE','JADE'),
# 	('Emerald','Emerald'),
# 	('Visual Basic .NET','Visual Basic .NET'),
# 	('PHP','PHP'),
# 	('JavaScript','JavaScript'),
# 	]

# FRAMEWORKS_BACKEND_MANYTOMANYFIELD_CLASS =[

# 	('Django','Django'),
# 	('ExpressJS','ExpressJS'),
# 	('Laravel','Laravel'),
# 	('Ruby on Rails','Ruby on Rails'),
# 	('CakePHP','CakePHP'),
# 	('Flask','Flask'),
# 	('ASP .NET Core','ASP .NET Core'),
# 	('Spring Boot','Spring Boot'),
# 	('Koa','Koa'),
# 	('Phoenix','Phoenix'),

# 	]


# FRAMEWORK_FRONTEND_MANYTOMANYFIELD_CLASS=[

# 	('HTML','HTML'),
# 	('CSS','CSS'),
# 	('JavaScript ','JavaScript '),
# 	('React','React'),
# 	('Angular','Angular'),
# 	('Vue','Vue'),
# 	('TypeScript ','TypeScript '),
# 	('Elm','Elm'),
# 	('jQuery','jQuery'),
# 	('Swift ','Swift '),

# 	]


# IDES_MANYTOMANYFIELD_CLASS =[

# 	('Visual Studio','Visual Studio'),
# 	('Visual Studio Code','Visual Studio Code'),
# 	('AWS Cloud9','AWS Cloud9'),
# 	('SlickEdit','SlickEdit'),
# 	('Eclipse Theia','Eclipse Theia'),
# 	('IntelliJ IDEA','IntelliJ IDEA'),
# 	('PyCharm','PyCharm'),
# 	('Xcode','Xcode'),
# 	('NetBeans','NetBeans'),
# 	('GNAT Studio','GNAT Studio'),
# 	('Eclipse','Eclipse'),
# 	]

# TEXT_EDITORS_MANYTOMANYFIELD_CLASS=[

# 	('Visual Studio Code','Visual Studio Code'),
# 	('Sublime Text','Sublime Text'),
# 	('Notepad++','Notepad++'),
# 	('UltraEdit','UltraEdit'),
# 	]

# CLOUD_COMPUTING_MANYTOMANYFIELD_CLASS=[

# 	('Amazon Web Services (AWS)','Amazon Web Services (AWS)'),
# 	('Microsoft Azure','Microsoft Azure'),
# 	('Google Cloud Platform (GCP)','Google Cloud Platform (GCP)'),
# 	]

# WEB_DEVELOPMENT_MANYTOMANYFIELD_CLASS=[

# 	('API','API'),
# 	('Chrome Developer Tools','Chrome Developer Tools'),
# 	('jQuery','jQuery'),
# 	('GitHub','GitHub'),
# 	('CodePen','CodePen'),
# 	('Angular.js','Angular.js'),
# 	('Sass','Sass'),
# 	]

# CONTAINERS_MANYTOMANYFIELD_CLASS=[

# 	('Docker','Docker'),
# 	('AWS Fargate','AWS Fargate'),
# 	('Google Kubernetes Engine','Google Kubernetes Engine'),
# 	('Amazon ECS','Amazon ECS'),
# 	('Linux Containers','Linux Containers'),
# 	('Microsoft Azure Container Services','Microsoft Azure Container Services'),

# 	('Database systems', 'Database systems'),
# 	('Computer networking', 'Computer networking'),
# 	('Data structures and algorithms', 'Data structures and algorithms'),
# 	('Computer security', 'Computer security'),
# 	('Distributed systems', 'Distributed systems'),
# 	('Software development', 'Software development'),
# 	('Operating systems', 'Operating systems'),
# 	('Programming languages', 'Programming languages'),
# 	('Advanced Computer Architecture', 'Advanced Computer Architecture'),

# 	]

# TEAMWORK_MANYTOMANYFIELD_CLASS = (
# 		("Confers with users in the development of a software solution.", "Confers with users in the development of a software solution."),
# 		("Mentors software developers", "Mentors software developers"),
# 		("Resolve a Disagreement on Implementation", "Resolve a Disagreement on Implementation"),
# 		)

# JOB_PERFORMENCE_MANYTOMANYFIELD_CLASS=(
# 	('Plans', 'Plans'),
# 	('Researches','Researches'),
# 	('Analysis' ,'Analysis'),
# 	('Systems analysis' ,'Systems analysis'),
# 	('Analyzes reported' ,'Analyzes reported'),
# 	('Makes determinations', 'Makes determinations'),
# 	('Develops the solution' ,'Develops the solution'),
# 	('Designs system specifications' ,'Designs system specifications'),
# 	('Designs standards', 'Designs standards'),
# 	('Designs programming' ,'Designs programming'),
# 	('Gains approvals' ,'Gains approvals'),
# 	('Improves operations' , 'Improves operations'),
# 	('Implementing a software solution', 'Implementing a software solution'),
# 	('Conducts a specific task', 'Conducts a specific task'),
# 	('Makes decision when handover to the software testing team', 'Makes decision when handover to the software testing team'),
# 	('Analyses a software development lifecycle.', 'Analyses a software development lifecycle.'),
# 	('Develops a software development lifecycle.', 'Develops a software development lifecycle.'),
# 	('Works autonomously on an operational feasibility task. ', 'Works autonomously on an operational feasibility task.'),
# 	('Develops software project from build to release','Develops software project from build to release'),
# 	)


# LEARNING_CAPACITY_MANYTOMANYFIELD_CLASS= (
# 	(' Can have technical solution for complex and potentially unique software problem.', ' Can have technical solution for complex and potentially unique software problem.'),
# 	('Assess the problem', 'Assess the problem'),
# 	('Undertakes research and analysis', 'Undertakes research and analysis'),
# 	('Manages risk', 'Manages risk'),
# 	('Uses external resource(stack overflow, etc)', 'Uses external resource(stack overflow, etc)'),
# 	('Researches to understand of business needs within your company.' , 'Researches to understand of business needs within your company.' ),
# 	('Learns and adapts quickly.' ,'Learns and adapts quickly.'),
# 	('Assess the technical specifications' , 'Assess the technical specifications'),
# 	)

# FOCUS_STYLE_MANYTOMANYFIELD_CLASS = [
# 	('Goal orientated', 'Goal orientated'),
# 	('Action-oriented', 'Action-oriented'),
# 	('Result oriented', 'Result oriented'),

# 	]
	
# TIME_MANAGEMENT_MANYTOMANYFIELD_CLASS=(
# 	(' Developed personal management method ' ,' Developed personal management method '),
# 	(' Management method for hectic multi-tasking ' ,' Management method for hectic multi-tasking '),
# 	('Management method for setting specific periods for a single task.' , 'Management method for setting specific periods for a single task.' ),
# 	('Has experience in enhancing timelines and productivity.' , 'Has experience in enhancing timelines and productivity.' ),
# 	('Delegates task on time' , 'Delegates task on time'),
# 	('Chooses team members to work on specific tasks', 'Chooses team members to work on specific tasks'),
# 	('Creates small team units to work together', 'Creates small team units to work together'),
# 	('Implements a time management methodology across the software development team.', 'Implements a time management methodology across the software development team.'),
# 	('Strictly prioritizes tasks as part of others’ time management strategy.' , 'Strictly prioritizes tasks as part of others’ time management strategy.' ),
# 	('Prioritizes over other tasks', 'Prioritizes over other tasks'),
# 	('Incorporates team timelines and needs into this', 'Incorporates team timelines and needs into this'),
# 	)


# COMMUNICATION_SKILS_MANYTOMANYFIELD_CLASS=(
# 	('Works with cross-functional teams', 'Works with cross-functional teams'),
# 	('Higher management ', 'Higher management '),
# 	('Software development project. ', 'Software development project. '),
# 	('Expresses complex information to non-experts in the field', 'Expresses complex information to non-experts in the field'),
# 	('Processes their needs against your own.', 'Processes their needs against your own.'),
# 	('Presents software architectural overview. ', 'Presents software architectural overview. '),
# 	('Consistent in efficiency and clarity' , 'Consistent in efficiency and clarity'),
# 	('Resolves a communication problem by thinking ', 'Resolves a communication problem by thinking '),
# 	("Learns to see things from anther's perspective", "Learns to see things from anther's perspective"),
# 	('Prevents conflict of ideas among the development team. ', 'Prevents conflict of ideas among the development team. '),
# 	('Assess the various opinions', 'Assess the various opinions'),
# 	('Feedback is solution based', 'Feedback is solution based'),
# 	('Resistance to listening to objections or ideas. ', 'Resistance to listening to objections or ideas. '),
# 	('Responds to this realization', 'Responds to this realization'),
# 	)

# LEADERSHIP_MANYTOMANYFIELD_CLASS=(

# 	('Independent judgment as a senior team member ', 'Independent judgment as a senior team member '),
# 	('Chooses a leadership through team autonomy methodology', 'Chooses a leadership through team autonomy methodology'),
# 	('Deals with issues arose', 'Deals with issues arose'),
# 	(' Motivates the team', ' Motivates the team'),
# 	('Challenges and rewards the team', 'Challenges and rewards the team'),
# 	('Can have methods of stimulation the team', 'Can have methods of stimulation the team'),
# 	('Involves the team while effectively taking charge', 'Involves the team while effectively taking charge'),
# 	('Assesses expert opinions against the noise', 'Assesses expert opinions against the noise'),
	
# 	)


# class NewPostForm_DS(ModelForm):
# 	class Meta:
# 		model = Post_DS
# 		fields = ('behavioural_challange', 'score_behavioural_challange', 'behavioural_challange_OPTION', 'note_behavioural_challange')
# 		exclude = ['user', 'posted', 'likes']
# 		labels = {
# 			'behavioural_challange': 'behavioural_challange',
# 			'task_method': 'task_method',
# 			'behavioural_challange_OPTION': 'behavioural_challange_OPTION',
# 			'note_behavioural_challange': 'note_behavioural_challange',		
# 		}
# 		widgets = {
# 			'behavioural_challange': forms.CheckboxSelectMultiple(attrs={'class':'form-select', 'placeholder':'behavioural_challange'}),
# 			'score_behavioural_challange': forms.TextInput(attrs={'class':'form-control', 'placeholder':'score_behavioural_challange'}),
# 			'behavioural_challange_OPTION': forms.Select(attrs={'class':'form-select', 'placeholder':'behavioural_challange_OPTION'}),
# 			'note_behavioural_challange': forms.TextInput(attrs={'class':'form-control', 'placeholder':'note_behavioural_challange'}),
# 		}

from bootstrap_datepicker_plus.widgets import DatePickerInput, TimePickerInput
class Experience_chart_Form_DS(forms.ModelForm):

	technical_task = forms.ChoiceField(widget=forms.Select, choices=TASK)
	technical_ocuppation = forms.ChoiceField(widget=forms.Select, choices=OCCUPATION)
	# start_date = forms.DateField(widget=DatePickerInput().start_of('event days'))
	# finish_date = forms.DateField(widget=DatePickerInput().start_of('event days'))

	# start_date = forms.CharField(widget = forms.SelectDateWidget())
	# finish_date = forms.CharField(widget = forms.SelectDateWidget())



	class Meta:
		model = Experience_chart
		exclude = ['id', 'user', 'week_number', 'posted']
		fields = '__all__'
		# fields = 'technical_task', 'technical_ocuppation', 'start_date', 'finish_date'
		widgets = {
            'start_date':DatePickerInput(),
            'finish_date':DatePickerInput(),
        }





class NewPostForm_DS(forms.ModelForm):
	# attendees_evaluated = forms.MultipleChoiceField(widget=forms.CheckboxSelectMultiple,choices=__________)
	# attendees_evaluated = forms.CharField(widget=forms.Textarea(attrs={'class': 'input is-medium'}), required=True)
	# attendees_evaluated=forms.ChoiceField(widget=forms.Select)
	
	# #METHOD TYPES

	task_choice=forms.ChoiceField(widget=forms.Select, choices=TASK_CHOICE)

	project_choice=forms.ChoiceField(widget=forms.Select, choices=PROJECT_CHOICE)

	examine_types=forms.ChoiceField(widget=forms.Select, choices=EXAMINE_TYPE)

	task_method=forms.ChoiceField(widget=forms.Select, choices=INTERVIEW_METHOD)

	task_completion=forms.ChoiceField(widget=forms.Select, choices=TASK_COMPLETION)

	sdls_phase=forms.ChoiceField(widget=forms.Select, choices=SDLC_PHASES)

	evaluation_duration=forms.ChoiceField(widget=forms.Select, choices=EVALUATION_DURATION)



	#CODE QUALITY

	clean_SCORE = forms.IntegerField(label="clean code quality: min-1 max-4", widget=forms.NumberInput(attrs={'class': 'form-control'}), required=True)
	clean_NOTE = forms.CharField(label="clean code quality note", widget=forms.Textarea(attrs={'class': 'input is-medium'}), required=False)

	refactored_SCORE  = forms.IntegerField(label="refactored quality: min-1 max-4", widget=forms.NumberInput(attrs={'class': 'form-control'}), required=True)
	refactored_NOTE = forms.CharField(label="refactored quality note", widget=forms.Textarea(attrs={'class': 'input is-medium'}), required=False) 

	well_documented_SCORE  = forms.IntegerField(label="well documented quality: min-1 max-4", widget=forms.NumberInput(attrs={'class': 'form-control'}), required=True)
	well_documented_NOTE = forms.CharField(label="well documented quality note", widget=forms.Textarea(attrs={'class': 'input is-medium'}), required=False)

	unit_tested_SCORE  = forms.IntegerField(label="unit tested quality: min-1 max-4", widget=forms.NumberInput(attrs={'class': 'form-control'}), required=True)
	unit_tested_NOTE = forms.CharField(label="unit tested quality note", widget=forms.Textarea(attrs={'class': 'input is-medium'}), required=False)

	debuged_SCORE  = forms.IntegerField(label="debugging quality: min-1 max-4", widget=forms.NumberInput(attrs={'class': 'form-control'}), required=True)
	debuged_NOTE = forms.CharField(label="debugging quality note", widget=forms.Textarea(attrs={'class': 'input is-medium'}), required=False)

	debuged_with_other_team_members_SCORE  = forms.IntegerField(label="debuged with other team members: min-1 max-4", widget=forms.NumberInput(attrs={'class': 'form-control'}), required=True)
	debuged_with_other_team_members_NOTE = forms.CharField(label="debuged with other team members note", widget=forms.Textarea(attrs={'class': 'input is-medium'}), required=False)
	
	debuged_other_team_members_bugs_SCORE  = forms.IntegerField(label="debuged other team members bugs: min-1 max-4", widget=forms.NumberInput(attrs={'class': 'form-control'}), required=True)
	debuged_other_team_members_bugs_NOTE = forms.CharField(label="debuged other team members bugs note", widget=forms.Textarea(attrs={'class': 'input is-medium'}), required=False) 

	#PROCESS QUALITY

	analyzed_SCORE  = forms.IntegerField(label="analizing quality: min-1 max-4", widget=forms.NumberInput(attrs={'class': 'form-control'}), required=True)
	analyzed_NOTE =  forms.CharField(label="analizing quality note", widget=forms.Textarea(attrs={'class': 'input is-medium'}), required=False)

	analyzed_with_other_team_members_SCORE  = forms.IntegerField(label="analyzed with other team members: min-1 max-4", widget=forms.NumberInput(attrs={'class': 'form-control'}), required=True)
	analyzed_with_other_team_members_NOTE = forms.CharField(label="analyzed with other team members note", widget=forms.Textarea(attrs={'class': 'input is-medium'}), required=False)

	analyzed_other_team_members_script_SCORE  = forms.IntegerField(label="analyzed other team members script: min-1 max-4", widget=forms.NumberInput(attrs={'class': 'form-control'}), required=True)
	analyzed_other_team_members_script_NOTE = forms.CharField(label="analyzed other team members script note", widget=forms.Textarea(attrs={'class': 'input is-medium'}), required=False) 


	discussed_SCORE  = forms.IntegerField(label="discussing the code: min-1 max-4", widget=forms.NumberInput(attrs={'class': 'form-control'}), required=True)
	discussed_NOTE = forms.CharField(label="discussing the code note", widget=forms.Textarea(attrs={'class': 'input is-medium'}), required=False) 

	discussed_with_other_team_members_SCORE  = forms.IntegerField(label="discussed with other team members: min-1 max-4", widget=forms.NumberInput(attrs={'class': 'form-control'}), required=True)
	discussed_with_other_team_members_NOTE = forms.CharField(label="discussed with other team members note", widget=forms.Textarea(attrs={'class': 'input is-medium'}), required=False)


	expected_problems_are_reasoned_SCORE  = forms.IntegerField(label="expected_problems_are_reasoned: min-1 max-4", widget=forms.NumberInput(attrs={'class': 'form-control'}), required=True)
	expected_problems_are_reasoned_NOTE = forms.CharField(label="expected_problems_are_reasoned note", widget=forms.Textarea(attrs={'class': 'input is-medium'}), required=False) 

	arbitrary_problems_are_reasoned_SCORE  = forms.IntegerField(label="arbitrary problems are reasoned: min-1 max-4", widget=forms.NumberInput(attrs={'class': 'form-control'}), required=True)
	arbitrary_problems_are_reasoned_NOTE = forms.CharField(label="arbitrary problems are reasoned note", widget=forms.Textarea(attrs={'class': 'input is-medium'}), required=False) 


	expected_constraints_are_reasoned_SCORE  = forms.IntegerField(label="expected constraints are reasoned: min-1 max-4", widget=forms.NumberInput(attrs={'class': 'form-control'}), required=True)
	expected_constraints_are_reasoned_NOTE = forms.CharField(label="expected constraints are reasoned note", widget=forms.Textarea(attrs={'class': 'input is-medium'}), required=False)

	arbitrary_constraints_are_reasoned_SCORE  = forms.IntegerField(label="arbitrary constraints are reasoned: min-1 max-4", widget=forms.NumberInput(attrs={'class': 'form-control'}), required=True)
	arbitrary_constraints_are_reasoned_NOTE = forms.CharField(label="arbitrary constraints are reasoned note", widget=forms.Textarea(attrs={'class': 'input is-medium'}), required=False) 


	designed_with_one_approach_SCORE  = forms.IntegerField(label="designed with one approach: min-1 max-4", widget=forms.NumberInput(attrs={'class': 'form-control'}), required=True)
	designed_with_one_approach_NOTE = forms.CharField(label="designed with one approach note", widget=forms.Textarea(attrs={'class': 'input is-medium'}), required=False) 

	designed_with_multiple_possible_approaches_SCORE  = forms.IntegerField(label="designed with multiple possible approaches: min-1 max-4", widget=forms.NumberInput(attrs={'class': 'form-control'}), required=True)
	designed_with_multiple_possible_approaches_NOTE = forms.CharField(label="designed with multiple possible approaches note", widget=forms.Textarea(attrs={'class': 'input is-medium'}), required=False)
	
	
	class Meta:
		model = Post_DS
		exclude = ['user', 'posted', 'likes', 'relevancy', 'conciseness']
		fields = '__all__'











	# # #METHOD TYPES
	# task_choice

	# project_choice

	# examine_types

	# task_method

	# task_completion

	# sdls_phase

	# evaluation_duration


	# #CODE QUALITY

	# clean_SCORE
	# clean_NOTE

	# refactored_SCORE
	# refactored_NOTE

	# well_documented_SCORE
	# well_documented_NOTE

	# unit_tested_SCORE
	# unit_tested_NOTE

	# debuged_SCORE
	# debuged_NOTE

	# debuged_with_other_team_members_SCORE  
	# debuged_with_other_team_members_NOTE
	
	# debuged_other_team_members_bugs_SCORE
	# debuged_other_team_members_bugs_NOTE

	# #PROCESS QUALITY

	# analyzed_SCORE
	# analyzed_NOTE

	# analyzed_with_other_team_members_SCORE
	# analyzed_with_other_team_members_NOTE

	# analyzed_other_team_members_script_SCORE
	# analyzed_other_team_members_script_NOTE


	# discussed_SCORE
	# discussed_NOTE

	# discussed_with_other_team_members_SCORE
	# discussed_with_other_team_members_NOTE


	# expected_problems_are_reasoned_SCORE
	# expected_problems_are_reasoned_NOTE

	# arbitrary_problems_are_reasoned_SCORE
	# arbitrary_problems_are_reasoned_NOTE 


	# expected_constraints_are_reasoned_SCORE
	# expected_constraints_are_reasoned_NOTE

	# arbitrary_constraints_are_reasoned_SCORE
	# arbitrary_constraints_are_reasoned_NOTE 


	# designed_with_one_approach_SCORE
	# designed_with_one_approach_NOTE 

	# designed_with_multiple_possible_approaches_SCORE
	# designed_with_multiple_possible_approaches_NOTE
	