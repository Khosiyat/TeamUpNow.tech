from django.db import models



################################################################################################ SKILL SETS


class TechSkills(models.Model):
	TECH_SKILLS = (
	('Database and SQL', 'Database and SQL'),
	('Object-oriented programming (OOP) languages', 'Object-oriented programming (OOP) languages'),
	('Integrated development environments (IDEs)', 'Integrated development environments (IDEs)'),
	('Cloud computing', 'Cloud computing'),
	('Web development', 'Web development'),
	('Containers', 'Containers'),
	('Text editors', 'Text editors'),
	('Git version control', 'Git version control'),
	)

	category = models.CharField(max_length=200, null=True, choices=TECH_SKILLS)
	# category = models.CharField(max_length=200, null=True)
	# tags = models.ManyToManyField(Tag)

	def __str__(self):
		return self.category



class SoftSkills(models.Model):
	SOFT_SKILLS = (
	('Communication (verbal and written)', 'Communication (verbal and written)'),
	('Teamwork and conflict resolution', 'Teamwork and conflict resolution'),
	('Problem solving', 'Problem solving'),
	('Empathy', 'Empathy'),
	('Patience', 'Patience'),
	('Curiosity', 'Curiosity'),
	('Adaptability', 'Adaptability'),
	('Accountability', 'Accountability'),
	('Time management', 'Time management'),
	)

	category = models.CharField(max_length=200, null=True, choices=SOFT_SKILLS)

	def __str__(self):
		return self.category




######################################################################### Solving Approach
class BehaviouralChallange(models.Model):
	BEHAVIORAL_CHALLENGE = [
	('Works under pressure', 'Works under pressure'),
	('Can not work under pressure', 'Can not work under pressure'),
]
	
	category = models.CharField(max_length=200, null=True, choices=BEHAVIORAL_CHALLENGE)
	# category = models.CharField(max_length=200, null=True)
	# tags = models.ManyToManyField(Tag)

	def __str__(self):
		return self.category

class FocusStyle(models.Model):
	FOCUS_STYLE = [
	('Goal orientated', 'Goal orientated'),
	('Action-oriented', 'Action-oriented'),
	('Result oriented', 'Result oriented'),

	]
	
	category = models.CharField(max_length=200, null=True, choices=FOCUS_STYLE)
	# category = models.CharField(max_length=200, null=True)
	# tags = models.ManyToManyField(Tag)

	def __str__(self):
		return self.category

class SolvingApproachGeneral(models.Model):
	SOLVING_APPROACH_GENERAL = [
	('Creative & Problem Solver', 'Creative & Problem Solver'),
	('Uncreative', 'Uncreative'),
	]
	
	category = models.CharField(max_length=200, null=True, choices=SOLVING_APPROACH_GENERAL)
	# category = models.CharField(max_length=200, null=True)
	# tags = models.ManyToManyField(Tag)

	def __str__(self):
		return self.category

class SolvingApproachSpecific(models.Model):
	SOLVING_APPROACH_SPECIFIC =[
	('regurgitated the solution the candidate already knew','regurgitated the solution the candidate already knew'),
	('managed to piece together a similar solution that is correct','managed to piece together a similar solution that is correct'),
	('happens to have an interest in the field related to the problem domain','happens to have an interest in the field related to the problem domain')
	]
	
	category = models.CharField(max_length=200, null=True, choices=SOLVING_APPROACH_SPECIFIC)
	# category = models.CharField(max_length=200, null=True)
	# tags = models.ManyToManyField(Tag)

	def __str__(self):
		return self.category

class ProjectExperience(models.Model):
	PROJECT_EXPERICE=[
	('has seen this exact problem before','has seen this exact problem before'),
	('has seen this similar problem before','has seen this exact problem before'),
	('has not seen the problem and field at all','has not seen the problem and field at all'),
	]



	category = models.CharField(max_length=200, null=True, choices=PROJECT_EXPERICE)
	# tags = models.ManyToManyField(Tag)

	def __str__(self):
		return self.category


################################################### SKILL SETS
class CodingQuality(models.Model):
	CODING_QUALITY = (
		# ('Clean', '1'),
		# ('Refactored', '1'),
		# ('well documented', '3'),
		# ('Unit Tested', '3'),

		# ('Debuged', '1'),
		# ('Debuged with other team members', '2'),
		# ('Debuged other team members bugs', '3'),

		# ('Analyzed', '1'),
		# ('Analyzed with other team members', '2'),
		# ('Analyzed other team members script', '3'),

		# ('Discussed', '1'),
		# ('Discussed with other team members', '2'),

		# ('Expected problems are reasoned', '4'),
		# ('Arbitrary problems are reasoned', '5'),

		# ('Expected constraints are reasoned', '4'),
		# ('Arbitrary constraints are reasoned', '5'),

		# ('Designed with one approache.', '1'),
		# ('Designed with multiple possible approaches', '5'),


		# ('1', 'Clean'),
		# ('1', 'Refactored'),
		# ('3', 'well documented'),
		# ('3', 'Unit Tested'),

		# ('1', 'Debuged'),
		# ('2', 'Debuged with other team members'),
		# ('2', 'Debuged other team members bugs'),

		# ('1', 'Analyzed'),
		# ('2', 'Analyzed with other team members'),
		# ('3', 'Analyzed other team members script'),

		# ('1', 'Discussed'),
		# ('2', 'Discussed with other team members'),

		# ('4', 'Expected problems are reasoned'),
		# ('5', 'Arbitrary problems are reasoned'),

		# ('4', 'Expected constraints are reasoned'),
		# ('5', 'Arbitrary constraints are reasoned'),

		# ('1', 'Designed with one approach'),
		# ('5', 'Designed with multiple possible approaches'),



		('Clean', 'Clean'),
		('Refactored', 'Refactored'),
		('well documented', 'well documented'),
		('Unit Tested', 'Unit Tested'),

		('Debuged', 'Debuged'),
		('Debuged with other team members', 'Debuged with other team members'),
		('Debuged other team members bugs', 'Debuged other team members bugs'),

		('Analyzed', 'Analyzed'),
		('Analyzed with other team members', 'Analyzed with other team members'),
		('Analyzed other team members script', 'Analyzed other team members script'),

		('Discussed', 'Discussed'),
		('Discussed with other team members', 'Discussed with other team members'),

		('Expected problems are reasoned', 'Expected problems are reasoned'),
		('Arbitrary problems are reasoned', 'Arbitrary problems are reasoned'),

		('Expected constraints are reasoned', 'Expected constraints are reasoned'),
		('Arbitrary constraints are reasoned', 'Arbitrary constraints are reasoned'),

		('Designed with one approach.', 'Designed with one approach'),
		('Designed with multiple possible approaches', 'Designed with multiple possible approaches'),

	)

	category = models.CharField(max_length=200, null=True, choices=CODING_QUALITY)
	# tags = models.ManyToManyField(Tag)

	def __str__(self):
		return self.category



class Leadership(models.Model):
	LEADERSHIP=(

	('Independent judgment as a senior team member ', 'Independent judgment as a senior team member '),
	('Chooses a leadership through team autonomy methodology', 'Chooses a leadership through team autonomy methodology'),
	('Deals with issues arose', 'Deals with issues arose'),
	(' Motivates the team', ' Motivates the team'),
	('Challenges and rewards the team', 'Challenges and rewards the team'),
	('Can have methods of stimulation the team', 'Can have methods of stimulation the team'),
	('Involves the team while effectively taking charge', 'Involves the team while effectively taking charge'),
	('Assesses expert opinions against the noise', 'Assesses expert opinions against the noise'),
	
	)

	category = models.CharField(max_length=200, null=True, choices=LEADERSHIP)
	# category = models.CharField(max_length=200, null=True)
	# tags = models.ManyToManyField(Tag)

	def __str__(self):
		return self.category




class CommunicationSkills(models.Model):
	COMMUNICATION_SKILS=(
	('Works with cross-functional teams', 'Works with cross-functional teams'),
	('Higher management ', 'Higher management '),
	('Software development project. ', 'Software development project. '),
	('Expresses complex information to non-experts in the field', 'Expresses complex information to non-experts in the field'),
	('Processes their needs against your own.', 'Processes their needs against your own.'),
	('Presents software architectural overview. ', 'Presents software architectural overview. '),
	('Consistent in efficiency and clarity' , 'Consistent in efficiency and clarity'),
	('Resolves a communication problem by thinking ', 'Resolves a communication problem by thinking '),
	("Learns to see things from anther's perspective", "Learns to see things from anther's perspective"),
	('Prevents conflict of ideas among the development team. ', 'Prevents conflict of ideas among the development team. '),
	('Assess the various opinions', 'Assess the various opinions'),
	('Feedback is solution based', 'Feedback is solution based'),
	('Resistance to listening to objections or ideas. ', 'Resistance to listening to objections or ideas. '),
	('Responds to this realization', 'Responds to this realization'),
	)

	category = models.CharField(max_length=200, null=True, choices=COMMUNICATION_SKILS)
	# tags = models.ManyToManyField(Tag)

	def __str__(self):
		return self.category



class TimeManagement(models.Model):
	TIME_MANAGEMENT=(
	(' Developed personal management method ' ,' Developed personal management method '),
	(' Management method for hectic multi-tasking ' ,' Management method for hectic multi-tasking '),
	('Management method for setting specific periods for a single task.' , 'Management method for setting specific periods for a single task.' ),
	('Has experience in enhancing timelines and productivity.' , 'Has experience in enhancing timelines and productivity.' ),
	('Delegates task on time' , 'Delegates task on time'),
	('Chooses team members to work on specific tasks', 'Chooses team members to work on specific tasks'),
	('Creates small team units to work together', 'Creates small team units to work together'),
	('Implements a time management methodology across the software development team.', 'Implements a time management methodology across the software development team.'),
	('Strictly prioritizes tasks as part of others’ time management strategy.' , 'Strictly prioritizes tasks as part of others’ time management strategy.' ),
	('Prioritizes over other tasks', 'Prioritizes over other tasks'),
	('Incorporates team timelines and needs into this', 'Incorporates team timelines and needs into this'),
	)

	category = models.CharField(max_length=200, null=True, choices=TIME_MANAGEMENT)
	# tags = models.ManyToManyField(Tag)

	def __str__(self):
		return self.category


class LearningCapacity(models.Model):
	LEARNING_CAPACITY= (
	(' Can have technical solution for complex and potentially unique software problem.', ' Can have technical solution for complex and potentially unique software problem.'),
	('Assess the problem', 'Assess the problem'),
	('Undertakes research and analysis', 'Undertakes research and analysis'),
	('Manages risk', 'Manages risk'),
	('Uses external resource(stack overflow, etc)', 'Uses external resource(stack overflow, etc)'),
	('Researches to understand of business needs within your company.' , 'Researches to understand of business needs within your company.' ),
	('Learns and adapts quickly.' ,'Learns and adapts quickly.'),
	('Assess the technical specifications' , 'Assess the technical specifications'),
	)

	category = models.CharField(max_length=200, null=True, choices=LEARNING_CAPACITY)
	# tags = models.ManyToManyField(Tag)

	def __str__(self):
		return self.category




class JobPerformence(models.Model):
	JOB_PERFORMENCE=(
	('Plans', 'Plans'),
	('Researches','Researches'),
	('Analysis' ,'Analysis'),
	('Systems analysis' ,'Systems analysis'),
	('Analyzes reported' ,'Analyzes reported'),
	('Makes determinations', 'Makes determinations'),
	('Develops the solution' ,'Develops the solution'),
	('Designs system specifications' ,'Designs system specifications'),
	('Designs standards', 'Designs standards'),
	('Designs programming' ,'Designs programming'),
	('Gains approvals' ,'Gains approvals'),
	('Improves operations' , 'Improves operations'),
	('Implementing a software solution', 'Implementing a software solution'),
	('Conducts a specific task', 'Conducts a specific task'),
	('Makes decision when handover to the software testing team', 'Makes decision when handover to the software testing team'),
	('Analyses a software development lifecycle.', 'Analyses a software development lifecycle.'),
	('Develops a software development lifecycle.', 'Develops a software development lifecycle.'),
	('Works autonomously on an operational feasibility task. ', 'Works autonomously on an operational feasibility task.'),
	('Develops software project from build to release','Develops software project from build to release'),
	)

	category = models.CharField(max_length=200, null=True, choices=JOB_PERFORMENCE)
	# tags = models.ManyToManyField(Tag)

	def __str__(self):
		return self.category




class Teamwork(models.Model):
	TEAMWORK = (
		("Confers with users in the development of a software solution.", "Confers with users in the development of a software solution."),
		("Mentors software developers", "Mentors software developers"),
		("Resolve a Disagreement on Implementation", "Resolve a Disagreement on Implementation"),
		)

	category = models.CharField(max_length=200, null=True, choices=TEAMWORK)
	# tags = models.ManyToManyField(Tag)

	def __str__(self):
		return self.category




class DataStructuresAndAlgorithms(models.Model):
	
	DATA_STRUCTURES_ALGORITHMS = (
		('Primitive Types ', 'Primitive Types '),
		('Convert base ', 'Convert base '),
		('Arrays', 'Arrays'),
		('Compute the max difference ', 'Compute the max difference '),
		('Strings', 'Strings'),
		('Interconvert strings and integers', 'Interconvert strings and integers'),
		('Reverse all the words in a sentence', 'Reverse all the words in a sentence'),
		('Linked Lists ', 'Linked Lists '),
		('Test for cyclicity', 'Test for cyclicity'),
		('Stacks and Queues ', 'Stacks and Queues '),
		('Implement a stack with max API ', 'Implement a stack with max API '),
		('Print a binary tree in order of increasing depth ', 'Print a binary tree in order of increasing depth '),
		('Binary Trees', 'Binary Trees'),
		('Test if a binary tree is balanced', 'Test if a binary tree is balanced'),
		('Heaps', 'Heaps'),
		('Merge sorted files', 'Merge sorted files'),
		('Searching', 'Searching'),
		('Search a sorted array for first occurrence of k', 'Search a sorted array for first occurrence of k'),
		('Hash Tables ', 'Hash Tables '),
		('Test if an anonymous letter is constructible', 'Test if an anonymous letter is constructible'),
		('Sorting', 'Sorting'),
		('Compute the intersection of two sorted arrays', 'Compute the intersection of two sorted arrays'),
		('Binary Search Trees ', 'Binary Search Trees '),
		('Test if a binary tree satisfies the BST property', 'Test if a binary tree satisfies the BST property'),
		('Recursion', 'Recursion'),
		('Enumerate the power set', 'Enumerate the power set'),
		('Dynamic Programming ', 'Dynamic Programming '),
		('Count the number of ways to traverse a 2D array ', 'Count the number of ways to traverse a 2D array '),
		('Greedy Algorithms and Invariants ', 'Greedy Algorithms and Invariants '),
		('The 3-sum problem', 'The 3-sum problem'),
		('Graphs', 'Graphs'),
		('Paint a Boolean matrix', 'Paint a Boolean matrix'),
		('Parallel Computing', 'Parallel Computing'),
		('Implement a Timer class ', 'Implement a Timer class '),
		('Design Problems ', 'Design Problems '),
		('Design a system for detecting copyright infringement', 'Design a system for detecting copyright infringement'),
	)


	category = models.CharField(max_length=200, null=True, choices=DATA_STRUCTURES_ALGORITHMS)
	# tags = models.ManyToManyField(Tag)

	def __str__(self):
		return self.category




class DataBaseSQL(models.Model):
	DATABASE_AND_SQL=[
	('RDMS | MySQL', 'RDMS | MySQL'),
	('DBMS | NoSQL', 'DBMS | NoSQL'),
	('DBMS | MongoDB', 'DBMS | MongoDB'),
	]

	category = models.CharField(max_length=200, null=True, choices=DATABASE_AND_SQL)
	# tags = models.ManyToManyField(Tag)

	def __str__(self):
		return self.category



class LanguagesBackend(models.Model):
	LANGUAGES_BACKEND =[

	('C','C'),
	('C++','C++'),
	('Java','Java'),
	('Python','Python'),
	('GO','GO'),
	('Ruby', 'Ruby'),
	('Scala','Scala'),
	('JADE','JADE'),
	('Emerald','Emerald'),
	('Visual Basic .NET','Visual Basic .NET'),
	('PHP','PHP'),
	('JavaScript','JavaScript'),
	]

	category = models.CharField(max_length=200, null=True, choices=LANGUAGES_BACKEND)
	# tags = models.ManyToManyField(Tag)

	def __str__(self):
		return self.category

class FrameworkFrontend(models.Model):
	FRAMEWORK_FRONTEND =[

	('HTML','HTML'),
	('CSS','CSS'),
	('JavaScript ','JavaScript '),
	('React','React'),
	('Angular','Angular'),
	('Vue','Vue'),
	('TypeScript ','TypeScript '),
	('Elm','Elm'),
	('jQuery','jQuery'),
	('Swift ','Swift '),

	]

	category = models.CharField(max_length=200, null=True, choices=FRAMEWORK_FRONTEND)
	# tags = models.ManyToManyField(Tag)

	def __str__(self):
		return self.category


class FrameworkBackend(models.Model):
	FRAMEWORKS_BACKEND =[

	('Django','Django'),
	('ExpressJS','ExpressJS'),
	('Laravel','Laravel'),
	('Ruby on Rails','Ruby on Rails'),
	('CakePHP','CakePHP'),
	('Flask','Flask'),
	('ASP .NET Core','ASP .NET Core'),
	('Spring Boot','Spring Boot'),
	('Koa','Koa'),
	('Phoenix','Phoenix'),

	]

	category = models.CharField(max_length=200, null=True, choices=FRAMEWORKS_BACKEND)
	# tags = models.ManyToManyField(Tag)

	def __str__(self):
		return self.category



class Ides(models.Model):
	IDEs =[

	('Visual Studio','Visual Studio'),
	('Visual Studio Code','Visual Studio Code'),
	('AWS Cloud9','AWS Cloud9'),
	('SlickEdit','SlickEdit'),
	('Eclipse Theia','Eclipse Theia'),
	('IntelliJ IDEA','IntelliJ IDEA'),
	('PyCharm','PyCharm'),
	('Xcode','Xcode'),
	('NetBeans','NetBeans'),
	('GNAT Studio','GNAT Studio'),
	('Eclipse','Eclipse'),
	]


	category = models.CharField(max_length=200, null=True, choices=IDEs)
	# tags = models.ManyToManyField(Tag)

	def __str__(self):
		return self.category


class TextEditors(models.Model):
	TEXT_EDITORS=[

	('Visual Studio Code','Visual Studio Code'),
	('Sublime Text','Sublime Text'),
	('Notepad++','Notepad++'),
	('UltraEdit','UltraEdit'),
	]

	category = models.CharField(max_length=200, null=True, choices=TEXT_EDITORS)
	# tags = models.ManyToManyField(Tag)

	def __str__(self):
		return self.category


class CloudComputing(models.Model):
	CLOUD_COMPUTING=[

	('Amazon Web Services (AWS)','Amazon Web Services (AWS)'),
	('Microsoft Azure','Microsoft Azure'),
	('Google Cloud Platform (GCP)','Google Cloud Platform (GCP)'),
	]

	category = models.CharField(max_length=200, null=True, choices=CLOUD_COMPUTING)
	# tags = models.ManyToManyField(Tag)

	def __str__(self):
		return self.category

class WebDevelopment(models.Model):
	WEB_DEVELOPMENT=[

	('API','API'),
	('Chrome Developer Tools','Chrome Developer Tools'),
	('jQuery','jQuery'),
	('GitHub','GitHub'),
	('CodePen','CodePen'),
	('Angular.js','Angular.js'),
	('Sass','Sass'),
	]

	category = models.CharField(max_length=200, null=True, choices=WEB_DEVELOPMENT)
	# tags = models.ManyToManyField(Tag)

	def __str__(self):
		return self.category

class Containers(models.Model):
	CONTAINERS=[

	('Docker','Docker'),
	('AWS Fargate','AWS Fargate'),
	('Google Kubernetes Engine','Google Kubernetes Engine'),
	('Amazon ECS','Amazon ECS'),
	('Linux Containers','Linux Containers'),
	('Microsoft Azure Container Services','Microsoft Azure Container Services'),

	('Database systems', 'Database systems'),
	('Computer networking', 'Computer networking'),
	('Data structures and algorithms', 'Data structures and algorithms'),
	('Computer security', 'Computer security'),
	('Distributed systems', 'Distributed systems'),
	('Software development', 'Software development'),
	('Operating systems', 'Operating systems'),
	('Programming languages', 'Programming languages'),
	('Advanced Computer Architecture', 'Advanced Computer Architecture'),

	]

	category = models.CharField(max_length=200, null=True, choices=CONTAINERS)
	# tags = models.ManyToManyField(Tag)

	def __str__(self):
		return self.category



######################################################################### Education


class Languages(models.Model):
	LANGUGAES = (
	('English', 'English'),
	('German', 'German'),
	('Spanish', 'Spanish'),
	('Chinese', 'Chinese'),
	('Arabic', 'Arabic'),
	('French', 'French'),
	('Turkish', 'Turkish'),
	)

	category = models.CharField(max_length=200, null=True, choices=LANGUGAES)
	# category = models.CharField(max_length=200, null=True)
	# tags = models.ManyToManyField(Tag)

	def __str__(self):
		return self.category



class Education(models.Model):
	EDUCATION = (
	('Secondary', 'Secondary'),
	('Bachelor', 'Bachelor'),
	('MA', 'MA'),
	('MB', 'MB'),
	('MBA', 'MBA'),
	('PhD', 'PhD'),
	
	
	)

	category = models.CharField(max_length=200, null=True, choices=EDUCATION)
	# category = models.CharField(max_length=200, null=True)
	# tags = models.ManyToManyField(Tag)

	def __str__(self):
		return self.category


class ComputerScienceCourses(models.Model):
	COMPUTER_SCIENCE_COURSES = (
	('Algorithms and Data Structures Courses', 'Algorithms and Data Structures Courses'),
	('STEM Courses', 'STEM Courses'),
	('Artificial Intelligence Courses', 'Artificial Intelligence Courses'),
	('Data Science Courses', 'Data Science Courses'),
	('Mathematics Courses', 'Mathematics Courses'),
	('Programming Languages Courses', 'Programming Languages Courses'),
	('Software Development Courses', 'Software Development Courses'),
	('Machine Learning Courses', 'Machine Learning Courses')
	)

	category = models.CharField(max_length=200, null=True, choices=COMPUTER_SCIENCE_COURSES)
	# category = models.CharField(max_length=200, null=True)
	# tags = models.ManyToManyField(Tag)

	def __str__(self):
		return self.category

class InvolvedSDLC(models.Model):
	INVOLVED_SDLC = (
	('Planning Stage', 'Planning Stage'),
	('Requirements of Analysis Stage', 'Requirements of Analysis Stage'),
	('Design and Prototyping Stage', 'Design and Prototyping Stage'),
	('Software Development Stage', 'Software Development Stage'),
	('Software Testing Stage', 'Software Testing Stage'),
	('Implementation and Integration', 'Implementation and Integration'),
	('Operations and Maintenance Stage', 'Operations and Maintenance Stage'),
	)

	category = models.CharField(max_length=200, null=True, choices=INVOLVED_SDLC)
	# category = models.CharField(max_length=200, null=True)
	# tags = models.ManyToManyField(Tag)

	def __str__(self):
		return self.category



class SdlcPhases(models.Model):
	SDLL_PHASES = (
	('_______', '_______'),
	)

	category = models.CharField(max_length=200, null=True, choices=SDLL_PHASES)
	# category = models.CharField(max_length=200, null=True)
	# tags = models.ManyToManyField(Tag)

	def __str__(self):
		return self.category


################################################################################################ EVALUATOR ################################################################################################
#########################################################################################################################################################################################################


class CollaboratingWith(models.Model):
	______ = (
	('hiring managers', 'hiring managers'),
	('hr department', 'hr department'),
	('CTO', 'CTO'),
	('tech leads', 'tech leads'),
	('product managers', 'product managers'),
	('project managers', 'project managers'),
	)

	category = models.CharField(max_length=200, null=True, choices=______)

	def __str__(self):
		return self.category



class AssessingFields(models.Model):
	______ = (
	('assesses algorithms', 'assesses algorithms'),
	('assesses back-end language', 'assesses back-end language'),
	('assesses back end frameworks', 'assesses back end frameworks'),
	('assesses front-end frameworks', 'assesses front-end frameworks'),
	('assesses soft skills ', 'assesses soft skills '),
	)

	category = models.CharField(max_length=200, null=True, choices=______)

	def __str__(self):
		return self.category




class Assisting(models.Model):
	______ = (
	('on-boarding process', 'on-boarding process'),
	('salary negotiations', 'salary negotiations'),
	('updating the assessment(with extra fee) ', 'updating the assessment(with extra fee) '),
	)

	category = models.CharField(max_length=200, null=True, choices=______)

	def __str__(self):
		return self.category





class TechnicalRoles(models.Model):
	______ = (
	('CTO', 'CTO'),
	('software engeneer', 'software engeneer'),
	('data science', 'data science'),
	('ML engeneer', 'ML engeneer'),
	)

	category = models.CharField(max_length=200, null=True, choices=______)

	def __str__(self):
		return self.category



class Experience(models.Model):
	______ = (
	('3-5', '3-5'),
	('5-10', '5-10'),
	('10-15', '10-15'),
	('more than 15', 'more than 15'),
	('________', '________'),
	('________', '________'),
	('________', '________'),
	('________', '________'),
	)

	category = models.CharField(max_length=200, null=True, choices=______)

	def __str__(self):
		return self.category



################################################################################################ COMPANY ################################################################################################
#########################################################################################################################################################################################################


class ProductsAndervices(models.Model):
	______ = (
	('application development', 'application development'),
	('game development', 'game development'),
	('software development analytics tools', 'software development analytics tools'),
	('web frameworks', 'web frameworks'),
	('web designing services', 'web designing services'),
	('help desk it services', 'help desk it services'),
	('virtual desktops', 'virtual desktops'),
	('CRM', 'CRM'),
	('software testing', 'software testing'),
	('test management', 'test management'),
	('network security', 'network security'),
	('data storage and management', 'data storage and management'),
	('data security', 'data security'),
	('data backups', 'data backups'),
	('tech/it support', 'tech/it support'),
	('file servers', 'file servers'),
	('email', 'email'),
	('cloud services', 'cloud services'),
	('PAAS (cloud platform as a service)', 'PAAS (cloud platform as a service)'),
	('IDE  (integrated development environments)', 'IDE  (integrated development environments)'),

	)

	category = models.CharField(max_length=200, null=True, choices=______)

	def __str__(self):
		return self.category



class ProvidedInsuranceTypes(models.Model):
	PROVIDED_INSURANCE_TYPES = (
	('health insurance', 'health insurance'),
	('dental insurance', 'dental insurance'),
	('vision care', 'vision care'),
	('life insurance', 'life insurance'),
	('legal insurance', 'legal insurance'),
	('pet insurance', 'pet insurance'),
	)

	category = models.CharField(max_length=200, null=True, choices=PROVIDED_INSURANCE_TYPES)

	def __str__(self):
		return self.category



class ProvidedVacationTypes(models.Model):
	PROVIDED_VOCATION_TYPES = (
	('paid vacation leave', 'paid vacation leave'),
	('personal leave', 'personal leave'),
	('sick leave ', 'sick leave '),
	('child care', 'child care'),
	('breaks', 'breaks'),
	('flexible schedules', 'flexible schedules'),
	)

	category = models.CharField(max_length=200, null=True, choices=PROVIDED_VOCATION_TYPES)

	def __str__(self):
		return self.category


class ProvidedBenefits(models.Model):
	PROVIDED_BENEFITS = (
	('pay raises ', 'pay raises '),
	('fitness', 'fitness'),
	('free meals', 'free meals'),
	('retirement benefits', 'retirement benefits'),
	('retirement planning services', 'retirement planning services'),
	('college debt relief', 'college debt relief'),
	('use of a company car', 'use of a company car'),
	('pensions and stock options', 'pensions and stock options'),
	('discounts on company products and services; housing', 'discounts on company products and services; housing'),
	('other optional benefits', 'other optional benefits'),
	)

	category = models.CharField(max_length=200, null=True, choices=PROVIDED_BENEFITS)

	def __str__(self):
		return self.category


