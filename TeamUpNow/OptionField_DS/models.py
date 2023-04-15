from django.db import models





################################################################################################ CHOICES


##################################-----> create field | CHOOSE ONE ---->ManyToMany

PROJECT_EXPERICE=[
	('Naive ', 'Naive '),
	('Experienced ', 'Experienced '),
	('Expert ', 'Expert '),
]


SOLVING_APPROACH_SPECIFIC =[
	('Naive ', 'Naive '),
	('Experienced ', 'Experienced '),
	('Expert ', 'Expert '),
]


SOLVING_APPROACH_GENERAL = [
	('Naive ', 'Naive '),
	('Experienced ', 'Experienced '),
	('Expert ', 'Expert '),
]



FOCUS_STYLE = [
	('Naive ', 'Naive '),
	('Experienced ', 'Experienced '),
	('Expert ', 'Expert '),

]


BEHAVIORAL_CHALLENGE = [
	('Naive ', 'Naive '),
	('Experienced ', 'Experienced '),
	('Expert ', 'Expert '),
]




###################################-----> create model as Tags | CHOOSE MULTIPLE




################################################### METHOD INFO OPTION

TASK_TYPE=[
	("General Task","General Task"),
	("Multistage tasks","Multistage tasks"),
]

CHALLANGE_TYPE=[
	("Tech Language","Tech Language"),
	("Tech Framework","Tech Framework"),
]

EVALUATION_DURATION  = [ 
	('1-2 weeks', '1-2 weeks'),
	('2-4 weeks', '2-4 weeks'), 
	('1-2 months', '1-2 months'),
	('2-3 months', '2-3 months'),
	('3-4 months', '3-4 months'),
	('4-5 months', '4-5 months'),
	('5-6 months', '5-6 months'),
	('8-10 months', '8-10 months'),
	('10-12 months', '10-12 months'),
]

	# SDLC_PHASES
SDLC_PHASES = [
	('Planning', 'Planning'),
	('Defining', 'Defining'),
	('Designing', 'Designing'),
	('Building', 'Building'),
	('Testing', 'Testing'),
	('Deployment', 'Deployment'),
]


	# TASK TYPE
EXAMINE_TYPE = [
	('CODING', 'CODING'),
	('ORAL', 'ORAL'),
	('CODING & ORAL', 'CODING & ORAL'),

]

	# TASK METHOD
INTERVIEW_METHOD = [
	('LIVE INTERVIEW', 'LIVE INTERVIEW'),
	('HOME ASSIGNMENT', 'HOME ASSIGNMENT'),
	('LIVE & HOME ASSIGNMENT', 'LIVE & HOME ASSIGNMENT'),

]

	# TASK METHOD
TECHNICAL_TASKS = [
	('Real project of the company', 'Real project of the company'),
	('Simulated project of the company', 'Simulated project of the company'),


]

TASK_COMPLETION = [
	('PAIR PROGRAMMING', 'PAIR PROGRAMMING'),
	('INDIVIDUAL PROGRAMMING', 'INDIVIDUAL PROGRAMMING'),
	
]


	# TASK CHOICE
TASK_CHOICE = [
	('GENERAL TASK', 'GENERAL TASK'),
	('SPECIFIC TASK', 'SPECIFIC TASK'),
]

	# TASK CHOICE
PROJECT_CHOICE = [
	('SPECIFIC PROJECT', 'SPECIFIC PROJECT'),
	('GRENERAL PROJECT', 'GRENERAL PROJECT'),
]


################################################### INDUSTRY & PROJECT TYPES
	# involved_projects

INDUSTRY_AND_PROJECT_TYPES = (
	('Business Projects', 'Business Projects'),
	('Medicine', 'Medicine'),
	('Agriculture Projects', 'Agriculture Projects'),
	('Fintech', 'Fintech'),
	('Blockchain', 'Blockchain'),
	('Crypto Currency', 'Crypto Currency'),
	('Machine Learning', 'Machine Learning'),
	('AI', 'AI'),
	('Business', 'Business'),
	('Analytics', 'Analytics'),
	('ERP', 'ERP'),
	('E-commerce', 'E-commerce'),
	('Agriculture', 'Agriculture'),
	('Data Science', 'Data Science'),
	('Banking', 'Banking'),
)
# INDUSTRY_AND_PROJECT_TYPES = (
# 	('0 Projects', 'Business Projects'),
# 	('1', 'Medicine'),
# 	('2', 'Agriculture Projects'),
# 	('3', 'Fintech'),
# 	('4', 'Blockchain'),
# 	('5', 'Crypto Currency'),
# 	('6', 'Machine Learning'),
# 	('7', 'AI'),
# 	('8', 'Business'),
# 	('9', 'Analytics'),
# 	('10', 'ERP'),
# 	('11', 'E-commerce'),
# 	('12', 'Agriculture'),
# 	('13', 'Data Science'),
# 	('14', 'Banking'),
# )



################################################### DEGREE OPTION

GENERAL_DEGREE_OF_THE_CANDIDATE = [
	('Junior', 'Junior'),
	('Middle', 'Middle'),
	('Senior', 'Senior'),
]


DEGREE_OF_THE_CANDIDATE_TO_THIS_SPECIFIC_PROJECT = [
	('Junior ', 'Junior '),
	('Middle ', 'Middle '),
	('Senior ', 'Senior '),
]



################################################### SKILL SETS OPTION
############## TECH SKILLS

	# DATA_STRUCTURES_AND_AGLORITHMS
DATA_STRUCTURES_AND_AGLORITHMS = [
	('Naive ', 'Naive '),
	('Experienced ', 'Experienced '),
	('Expert ', 'Expert '),
]


	# CODING_QUALITY
CODING_QUALITY = [
	('Naive ', 'Naive '),
	('Experienced ', 'Experienced '),
	('Expert ', 'Expert '),
]

	# DATABASE_AND_SQL_OPTION
DATABASE_AND_SQL_OPTION = [
	('Naive ', 'Naive '),
	('Experienced ', 'Experienced '),
	('Expert ', 'Expert '),
]

	# LANGUAGES_BACKEND_OPTION
LANGUAGES_BACKEND_OPTION = [
	('Naive ', '1 '),
	('Experienced ', '2 '),
	('Expert ', '3 '),
]

	# LANGUAGES_FRONTEND_OPTION
LANGUAGES_FRONTEND_OPTION = [
	('Naive ', 'Naive '),
	('Experienced ', 'Experienced '),
	('Expert ', 'Expert '),
]

	# FRAMEWORK_FRONTEND_OPTION
FRAMEWORK_FRONTEND_OPTION = [
	('Naive ', 'Naive '),
	('Experienced ', 'Experienced '),
	('Expert ', 'Expert '),
]

	# IDEs_OPTION
IDES_OPTION = [
	('Naive ', 'Naive '),
	('Experienced ', 'Experienced '),
	('Expert ', 'Expert '),
]

	# TEXT_EDITORS_OPTION
TEXT_EDITORS_OPTION = [
	('Naive ', 'Naive '),
	('Experienced ', 'Experienced '),
	('Expert ', 'Expert '),
]

	# CLOUD_COMPUTING_OPTION
CLOUD_COMPUTING_OPTION = [
	('Naive ', 'Naive '),
	('Experienced ', 'Experienced '),
	('Expert ', 'Expert '),
]


	# WEB_DEVELOPMENT_OPTION
WEB_DEVELOPMENT_OPTION = [
	('Naive ', 'Naive '),
	('Experienced ', 'Experienced '),
	('Expert ', 'Expert '),
]

	# CONTAINERS_OPTION
CONTAINERS_OPTION = [
	('Naive ', 'Naive '),
	('Experienced ', 'Experienced '),
	('Expert ', 'Expert '),
]


############## SOFT SKILLS

	# LEADERSHIP
LEADERSHIP = [
	('Naive ', 'Naive '),
	('Experienced ', 'Experienced '),
	('Expert ', 'Expert '),
]


	# COMMUNICATIN_SKILLS
COMMUNICATIN_SKILLS = [
	('Naive ', 'Naive '),
	('Experienced ', 'Experienced '),
	('Expert ', 'Expert '),
]



	# TIME_MANAGEMENT
TIME_MANAGEMENT = [
	('Naive ', 'Naive '),
	('Experienced ', 'Experienced '),
	('Expert ', 'Expert '),
]


	# LEARNING_CAPACITY
LEARNING_CAPACITY = [
	('Naive ', 'Naive '),
	('Experienced ', 'Experienced '),
	('Expert ', 'Expert '),
]


	# JOB_PERFORMENCE
JOB_PERFORMENCE = [
	('Naive ', 'Naive '),
	('Experienced ', 'Experienced '),
	('Expert ', 'Expert '),
]


	# TEAMWORK
TEAMWORK = [
	('Naive ', 'Naive '),
	('Experienced ', 'Experienced '),
	('Expert ', 'Expert '),
]






############## TECH SKILLS


DATA_STRUCTURES_ALGORITHMS = [
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
]



DATABASE_AND_SQL=[
('RDMS | MySQL', 'RDMS | MySQL'),
('DBMS | NoSQL', 'DBMS | NoSQL'),
('DBMS | MongoDB', 'DBMS | MongoDB'),
]


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


TEXT_EDITORS=[

('Visual Studio Code','Visual Studio Code'),
('Sublime Text','Sublime Text'),
('Notepad++','Notepad++'),
('UltraEdit','UltraEdit'),
]


CLOUD_COMPUTING=[

('Amazon Web Services (AWS)','Amazon Web Services (AWS)'),
('Microsoft Azure','Microsoft Azure'),
('Google Cloud Platform (GCP)','Google Cloud Platform (GCP)'),
]

WEB_DEVELOPMENT=[

('API','API'),
('Chrome Developer Tools','Chrome Developer Tools'),
('jQuery','jQuery'),
('GitHub','GitHub'),
('CodePen','CodePen'),
('Angular.js','Angular.js'),
('Sass','Sass'),
]

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



################################################### REQUEST
############## COMMENT REQUESTS

	# REQUEST TALENTS
REQUEST_TALENTS = [
	('I request this candidate', 'I request this candidate'),
	('I request a candidate who has the same stack', 'I request a candidate who has the same stack'),

]



##################################-----> new Post | Request Talent

TASK = [
		('Data mining', 'Data mining'),
		('Data Processing', 'Data Processing'),
		('Data Cleaning', 'Data Cleaning'),
		('Create and optimize classifiers', 'Create and optimize classifiers'),
		('Carrying out prepossessing of unstructured data', 'Carrying out prepossessing of unstructured data'),
		('Carrying out prepossessing of structured data', 'Carrying out prepossessing of structured data'),
		('Enhancing data collection procedures', 'Enhancing data collection procedures'),
		('Using ML tools to select features', 'Using ML tools to select features'),
		('Validating the integrity of data to be used for analysis', 'Validating the integrity of data to be used for analysis'),
		('Analyzing big data to find patterns and solutions', 'Analyzing big data to find patterns and solutions'),
		('Analyzing patterns to find solutions', 'Analyzing patterns to find solutions'),
		('Developing prediction systems', 'Developing prediction systems'),
		('Developing machine learning algorithms', 'Developing machine learning algorithms'),
		('Combining various algorithms and modules', 'Combining various algorithms and modules'),
		('Visualizing Data', 'Visualizing Data'),
		('Visualizing Patterns', 'Visualizing Patterns'),
		('Creating comprehensive analytical solutions', 'Creating comprehensive analytical solutions'),
		('Propose ML solutions to tackle challenges', 'Propose ML solutions to tackle challenges'),
		('Constructing data engineering pipelines', 'Constructing data engineering pipelines'), 
		('Architecting data pipelines', 'Architecting data pipelines'), 
		('Implementing data pipelines', 'Implementing data pipelines'), 
		('Monitoring data pipelines' ,'Monitoring data pipelines'), 
		('Working on cost reduction' ,'Working on cost reduction'),
		('Working on effort estimation' ,'Working on effort estimation'),
		('Working on cost optimization' ,'Working on cost optimization'), 
	]


OCCUPATION = [

		('Data Scientist', 'Data Scientist'),
		('Data Analyst' ,'Data Analyst'),
		('Data Engineer','Data Engineer'),
		('ML Engineer', 'ML Engineer'),
		('Machine Learning Scientist' ,'Machine Learning Scientist'),
		('Business Analyst', 'Business Analyst'),
		('Marketing Analyst', 'Marketing Analyst'),
		('Data Architect', 'Data Architect'),
		('Applications Architect', 'Applications Architect'),
		('Enterprise Architect','Enterprise Architect'),
		('Infrastructure Architect', 'Infrastructure Architect'), 
		('Data and Analytics Manager', 'Data and Analytics Manager'),
		('BI Analyst', 'BI Analyst'),
		('BI Developer', 'BI Developer'),
		('Statistician', 'Statistician'),
		('Data Mining Specialist', 'Data Mining Specialist'),
		('Database Administrator', 'Database Administrator'),
		('Database Developer', 'Database Developer'),
	]




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



































