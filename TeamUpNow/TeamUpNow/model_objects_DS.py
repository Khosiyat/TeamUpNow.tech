from django.shortcuts import render, get_object_or_404, redirect
from django.http import HttpResponse, HttpResponseRedirect
from django.template import loader

from django.contrib.auth.models import User, Group


from django.db.models import Q
from django.core.paginator import Paginator


from post_DS.models import Stream_DS, Post_DS,Experience_chart, Tag_DS, Likes_DS, PostFileContent_DS, Follow_DS
from post_DS.forms import NewPostForm_DS, Experience_chart_Form_DS
from stories_employer.models import Story_employer, StoryStream_employer

from comment_DS.models import Comment_DS
from comment_DS.forms import CommentForm_DS

from authy_DS.models import Profile_DS
from authy_DS.forms import EditProfileForm_DS

from notifications_DS.models import Notification_DS
from direct_DS.models import Message_DS



from django.urls import reverse

from statistics import mode, mean


from authy_DS.utils import *
from post_DS.utils import *
from authy_DS.utils import *
from post_DS.decorators import unauthenticated_user, allowed_users,admin_required, dataScientist_only

from direct_DS.forms import MessageSendForm_DS

from skills_TaggingField.models import *



#visualize the data
import pandas as pd
import plotly.figure_factory as ff
from plotly.offline import plot
import plotly.express as px
import numpy as np
import matplotlib.pyplot as plt


from datetime import date, timedelta,datetime

from dateutil import relativedelta








class Profile_Objects_DS:
	def __init__(self, user):
		self.profile = Profile_DS.objects.get(user=user)
		# self.profile_user = Profile_DS.objects.get(user=user)

		# self.user_SELF =request.user.id
		# self.profile_self = Profile_DS.objects.get(user=self.user_SELF)

		self.posts_count = Experience_chart.objects.filter(user=user).count()
		self.posts_count_name = [c.technical_task for c in Experience_chart.objects.filter(user=user)]
		
		self.posts_count_responsible = [c.technical_ocuppation for c in Experience_chart.objects.filter(user=user)]
		self.start_date = [c.start_date for c in Experience_chart.objects.filter(user=user)]
		self.finish_date = [c.finish_date for c in Experience_chart.objects.filter(user=user)]

		self.following_count = Follow_DS.objects.filter(follower=user).count()
		self.followers_count = Follow_DS.objects.filter(following=user).count()


		self.followingAndfollowers_number=[self.following_count, self.followers_count]
		self.followingAndfollowers_names=['following_count', 'followers_count']

		self.responsible_unique_count = len(np.unique([c.technical_ocuppation for c in Experience_chart.objects.filter(user=user)]))
		self.tasks_unique_count = len([c.technical_task for c in Experience_chart.objects.filter(user=user)]) 

		self.posts_value_unique_=[self.responsible_unique_count,self.tasks_unique_count]
		self.posts_names_unique_=['Responsibility','Task']



# class Stream_Objects:
# 	def __init__(self, user, post_id):	
# 		self.posts = Stream_DS.objects.filter(user=user)
# 		self.group_ids = []
# 		for post in self.posts:
# 			self.group_ids.append(post.post_id)
# 		self.post_items = Post_DS.objects.filter(id__in=self.group_ids).all().order_by('-posted')	


			
# 		posts = Stream_DS.objects.filter(user=user)
# 		group_ids = []
# 		for post in posts:
# 			group_ids.append(post.post_id)
# 		post_items = Post_DS.objects.filter(id__in=group_ids).all().order_by('-posted')	






		
		
		
	# def show_student(self, request, user):
	# 	self.follow_status = Follow_DS.objects.filter(following=user, follower=request.user).exists()






class Profile_activityCalculations_DS(Profile_Objects_DS):
	def __init__(self, user):
	########################### profile activity calculations ###########################
		#activity log
		# self.expreriencePost_notifications_count=Experience_chart.objects.filter(user=user).count()	
		self.all_OR_follower_post=Experience_chart.objects.filter(posted__lt=datetime.today()).count()
		self.all_OR_follower_post_evaluation=Stream_DS.objects.filter(user=user).count()
		self.expreriencePost_yourPost_count=Post_DS.objects.filter(user=user).count()	

			

		self.notifications_count = Notification_DS.objects.filter(user=user, notification_type=2).count()	


		self.follow_status = Follow_DS.objects.filter(following=user, follower=user).exists()
		self.follow_notifications_count = Follow_DS.objects.filter(following=user).count()
		#logic to prevent matplotlib error. 1 does not change followers' quantity, but just avoids error
		if self.follow_notifications_count==0:
			self.follow_notifications_count=1
		###############

		self.comment_notifications_count=Notification_DS.objects.filter(user=user, notification_type=2).count()	
		self.like_notifications_count=Notification_DS.objects.filter(user=user, notification_type=1).count()
		self.expreriencePost_notifications_count=Experience_chart.objects.filter(user=user).count()
		#logic to prevent matplotlib error. 1 does not change followers' quantity, but just avoids error
		if self.expreriencePost_notifications_count==0:
			self.expreriencePost_notifications_count=1
		###############


		self.message_notifications_count=Message_DS.objects.filter(user=user).count()	


		self.notifications = Notification_DS.objects.filter(user=user).order_by('-date')
		Notification_DS.objects.filter(user=user, is_seen=False).update(is_seen=True)
	







 
class Profile_Illustrations_DS(Profile_Objects_DS):
	def __init__(self, user):
		
		self.post_objects_get=Profile_Objects_DS(user=user)

		self.followingAndfollowers=get_bar_chart_profileDashboard_interaction(self.post_objects_get.followingAndfollowers_names, self.post_objects_get.followingAndfollowers_number)

		self.sum_of_Experience_unique_count=get_pie_profileDashboard_projects(self.post_objects_get.posts_value_unique_, self.post_objects_get.posts_names_unique_)



			
		profile_activityCalculations = Profile_activityCalculations_DS(user=user)

		# activity log
		self.x_data_all_notification=[
						profile_activityCalculations.follow_notifications_count, 
						profile_activityCalculations.comment_notifications_count, 
						profile_activityCalculations.like_notifications_count, 
						profile_activityCalculations.expreriencePost_notifications_count, 
						profile_activityCalculations.message_notifications_count,
						]
		self.y_label_all_notification =['teamedUp',  
									'Requests',
									'Scores', 
									"Your Experience", 
									"Interview Arrengements",]
		
		self.bubblePlot=get_bubblePlot(self.x_data_all_notification, self.y_label_all_notification)


		#arranged & requested
		self.x_data_arranged_and_requestes=[profile_activityCalculations.comment_notifications_count, profile_activityCalculations.message_notifications_count]
		self.y_label_arranged_and_requestes=['requested', 'arranged']
		self.arranged_and_requestes=get_bar_chart_postDashboard_quality(self.y_label_arranged_and_requestes, self.x_data_arranged_and_requestes)

		



		# scored and teamed up
		self.x_data_teamedUp_and_scored=[profile_activityCalculations.follow_notifications_count,profile_activityCalculations.like_notifications_count]
		self.y_label_teamedUp_and_scored=['TeamedUp','Scored']

		self.teamedUp_and_scored=get_pie_postDashboard_projects(self.x_data_teamedUp_and_scored, self.y_label_teamedUp_and_scored)





class Profile_dateCalculations_DS(Profile_Objects_DS):
	def __init__(self, user):
		
		self.post_objects_get=Profile_Objects_DS(user=user)
		########################### profile date calculations ###########################
		
		self.data = {'date_col_1': self.post_objects_get.start_date,
	
					'date_col_2': self.post_objects_get.finish_date}
	
		self.worked_dates_allProjects= pd.DataFrame(self.data)



		self.worked_dates_months = self.worked_dates_allProjects.apply(lambda row: abs(relativedelta.relativedelta(row['date_col_2'],
																row['date_col_1']).months), 
																axis=1)

		self.worked_dates_years= self.worked_dates_allProjects.apply(lambda row: abs(relativedelta.relativedelta(row['date_col_2'],
																row['date_col_1']).years), 
																axis=1)

		self.worked_dates_allProjects = self.worked_dates_months + (self.worked_dates_years * 12)


		


		# self.worked_dates_allProjects = pd.DataFrame({'worked_dates_allProjects': self.worked_dates_allProjects,
		# 			'name_project': self.post_objects_get.posts_count_name})


		self.worked_dates_allProjects = pd.DataFrame({'worked_dates_allProjects': self.worked_dates_allProjects,
					'name_project': self.post_objects_get.posts_count_name})



		####################################  MONTHS  ####################################


		self.calculated_totalMonths=self.worked_dates_years*12 + self.worked_dates_months
		self.worked_months_sum= sum(self.calculated_totalMonths)


		####################################  YEARS  ####################################


		self.calculated_totalYearsSum=self.calculated_totalMonths//12
		self.worked_years_sum= sum(self.calculated_totalYearsSum)

		
		####################################  DAYS  ####################################

		self.calculated_totalDays=self.calculated_totalMonths*22
		self.worked_days_sum= sum(self.calculated_totalDays)
		
		
		self.calculated_totalYears=self.worked_dates_years+0.5

		######################### BIOGRAPHY DATA #########################

		self.worked_sinceFirstYear=min(self.post_objects_get.start_date)

		self.tasks_count_name = pd.DataFrame({'name_project': self.post_objects_get.posts_count_name})
		self.responsibility_count_responsible = pd.DataFrame({'name_project': self.post_objects_get.posts_count_responsible})
		

		self.tasks_unique_name=np.unique(self.tasks_count_name)
		self.responsibility_unique_responsible=np.unique(self.responsibility_count_responsible)






class Profile_ProjectsIllustrations_DS(Profile_dateCalculations_DS):
	def __init__(self, user):
		
		self.post_objects_get=Profile_Objects_DS(user=user)
		self.profile_dateCalculations = Profile_dateCalculations_DS(user=user)



		

		self.worked_dates_allProjects_date_difference = self.profile_dateCalculations.worked_dates_allProjects['worked_dates_allProjects']
		self.worked_dates_allProjects_name_project = self.profile_dateCalculations.worked_dates_allProjects['name_project']

		self.worked_months_allProjects=get_pie(self.worked_dates_allProjects_date_difference, self.worked_dates_allProjects_name_project)

		

		self.worked_days_allProjects=get_pie(self.profile_dateCalculations.calculated_totalDays, self.worked_dates_allProjects_name_project)
		

		self.worked_years_allProjects=get_pie(self.profile_dateCalculations.calculated_totalYears, self.worked_dates_allProjects_name_project)



			
		
		self.qs = Experience_chart.objects.filter(user=user)
		self.projects_data = [
			{
				'Project': x.technical_task,
				'Start': x.start_date,
				'Finish': x.finish_date,
				'Responsible': x.technical_ocuppation
			} for x in self.qs
		]

		self.df = pd.DataFrame(self.projects_data)
		
		
		self.fig = px.timeline(
							self.df, x_start="Start", 
							x_end="Finish", 
							y="Responsible", 
							color="Responsible", 
							text='Project', 
							height=300, 
							width=1100, 
							# pattern_shape="Project",
							# pattern_shape_sequence=[".", ".", "."],
							# pattern_shape_sequence=False,

							#colors
							# color_discrete_sequence=px.colors.qualitative.Set3,
							# color_discrete_sequence=px.colors.qualitative.Pastel2, #LIGH CHOICE

							# color_discrete_sequence=px.colors.qualitative.Pastel1,
							# color_discrete_sequence=px.colors.qualitative.Pastel,

							# color_discrete_sequence=px.colors.qualitative.Set2,
							color_discrete_sequence=px.colors.qualitative.T10,  #DARK CHOICE

							)

		self.fig.update_layout({
		'plot_bgcolor': 'rgba(0,0,0,0)',
		'paper_bgcolor': 'rgba(0,0,0,0)'
		})
		# fig = ff.create_gantt(df)
		self.fig.update_yaxes(autorange="reversed")
		self.gantt_plot = plot(self.fig, output_type="div")




class Profile_Display_contextList_DS(Profile_ProjectsIllustrations_DS):
	def __init__(self, request, username):

		self.user = get_object_or_404(User, username=username)

			
		self.posts_stream = Stream_DS.objects.filter(user=self.user)

		self.group_ids = []

		for post in self.posts_stream:
			self.group_ids.append(post.post_id)
			
		self.post_items = Post_DS.objects.filter(id__in=self.group_ids).all().order_by('-posted')	

		self.post_items_experience_chart = Experience_chart.objects.filter(user=self.user)
		
		#logic to prevent matplotlib error. 1 does not change followers' quantity, but just avoids error
		if self.post_items_experience_chart==0:
			self.post_items_experience_chart=1
		###############


		self.posts = Post_DS.objects.filter(user=self.user).order_by('-posted')

			
	######### display
		self.posts = Post_DS.objects.filter(user=self.user).order_by('-posted')

		post_objects_get=Profile_Objects_DS(user=self.user)

		self.user_SELF =request.user.id
		self.profile_self = Profile_DS.objects.get(user=self.user_SELF)
		self.notifications_self = Notification_DS.objects.filter(user=self.user_SELF).order_by('-date')
		self.posts_self  = Post_DS.objects.filter(user=self.user_SELF).order_by('-posted')

		

		profile_dateCalculations = Profile_dateCalculations_DS(user=self.user)
		profile_activityCalculations = Profile_activityCalculations_DS(user=self.user)
		profile_Illustrations = Profile_Illustrations_DS(user=self.user)
		profile_ProjectsIllustrations = Profile_ProjectsIllustrations_DS(user=self.user)



		self.context = {
			
			# 'post':post,
			'posts': self.posts,
			'posts_self': self.posts_self,
			'post_items': self.post_items,

			#perofile illustrations
			'plot_div': profile_ProjectsIllustrations.gantt_plot,

			'worked_months_allProjects':profile_ProjectsIllustrations.worked_months_allProjects,
			
			'worked_days_allProjects':profile_ProjectsIllustrations.worked_days_allProjects,
			'worked_years_allProjects':profile_ProjectsIllustrations.worked_years_allProjects,

			'post_items_experience_chart':self.post_items_experience_chart,
			'posts_count_name':post_objects_get.posts_count_name,
			'posts_count_responsible':post_objects_get.posts_count_responsible,

			'followingAndfollowers':profile_Illustrations.followingAndfollowers,

			#profile
			'profile':post_objects_get.profile,
			'profile_self':self.profile_self,

			'following_count':post_objects_get.following_count,
			'followers_count':post_objects_get.followers_count,
			'posts_count':post_objects_get.posts_count,

			'follow_status':profile_activityCalculations.follow_status,

			# activity log dashboard
			"expreriencePost_notifications_count":profile_activityCalculations.expreriencePost_notifications_count,
			"all_OR_follower_post":profile_activityCalculations.all_OR_follower_post,
			'all_OR_follower_post_evaluation':profile_activityCalculations.all_OR_follower_post_evaluation,
			'expreriencePost_yourPost_count':profile_activityCalculations.expreriencePost_yourPost_count,

			'followingAndfollowers':profile_Illustrations.followingAndfollowers,
			'sum_of_Experience_unique_count':profile_Illustrations.sum_of_Experience_unique_count,

			# notifications
			'notifications': profile_activityCalculations.notifications,
			'notifications_self': self.notifications_self,

			# Experience Log
			'worked_days_sum':profile_dateCalculations.worked_days_sum,
			'responsibility_unique_responsible':profile_dateCalculations.responsibility_unique_responsible,
			'worked_sinceFirstYear':profile_dateCalculations.worked_sinceFirstYear,
			'tasks_unique_name':profile_dateCalculations.tasks_unique_name,
			'worked_months_sum':profile_dateCalculations.worked_months_sum,

			# Date/Experience Calculation
			'calculated_totalDays':profile_dateCalculations.calculated_totalDays,
			'worked_years_sum':profile_dateCalculations.worked_years_sum,
			
		}



class EditProfile_objects_DS():
	def __init__(self, request):
		self.user = request.user.id
		self.profile = Profile_DS.objects.get(user__id=self.user)


		if request.method == 'POST':
			self.form = EditProfileForm_DS(request.POST, request.FILES)
			if self.form.is_valid():
				self.profile.picture = self.form.cleaned_data.get('picture')
				self.profile.first_name = self.form.cleaned_data.get('first_name')
				self.profile.last_name = self.form.cleaned_data.get('last_name')

				self.profile.industry_and_projects = self.form.cleaned_data.get('industry_and_projects')
				self.profile.location = self.form.cleaned_data.get('location')
				self.profile.telephone = self.form.cleaned_data.get('telephone')
				self.profile.kaggle = self.form.cleaned_data.get('kaggle')
				self.profile.github = self.form.cleaned_data.get('github')
				self.profile.linkedInn = self.form.cleaned_data.get('linkedInn')
				self.profile.previous_CTO_linkedInn_link = self.form.cleaned_data.get('previous_CTO_linkedInn_link')
				self.profile.previous_HRmanager_linkedInn_link = self.form.cleaned_data.get('previous_HRmanager_linkedInn_link')
				
				self.profile.save()
				# return redirect('index_DS')
		else:
			self.form = EditProfileForm_DS()


	######### display
		posts = Post_DS.objects.filter(user=self.user).order_by('-posted')

		post_objects_get=Profile_Objects_DS(user=self.user)

		profile_dateCalculations = Profile_dateCalculations_DS(user=self.user)
		profile_activityCalculations = Profile_activityCalculations_DS(user=self.user)
		profile_Illustrations = Profile_Illustrations_DS(user=self.user)
		profile_ProjectsIllustrations = Profile_ProjectsIllustrations_DS(user=self.user)
		


		self.context = {
			#form
			'form':self.form,

			# 'post':post,
			'posts': posts,

			#perofile illustrations
			'plot_div': profile_ProjectsIllustrations.gantt_plot,

			'worked_months_allProjects':profile_ProjectsIllustrations.worked_months_allProjects,
			
			'worked_days_allProjects':profile_ProjectsIllustrations.worked_days_allProjects,
			'worked_years_allProjects':profile_ProjectsIllustrations.worked_years_allProjects,
			
			'posts_count_name':post_objects_get.posts_count_name,
			'posts_count_responsible':post_objects_get.posts_count_responsible,

			'followingAndfollowers':profile_Illustrations.followingAndfollowers,

			#profile
			'profile':post_objects_get.profile,

			'following_count':post_objects_get.following_count,
			'followers_count':post_objects_get.followers_count,
			'posts_count':post_objects_get.posts_count,

			'follow_status':profile_activityCalculations.follow_status,

			# activity log dashboard
			"expreriencePost_notifications_count":profile_activityCalculations.expreriencePost_notifications_count,
			"all_OR_follower_post":profile_activityCalculations.all_OR_follower_post,
			'all_OR_follower_post_evaluation':profile_activityCalculations.all_OR_follower_post_evaluation,
			'expreriencePost_yourPost_count':profile_activityCalculations.expreriencePost_yourPost_count,

			'followingAndfollowers':profile_Illustrations.followingAndfollowers,
			'sum_of_Experience_unique_count':profile_Illustrations.sum_of_Experience_unique_count,

			# notifications
			'notifications': profile_activityCalculations.notifications,

			# Experience Log
			'worked_days_sum':profile_dateCalculations.worked_days_sum,
			'responsibility_unique_responsible':profile_dateCalculations.responsibility_unique_responsible,
			'worked_sinceFirstYear':profile_dateCalculations.worked_sinceFirstYear,
			'tasks_unique_name':profile_dateCalculations.tasks_unique_name,
			'worked_months_sum':profile_dateCalculations.worked_months_sum,

			# Date/Experience Calculation
			'calculated_totalDays':profile_dateCalculations.calculated_totalDays,
			'worked_years_sum':profile_dateCalculations.worked_years_sum,

		}
		

class Post_Objects_DS(Profile_Objects_DS):
	def __init__(self, request, post_id):
	##### scores
		############ CODE QUALITY
		post_objects = Post_DS.objects.get(id=post_id) 
		self.clean_SCORE = post_objects.clean_SCORE
		self.refactored_SCORE  = post_objects.refactored_SCORE
		self.well_documented_SCORE  = post_objects.well_documented_SCORE
		self.unit_tested_SCORE  = post_objects.unit_tested_SCORE
		self.debuged_SCORE  = post_objects.debuged_SCORE
		self.debuged_with_other_team_members_SCORE = post_objects.debuged_with_other_team_members_SCORE
		self.debuged_other_team_members_bugs_SCORE  = post_objects.debuged_other_team_members_bugs_SCORE

		############ PROCESS QUALITY

		self.analyzed_SCORE  = post_objects.analyzed_SCORE
		self.analyzed_with_other_team_members_SCORE = post_objects.analyzed_with_other_team_members_SCORE
		self.analyzed_other_team_members_script_SCORE  = post_objects.analyzed_other_team_members_script_SCORE
		self.discussed_SCORE = post_objects.discussed_SCORE
		self.discussed_with_other_team_members_SCORE = post_objects.discussed_with_other_team_members_SCORE
		self.expected_problems_are_reasoned_SCORE  = post_objects.expected_problems_are_reasoned_SCORE
		self.arbitrary_problems_are_reasoned_SCORE  = post_objects.arbitrary_problems_are_reasoned_SCORE
		self.expected_constraints_are_reasoned_SCORE  = post_objects.expected_constraints_are_reasoned_SCORE
		self.arbitrary_constraints_are_reasoned_SCORE  = post_objects.arbitrary_constraints_are_reasoned_SCORE
		self.designed_with_one_approach_SCORE  = post_objects.designed_with_one_approach_SCORE
		self.designed_with_multiple_possible_approaches_SCORE  = post_objects.designed_with_multiple_possible_approaches_SCORE

	##### note of the scores
		############ SCORES
		self.clean_NOTE = post_objects.clean_NOTE
		self.refactored_NOTE = post_objects.refactored_NOTE
		self.well_documented_NOTE = post_objects.well_documented_NOTE
		self.unit_tested_NOTE = post_objects.unit_tested_NOTE
		self.debuged_NOTE = post_objects.debuged_NOTE
		self.debuged_with_other_team_members_NOTE = post_objects.debuged_with_other_team_members_NOTE
		self.debuged_other_team_members_bugs_NOTE = post_objects.debuged_other_team_members_bugs_NOTE
		##########PROCESS QUALITY
		self.analyzed_NOTE = post_objects.analyzed_NOTE
		self.analyzed_with_other_team_members_NOTE = post_objects.analyzed_with_other_team_members_NOTE
		self.analyzed_other_team_members_script_NOTE = post_objects.analyzed_other_team_members_script_NOTE
		self.discussed_NOTE = post_objects.discussed_NOTE
		self.discussed_with_other_team_members_NOTE = post_objects.discussed_with_other_team_members_NOTE
		self.expected_problems_are_reasoned_NOTE = post_objects.expected_problems_are_reasoned_NOTE
		self.arbitrary_problems_are_reasoned_NOTE = post_objects.arbitrary_problems_are_reasoned_NOTE
		self.expected_constraints_are_reasoned_NOTE = post_objects.expected_constraints_are_reasoned_NOTE
		self.arbitrary_constraints_are_reasoned_NOTE = post_objects.arbitrary_constraints_are_reasoned_NOTE
		self.designed_with_one_approach_NOTE = post_objects.designed_with_one_approach_NOTE
		self.designed_with_multiple_possible_approaches_NOTE = post_objects.designed_with_multiple_possible_approaches_NOTE

	##############################################################################################################################################
	



class Post_Objects_SkillsCalculations_DS(Profile_Objects_DS):
	def __init__(self, request, post_id):
		
		post_objects=Post_Objects_DS(request,post_id)
		# p=post_objects.clean_SCORE
		########### CHART functions
			#######################################---------->>> Skills PIE
		
		#leadership_SKILL
		self.leadership_SKILL = [post_objects.debuged_other_team_members_bugs_SCORE + post_objects.analyzed_other_team_members_script_SCORE + (post_objects.debuged_other_team_members_bugs_SCORE + post_objects.analyzed_other_team_members_script_SCORE//2)]
		# working_with_team_members_SKILL
		self.working_with_team_members_SKILL = [post_objects.debuged_with_other_team_members_SCORE + post_objects.analyzed_with_other_team_members_SCORE + post_objects.discussed_with_other_team_members_SCORE]
		# communication_SKILL
		self.communication_SKILL= [post_objects.expected_constraints_are_reasoned_SCORE + post_objects.expected_problems_are_reasoned_SCORE + (post_objects.discussed_with_other_team_members_SCORE + post_objects.debuged_with_other_team_members_SCORE)//2]
		# problemSolving_SKILL
		self.designed_with_one_approach_SCORE=post_objects.designed_with_one_approach_SCORE//2
		self.problemSolving_SKILL= [post_objects.designed_with_multiple_possible_approaches_SCORE + post_objects.arbitrary_constraints_are_reasoned_SCORE + post_objects.arbitrary_problems_are_reasoned_SCORE + post_objects.designed_with_one_approach_SCORE]
		# code_quality
		self.restOfThe_code_quality_SCORE=(post_objects.clean_SCORE + post_objects.refactored_SCORE + post_objects.debuged_SCORE + post_objects.analyzed_SCORE + post_objects.discussed_SCORE)*2
		self.well_documented_SCORE=(post_objects.well_documented_SCORE*4)
		self.unit_tested_SCORE=(post_objects.unit_tested_SCORE*4)
		self.code_quality= [post_objects.unit_tested_SCORE + post_objects.well_documented_SCORE + self.restOfThe_code_quality_SCORE]
		#Average of all Skills
		self.leadership_SKILL=round(mean(self.leadership_SKILL))
		self.working_with_team_members_SKILL=round(mean(self.working_with_team_members_SKILL))
		self.communication_SKILL=round(mean(self.communication_SKILL))
		self.problemSolving_SKILL=round(mean(self.problemSolving_SKILL))
		self.code_quality = round(mean(self.code_quality))



class Post_Objects_SkillsIllustrations_DS(Post_Objects_SkillsCalculations_DS):
	def __init__(self, request, post_id):
		
		post_objects=Post_Objects_SkillsCalculations_DS(request,post_id)

		self.x_data_all_skills=[
						post_objects.leadership_SKILL, 
						post_objects.working_with_team_members_SKILL, 
						post_objects.problemSolving_SKILL, 
						post_objects.communication_SKILL, 
						post_objects.code_quality
						]
						
		self.y_label_all_skills ='leadership', 'team work',  'problemSolving', 'communication', "code quality"

		self.skills_avgScore_dashboard = get_pie_postDashboard_projects(self.x_data_all_skills, self.y_label_all_skills)
		self.skills_avgScore = get_pie_post_projects(self.x_data_all_skills, self.y_label_all_skills)

		self.bubblePlot=get_bubblePlot(self.x_data_all_skills, self.y_label_all_skills)



			#######################################---------->>> Skills BAR

		post_objects_get=Post_Objects_DS(request,post_id)

		#CODE QUALITY
		self.x_code_quality = [post_objects_get.clean_SCORE, 
		post_objects_get.refactored_SCORE, 
		post_objects_get.well_documented_SCORE,
		post_objects_get.unit_tested_SCORE,
		post_objects_get.debuged_SCORE,
		post_objects_get.analyzed_SCORE, 
		post_objects_get.discussed_SCORE,
		]

		self.y_code_quality = ['clean',
		'refactored',
		'well documented',
		'unit tested',
		'debuged',
		'analyzed',
		'discussed',
		]


		########################## SOFT SKILLS
		#COMMUNICATION
		self.x_communication_skills = [post_objects_get.expected_problems_are_reasoned_SCORE,
		post_objects_get.expected_constraints_are_reasoned_SCORE,
		post_objects_get.discussed_with_other_team_members_SCORE,
		]

		self.y_communication_skills = ['expected problems are reasoned',
		'expected constraints are reasoned',
		'discussed with other team members',
		]
		#TEAM WORK SKILLS
		self.x_team_work_skills = [post_objects_get.debuged_with_other_team_members_SCORE,
		post_objects_get.analyzed_with_other_team_members_SCORE
		]

		self.y_team_work_skills = ['debuged with other team members',
		'analyzed with other team members',
		]
		#LEADERSHIP SKILLS
		self.x_leadership_skills = [post_objects_get.debuged_other_team_members_bugs_SCORE,
		post_objects_get.analyzed_other_team_members_script_SCORE
		]

		self.y_leadership_skills = ['debuged other team members bugs',
		'analyzed other team members script',
		]

		#PROBLEM SOLVING
		self.x_problem_solving_skills = [post_objects_get.arbitrary_problems_are_reasoned_SCORE,
		post_objects_get.arbitrary_constraints_are_reasoned_SCORE,
		post_objects_get.designed_with_one_approach_SCORE,
		post_objects_get.designed_with_multiple_possible_approaches_SCORE,
		]

		self.y_problem_solving_skills = ['arbitrary problems are reasoned',
		'arbitrary constraints are reasoned',
		'designed with one approach SCORE',
		'designed with multiple possible approaches',
		]

		self.barChart_code_quality=get_code_quality(self.y_code_quality, self.x_code_quality)
		self.barChart_problem_solving_skills=get_problem_solving_skills(self.y_problem_solving_skills, self.x_problem_solving_skills)
		self.barChart_communication_skills=get_communication_skills(self.y_communication_skills, self.x_communication_skills)
		self.barChart_team_work_skills=get_team_work_skills(self.y_team_work_skills, self.x_team_work_skills)
		self.barChart_leadership_skills=get_leadership_skills(self.y_leadership_skills, self.x_leadership_skills)




	############ evaluation quality
		post_objects_get = Post_DS.objects.get(id=post_id) 
		self.conciseness = post_objects_get.conciseness
		self.relevancy = post_objects_get.relevancy
		
		self.concisenessnumber=[post_objects_get.conciseness, post_objects_get.relevancy]
		self.relevancy_names=['conciseness', 'relevancy']
		self.sum_of_post_quality=get_bar_chart_postDashboard_quality(self.relevancy_names, self.concisenessnumber)





class Post_Display_DS(Post_Objects_SkillsIllustrations_DS):
	def __init__(self, request, post_id):

		self.post = get_object_or_404(Post_DS, id=post_id)
		self.favorited = False
		self.user = request.user

			#comment
		self.comments = Comment_DS.objects.filter(post=self.post).order_by('date')
		
		if request.user.is_authenticated:
			self.profile = Profile_DS.objects.get(user=self.user)

			if self.profile.favorites.filter(id=post_id).exists():
				self.favorited = True



class Post_Display_contextList_DS(Post_Objects_SkillsIllustrations_DS):
	def __init__(self, request, post_id):

		post_objects_get = Post_DS.objects.get(id=post_id) 
		post_objects_SkillsIllustrations=Post_Objects_SkillsIllustrations_DS(request,post_id)
		post_objects_dislay=Post_Display_DS(request,post_id)

		self.context = {
		
		'post':post_objects_dislay.post,
		'favorited':post_objects_dislay.favorited,
		'profile':post_objects_dislay.profile,
		'comments':post_objects_dislay.comments,


########################################################## score

		'barChart_code_quality': post_objects_SkillsIllustrations.barChart_code_quality,
		'barChart_communication_skills':post_objects_SkillsIllustrations.barChart_communication_skills,
		'barChart_team_work_skills':post_objects_SkillsIllustrations.barChart_team_work_skills,
		'barChart_leadership_skills':post_objects_SkillsIllustrations.barChart_leadership_skills, 
		'barChart_problem_solving_skills':post_objects_SkillsIllustrations.barChart_problem_solving_skills,

		'skills_avgScore':post_objects_SkillsIllustrations.skills_avgScore,
		'skills_avgScore_dashboard':post_objects_SkillsIllustrations.skills_avgScore_dashboard,
		'sum_of_post_quality':post_objects_SkillsIllustrations.sum_of_post_quality,

		'bubblePlot':post_objects_SkillsIllustrations.bubblePlot,

########################################################## note

	############PROCESS QUALITY

		# analyzed_SCORE
		# analyzed_with_other_team_members_SCORE
		# analyzed_other_team_members_script_SCORE
		# discussed_SCORE
		# discussed_with_other_team_members_SCORE
		# expected_problems_are_reasoned_SCORE
		# arbitrary_problems_are_reasoned_SCORE
		# expected_constraints_are_reasoned_SCORE
		# arbitrary_constraints_are_reasoned_SCORE
		# designed_with_one_approach_SCORE
		# designed_with_multiple_possible_approaches_SCORE

		#PROCESS QUALITY _SCORE
		'clean_NOTE':post_objects_get.clean_NOTE,
		'refactored_NOTE':post_objects_get.refactored_NOTE,
		'well_documented_NOTE':post_objects_get.well_documented_NOTE,
		'unit_tested_NOTE':post_objects_get.unit_tested_NOTE,
		'debuged_NOTE':post_objects_get.debuged_NOTE,
		'debuged_with_other_team_members_NOTE':post_objects_get.debuged_with_other_team_members_NOTE,
		'debuged_other_team_members_bugs_NOTE':post_objects_get.debuged_other_team_members_bugs_NOTE,
		#PROCESS QUALITY _NOTE
		'analyzed_NOTE':post_objects_get.analyzed_NOTE,
		'analyzed_with_other_team_members_NOTE':post_objects_get.analyzed_with_other_team_members_NOTE,
		'analyzed_other_team_members_script_NOTE':post_objects_get.analyzed_other_team_members_script_NOTE,
		'discussed_NOTE':post_objects_get.discussed_NOTE,
		'discussed_with_other_team_members_NOTE':post_objects_get.discussed_with_other_team_members_NOTE,
		'expected_problems_are_reasoned_NOTE':post_objects_get.expected_problems_are_reasoned_NOTE,
		'arbitrary_problems_are_reasoned_NOTE':post_objects_get.arbitrary_problems_are_reasoned_NOTE,
		'expected_constraints_are_reasoned_NOTE':post_objects_get.expected_constraints_are_reasoned_NOTE,
		'arbitrary_constraints_are_reasoned_NOTE':post_objects_get.arbitrary_constraints_are_reasoned_NOTE,
		'designed_with_one_approach_NOTE':post_objects_get.designed_with_one_approach_NOTE,
		'designed_with_multiple_possible_approaches_NOTE':post_objects_get.designed_with_multiple_possible_approaches_NOTE,

	}






# class Post_EditPost_DS(Post_Objects_SkillsIllustrations_DS):
# 	def __init__(self, request, event_id):

# 		self.user = request.user
# 		self.post_item = Post_DS.objects.get(pk=event_id)
		
# 		if request.method == 'POST':
# 			self.form_EditPost = NewPostForm_DS(request.POST)

# 			if self.form_EditPost.is_valid():
				
# 		# # #METHOD TYPES
# 				self.post_item.attendees_evaluated = self.form_EditPost.cleaned_data.get('attendees_evaluated')
# 				self.post_item.task_choice = self.form_EditPost.cleaned_data.get('task_choice')
# 				self.post_item.project_choice = self.form_EditPost.cleaned_data.get('project_choice')
# 				self.post_item.examine_types = self.form_EditPost.cleaned_data.get('examine_types')
# 				self.post_item.task_method = self.form_EditPost.cleaned_data.get('task_method')
# 				self.post_item.task_completion = self.form_EditPost.cleaned_data.get('task_completion')
# 				self.post_item.sdls_phase = self.form_EditPost.cleaned_data.get('sdls_phase')
# 				self.post_item.evaluation_duration = self.form_EditPost.cleaned_data.get('evaluation_duration')

# 		# #CODE QUALITY
# 				self.post_item.clean_SCORE = self.form_EditPost.cleaned_data.get('clean_SCORE')
# 				self.post_item.clean_NOTE = self.form_EditPost.cleaned_data.get('clean_NOTE')
# 				self.post_item.refactored_SCORE = self.form_EditPost.cleaned_data.get('refactored_SCORE')
# 				self.post_item.refactored_NOTE = self.form_EditPost.cleaned_data.get('refactored_NOTE')
# 				self.post_item.well_documented_SCORE = self.form_EditPost.cleaned_data.get('well_documented_SCORE')
# 				self.post_item.well_documented_NOTE = self.form_EditPost.cleaned_data.get('well_documented_NOTE')
# 				self.post_item.unit_tested_SCORE = self.form_EditPost.cleaned_data.get('unit_tested_SCORE')
# 				self.post_item.unit_tested_NOTE = self.form_EditPost.cleaned_data.get('unit_tested_NOTE')
# 				self.post_item.debuged_SCORE = self.form_EditPost.cleaned_data.get('debuged_SCORE')
# 				self.post_item.debuged_NOTE = self.form_EditPost.cleaned_data.get('debuged_NOTE')
# 				self.post_item.debuged_with_other_team_members_SCORE = self.form_EditPost.cleaned_data.get('debuged_with_other_team_members_SCORE')
# 				self.post_item.debuged_with_other_team_members_NOTE = self.form_EditPost.cleaned_data.get('debuged_with_other_team_members_NOTE')
# 				self.post_item.debuged_other_team_members_bugs_SCORE = self.form_EditPost.cleaned_data.get('debuged_other_team_members_bugs_SCORE')
# 				self.post_item.debuged_other_team_members_bugs_NOTE = self.form_EditPost.cleaned_data.get('debuged_other_team_members_bugs_NOTE')

# 		# #PROCESS QUALITY
# 				self.post_item.analyzed_SCORE = self.form_EditPost.cleaned_data.get('analyzed_SCORE')
# 				self.post_item.analyzed_NOTE = self.form_EditPost.cleaned_data.get('analyzed_NOTE')
# 				self.post_item.analyzed_with_other_team_members_SCORE = self.form_EditPost.cleaned_data.get('analyzed_with_other_team_members_SCORE')
# 				self.post_item.analyzed_with_other_team_members_NOTE = self.form_EditPost.cleaned_data.get('analyzed_with_other_team_members_NOTE')
# 				self.post_item.analyzed_other_team_members_script_SCORE = self.form_EditPost.cleaned_data.get('analyzed_other_team_members_script_SCORE')
# 				self.post_item.analyzed_other_team_members_script_NOTE = self.form_EditPost.cleaned_data.get('analyzed_other_team_members_script_NOTE')
# 				self.post_item.discussed_SCORE = self.form_EditPost.cleaned_data.get('discussed_SCORE')
# 				self.post_item.discussed_NOTE = self.form_EditPost.cleaned_data.get('discussed_NOTE')
# 				self.post_item.discussed_with_other_team_members_SCORE = self.form_EditPost.cleaned_data.get('discussed_with_other_team_members_SCORE')
# 				self.post_item.discussed_with_other_team_members_NOTE = self.form_EditPost.cleaned_data.get('discussed_with_other_team_members_NOTE')
# 				self.post_item.expected_problems_are_reasoned_SCORE = self.form_EditPost.cleaned_data.get('expected_problems_are_reasoned_SCORE')
# 				self.post_item.expected_problems_are_reasoned_NOTE = self.form_EditPost.cleaned_data.get('expected_problems_are_reasoned_NOTE')
# 				self.post_item.arbitrary_problems_are_reasoned_SCORE = self.form_EditPost.cleaned_data.get('arbitrary_problems_are_reasoned_SCORE')
# 				self.post_item.arbitrary_problems_are_reasoned_NOTE = self.form_EditPost.cleaned_data.get('arbitrary_problems_are_reasoned_NOTE')
# 				self.post_item.expected_constraints_are_reasoned_SCORE = self.form_EditPost.cleaned_data.get('expected_constraints_are_reasoned_SCORE')
# 				self.post_item.expected_constraints_are_reasoned_NOTE = self.form_EditPost.cleaned_data.get('expected_constraints_are_reasoned_NOTE')
# 				self.post_item.arbitrary_constraints_are_reasoned_SCORE = self.form_EditPost.cleaned_data.get('arbitrary_constraints_are_reasoned_SCORE')
# 				self.post_item.arbitrary_constraints_are_reasoned_NOTE = self.form_EditPost.cleaned_data.get('arbitrary_constraints_are_reasoned_NOTE')
# 				self.post_item.designed_with_one_approach_SCORE = self.form_EditPost.cleaned_data.get('designed_with_one_approach_SCORE')
# 				self.post_item.designed_with_one_approach_NOTE = self.form_EditPost.cleaned_data.get('designed_with_one_approach_NOTE')
# 				self.post_item.designed_with_multiple_possible_approaches_SCORE = self.form_EditPost.cleaned_data.get('designed_with_multiple_possible_approaches_SCORE')
# 				self.post_item.designed_with_multiple_possible_approaches_NOTE = self.form_EditPost.cleaned_data.get('designed_with_multiple_possible_approaches_NOTE')
# 				self.post_item.save()

# 				# return HttpResponseRedirect(reverse('postdetails_DS', args=[event_id]))
# 		else:
# 			self.form_EditPost = NewPostForm_DS()
			

# ############# display
# 		post_objects_get = Post_DS.objects.get(id=event_id) 
# 		post_objects_SkillsIllustrations=Post_Objects_SkillsIllustrations_DS(request,event_id)
# 		post_objects_dislay=Post_Display_DS(request,event_id)

# 		self.context = {
# 			'form_EditPost':self.form_EditPost,
# 			'post_item':self.post_item,
# 			'post':post_objects_dislay.post,
# 			'favorited':post_objects_dislay.favorited,
# 			'profile':post_objects_dislay.profile,
# 			'comments':post_objects_dislay.comments,
# 	########################################################## score
# 			'barChart_code_quality': post_objects_SkillsIllustrations.barChart_code_quality,
# 			'barChart_communication_skills':post_objects_SkillsIllustrations.barChart_communication_skills,
# 			'barChart_team_work_skills':post_objects_SkillsIllustrations.barChart_team_work_skills,
# 			'barChart_leadership_skills':post_objects_SkillsIllustrations.barChart_leadership_skills, 
# 			'barChart_problem_solving_skills':post_objects_SkillsIllustrations.barChart_problem_solving_skills,

# 			'skills_avgScore':post_objects_SkillsIllustrations.skills_avgScore,
# 			'skills_avgScore_dashboard':post_objects_SkillsIllustrations.skills_avgScore_dashboard,
# 			'sum_of_post_quality':post_objects_SkillsIllustrations.sum_of_post_quality,

# 			'bubblePlot':post_objects_SkillsIllustrations.bubblePlot,
# 	########################################################## note

# 		############PROCESS QUALITY

# 			# analyzed_SCORE
# 			# analyzed_with_other_team_members_SCORE
# 			# analyzed_other_team_members_script_SCORE
# 			# discussed_SCORE
# 			# discussed_with_other_team_members_SCORE
# 			# expected_problems_are_reasoned_SCORE
# 			# arbitrary_problems_are_reasoned_SCORE
# 			# expected_constraints_are_reasoned_SCORE
# 			# arbitrary_constraints_are_reasoned_SCORE
# 			# designed_with_one_approach_SCORE
# 			# designed_with_multiple_possible_approaches_SCORE

# 			#PROCESS QUALITY _SCORE
# 			'clean_NOTE':post_objects_get.clean_NOTE,
# 			'refactored_NOTE':post_objects_get.refactored_NOTE,
# 			'well_documented_NOTE':post_objects_get.well_documented_NOTE,
# 			'unit_tested_NOTE':post_objects_get.unit_tested_NOTE,
# 			'debuged_NOTE':post_objects_get.debuged_NOTE,
# 			'debuged_with_other_team_members_NOTE':post_objects_get.debuged_with_other_team_members_NOTE,
# 			'debuged_other_team_members_bugs_NOTE':post_objects_get.debuged_other_team_members_bugs_NOTE,
# 			#PROCESS QUALITY _NOTE
# 			'analyzed_NOTE':post_objects_get.analyzed_NOTE,
# 			'analyzed_with_other_team_members_NOTE':post_objects_get.analyzed_with_other_team_members_NOTE,
# 			'analyzed_other_team_members_script_NOTE':post_objects_get.analyzed_other_team_members_script_NOTE,
# 			'discussed_NOTE':post_objects_get.discussed_NOTE,
# 			'discussed_with_other_team_members_NOTE':post_objects_get.discussed_with_other_team_members_NOTE,
# 			'expected_problems_are_reasoned_NOTE':post_objects_get.expected_problems_are_reasoned_NOTE,
# 			'arbitrary_problems_are_reasoned_NOTE':post_objects_get.arbitrary_problems_are_reasoned_NOTE,
# 			'expected_constraints_are_reasoned_NOTE':post_objects_get.expected_constraints_are_reasoned_NOTE,
# 			'arbitrary_constraints_are_reasoned_NOTE':post_objects_get.arbitrary_constraints_are_reasoned_NOTE,
# 			'designed_with_one_approach_NOTE':post_objects_get.designed_with_one_approach_NOTE,
# 			'designed_with_multiple_possible_approaches_NOTE':post_objects_get.designed_with_multiple_possible_approaches_NOTE,

# 		}





 


class Post_EditPost_DS():
	def __init__(self, request, event_id):
		self.user = request.user.id
		self.post_object = Post_DS.objects.get(pk=event_id)

		self.post=Post_DS.objects.all()
		
		if request.method == 'POST':
			self.form = NewPostForm_DS(request.POST, request.FILES)
			if self.form.is_valid():
			
				# #METHOD TYPES 
				self.post_object.task_choice = self.form.cleaned_data.get('task_choice')
				self.post_object.project_choice = self.form.cleaned_data.get('project_choice')
				self.post_object.examine_types = self.form.cleaned_data.get('examine_types')
				self.post_object.task_method = self.form.cleaned_data.get('task_method')
				self.post_object.task_completion = self.form.cleaned_data.get('task_completion')
				self.post_object.sdls_phase = self.form.cleaned_data.get('sdls_phase')
				self.post_object.evaluation_duration = self.form.cleaned_data.get('evaluation_duration')

				#CODE QUALITY
				self.post_object.clean_SCORE = self.form.cleaned_data.get('clean_SCORE')
				self.post_object.clean_NOTE = self.form.cleaned_data.get('clean_NOTE')
				self.post_object.refactored_SCORE = self.form.cleaned_data.get('refactored_SCORE')
				self.post_object.refactored_NOTE = self.form.cleaned_data.get('refactored_NOTE')
				self.post_object.well_documented_SCORE = self.form.cleaned_data.get('well_documented_SCORE')
				self.post_object.well_documented_NOTE = self.form.cleaned_data.get('well_documented_NOTE')
				self.post_object.unit_tested_SCORE = self.form.cleaned_data.get('unit_tested_SCORE')
				self.post_object.unit_tested_NOTE = self.form.cleaned_data.get('unit_tested_NOTE')
				self.post_object.debuged_SCORE = self.form.cleaned_data.get('debuged_SCORE')
				self.post_object.debuged_NOTE = self.form.cleaned_data.get('debuged_NOTE')
				self.post_object.debuged_with_other_team_members_SCORE = self.form.cleaned_data.get('debuged_with_other_team_members_SCORE')
				self.post_object.debuged_with_other_team_members_NOTE = self.form.cleaned_data.get('debuged_with_other_team_members_NOTE')
				self.post_object.debuged_other_team_members_bugs_SCORE = self.form.cleaned_data.get('debuged_other_team_members_bugs_SCORE')
				self.post_object.debuged_other_team_members_bugs_NOTE = self.form.cleaned_data.get('debuged_other_team_members_bugs_NOTE') 

				#PROCESS QUALITY 
				self.post_object.analyzed_SCORE = self.form.cleaned_data.get('analyzed_SCORE')
				self.post_object.analyzed_NOTE = self.form.cleaned_data.get('analyzed_NOTE')
				self.post_object.analyzed_with_other_team_members_SCORE = self.form.cleaned_data.get('analyzed_with_other_team_members_SCORE')
				self.post_object.analyzed_with_other_team_members_NOTE = self.form.cleaned_data.get('analyzed_with_other_team_members_NOTE')
				self.post_object.analyzed_other_team_members_script_SCORE = self.form.cleaned_data.get('analyzed_other_team_members_script_SCORE')
				self.post_object.analyzed_other_team_members_script_NOTE = self.form.cleaned_data.get('analyzed_other_team_members_script_NOTE')
				self.post_object.discussed_SCORE = self.form.cleaned_data.get('discussed_SCORE')
				self.post_object.discussed_NOTE = self.form.cleaned_data.get('discussed_NOTE')
				self.post_object.discussed_with_other_team_members_SCORE = self.form.cleaned_data.get('discussed_with_other_team_members_SCORE')
				self.post_object.discussed_with_other_team_members_NOTE = self.form.cleaned_data.get('discussed_with_other_team_members_NOTE')
				self.post_object.expected_problems_are_reasoned_SCORE = self.form.cleaned_data.get('expected_problems_are_reasoned_SCORE')
				self.post_object.expected_problems_are_reasoned_NOTE = self.form.cleaned_data.get('expected_problems_are_reasoned_NOTE')
				self.post_object.arbitrary_problems_are_reasoned_SCORE = self.form.cleaned_data.get('arbitrary_problems_are_reasoned_SCORE')
				self.post_object.arbitrary_problems_are_reasoned_NOTE = self.form.cleaned_data.get('arbitrary_problems_are_reasoned_NOTE')
				self.post_object.expected_constraints_are_reasoned_SCORE = self.form.cleaned_data.get('expected_constraints_are_reasoned_SCORE')
				self.post_object.expected_constraints_are_reasoned_NOTE = self.form.cleaned_data.get('expected_constraints_are_reasoned_NOTE')
				self.post_object.arbitrary_constraints_are_reasoned_SCORE = self.form.cleaned_data.get('arbitrary_constraints_are_reasoned_SCORE')
				self.post_object.arbitrary_constraints_are_reasoned_NOTE = self.form.cleaned_data.get('arbitrary_constraints_are_reasoned_NOTE')
				self.post_object.designed_with_one_approach_SCORE = self.form.cleaned_data.get('designed_with_one_approach_SCORE')
				self.post_object.designed_with_one_approach_NOTE = self.form.cleaned_data.get('designed_with_one_approach_NOTE')
				self.post_object.designed_with_multiple_possible_approaches_SCORE = self.form.cleaned_data.get('designed_with_multiple_possible_approaches_SCORE')
				self.post_object.designed_with_multiple_possible_approaches_NOTE = self.form.cleaned_data.get('designed_with_multiple_possible_approaches_NOTE')

				self.post_object.save()
				return redirect('index_DS')

		else:
			self.form = NewPostForm_DS()



	######### display
		posts = Post_DS.objects.filter(user=self.user).order_by('-posted') 
		profile_activityCalculations = Profile_activityCalculations_DS(user=self.user)
		profile_Illustrations = Profile_Illustrations_DS(user=self.user)
		profile_Objects = Profile_Objects_DS(user=self.user) 
		
		self.context = {
			'posts':posts, 
			'form':self.form, 

			#profile
			'profile':profile_Objects.profile,

			# activity log dashboard
			"expreriencePost_notifications_count":profile_activityCalculations.expreriencePost_notifications_count,
			"all_OR_follower_post":profile_activityCalculations.all_OR_follower_post,
			'all_OR_follower_post_evaluation':profile_activityCalculations.all_OR_follower_post_evaluation,
			'expreriencePost_yourPost_count':profile_activityCalculations.expreriencePost_yourPost_count,

			'followingAndfollowers':profile_Illustrations.followingAndfollowers,
			'sum_of_Experience_unique_count':profile_Illustrations.sum_of_Experience_unique_count,

			'notifications_count':profile_activityCalculations.notifications_count,

			#chart
			"bubblePlot":profile_Illustrations.bubblePlot,
			'arranged_and_requestes':profile_Illustrations.arranged_and_requestes,
			'teamedUp_and_scored':profile_Illustrations.teamedUp_and_scored,


			#notification part
			'notifications': profile_activityCalculations.notifications,

			# activity log dashboard
			'follow_notifications_count':profile_activityCalculations.follow_notifications_count,
			'comment_notifications_count':profile_activityCalculations.comment_notifications_count,	
			"message_notifications_count":profile_activityCalculations.message_notifications_count,
			"like_notifications_count":profile_activityCalculations.like_notifications_count,
			'follow_status':profile_activityCalculations.follow_status,
			
			
			
		}




class Post_EditExperience_chart_DS():
	def __init__(self, request, event_id):
		self.user = request.user.id
		self.experience_object = Experience_chart.objects.get(pk=event_id)

		self.post=Experience_chart.objects.all()
		if request.method == 'POST':
			self.form = Experience_chart_Form_DS(request.POST, request.FILES)
			if self.form.is_valid():
			
				self.experience_object.technical_task = self.form.cleaned_data.get('technical_task')
				self.experience_object.technical_ocuppation = self.form.cleaned_data.get('technical_ocuppation')
				self.experience_object.start_date = self.form.cleaned_data.get('start_date')
				self.experience_object.finish_date = self.form.cleaned_data.get('finish_date')
				self.experience_object.save()
				# return redirect('index_DS')
		else:
			self.form = Experience_chart_Form_DS()

	######### display
		posts = Post_DS.objects.filter(user=self.user).order_by('-posted')
		post_objects_get=Profile_Objects_DS(user=self.user)
		profile_dateCalculations = Profile_dateCalculations_DS(user=self.user)
		profile_activityCalculations = Profile_activityCalculations_DS(user=self.user)
		profile_Illustrations = Profile_Illustrations_DS(user=self.user)
		
		self.context = {
			'posts':posts, 
			'form':self.form,
			'post':self.post,
			# 'followers_count':followers_count,
			'profile':post_objects_get.profile,

			# activity log dashboard
			"expreriencePost_notifications_count":profile_activityCalculations.expreriencePost_notifications_count,
			"all_OR_follower_post":profile_activityCalculations.all_OR_follower_post,
			'all_OR_follower_post_evaluation':profile_activityCalculations.all_OR_follower_post_evaluation,
			'expreriencePost_yourPost_count':profile_activityCalculations.expreriencePost_yourPost_count,

			'followingAndfollowers':profile_Illustrations.followingAndfollowers,
			'sum_of_Experience_unique_count':profile_Illustrations.sum_of_Experience_unique_count,

			'worked_days_sum':profile_dateCalculations.worked_days_sum,
			'responsibility_unique_responsible':profile_dateCalculations.responsibility_unique_responsible,
			'worked_sinceFirstYear':profile_dateCalculations.worked_sinceFirstYear,
			'tasks_unique_name':profile_dateCalculations.tasks_unique_name,
			'worked_months_sum':profile_dateCalculations.worked_months_sum,
			
		}




class Post_Experience_chart_DS():
	def __init__(self, request):	
		self.user = request.user
		self.post=Experience_chart.objects.all()
		
		if request.method == 'POST':
			self.form = Experience_chart_Form_DS(request.POST)

			if self.form.is_valid():
				self.post_owner_form=self.form.save(commit=False)
				self.post_owner_form.user=request.user
				self.post_owner_form.save()
				self.form.save_m2m()
				# return redirect('Experience_chart_DS')
		else:
			self.form = Experience_chart_Form_DS()
	
	######### display
		posts = Post_DS.objects.filter(user=self.user).order_by('-posted')
		post_objects_get=Profile_Objects_DS(user=self.user)
		profile_dateCalculations = Profile_dateCalculations_DS(user=self.user)
		profile_activityCalculations = Profile_activityCalculations_DS(user=self.user)
		profile_Illustrations = Profile_Illustrations_DS(user=self.user)

		self.context = {
			'posts':posts, 
			'form':self.form,
			'post':self.post,
			# 'followers_count':followers_count,
			'profile':post_objects_get.profile,

			# activity log dashboard
			"expreriencePost_notifications_count":profile_activityCalculations.expreriencePost_notifications_count,
			"all_OR_follower_post":profile_activityCalculations.all_OR_follower_post,
			'all_OR_follower_post_evaluation':profile_activityCalculations.all_OR_follower_post_evaluation,
			'expreriencePost_yourPost_count':profile_activityCalculations.expreriencePost_yourPost_count,

			'followingAndfollowers':profile_Illustrations.followingAndfollowers,
			'sum_of_Experience_unique_count':profile_Illustrations.sum_of_Experience_unique_count,

			'worked_days_sum':profile_dateCalculations.worked_days_sum,
			'responsibility_unique_responsible':profile_dateCalculations.responsibility_unique_responsible,
			'worked_sinceFirstYear':profile_dateCalculations.worked_sinceFirstYear,
			'tasks_unique_name':profile_dateCalculations.tasks_unique_name,
			'worked_months_sum':profile_dateCalculations.worked_months_sum,
			
		}






class Post_NewPost_DS():
	def __init__(self, request):

		self.user = request.user
		self.post=Post_DS.objects.all()
			
		if request.method == 'POST':
			self.form = NewPostForm_DS(request.POST)

			if self.form.is_valid():
				self.post_owner_form=self.form.save(commit=False)
				self.post_owner_form.user=request.user
				self.post_owner_form.save()
				self.form.save_m2m()
				# return redirect('newpost_DS')		
		else:
			self.form = NewPostForm_DS()

		#msg part
		self.messages = Message_DS.get_messages(self.user)
		self.active_direct = None
		self.directs = None

		if self.messages:
			self.message = self.messages[0]
			self.active_direct = self.message['user'].username
			self.directs = Message_DS.objects.filter(user=self.user, recipient=self.message['user'])
			self.directs.update(is_read=True)
			for self.message in self.messages:
				if self.message['user'].username == self.active_direct:
					self.message['unread'] = 0

	######### display
		profile_activityCalculations = Profile_activityCalculations_DS(user=self.user)
		profile_Illustrations = Profile_Illustrations_DS(user=self.user)
		profile_Objects = Profile_Objects_DS(user=self.user)

		self.context = {
			'form':self.form,
			'post':self.post,

			#msg part
			'directs': self.directs,
			'messages': self.messages,
			'active_direct': self.active_direct,


			#profile
			'profile':profile_Objects.profile,

			# activity log dashboard
			"expreriencePost_notifications_count":profile_activityCalculations.expreriencePost_notifications_count,
			"all_OR_follower_post":profile_activityCalculations.all_OR_follower_post,
			'all_OR_follower_post_evaluation':profile_activityCalculations.all_OR_follower_post_evaluation,
			'expreriencePost_yourPost_count':profile_activityCalculations.expreriencePost_yourPost_count,

			'followingAndfollowers':profile_Illustrations.followingAndfollowers,
			'sum_of_Experience_unique_count':profile_Illustrations.sum_of_Experience_unique_count,

			'notifications_count':profile_activityCalculations.notifications_count,

			#chart
			"bubblePlot":profile_Illustrations.bubblePlot,
			'arranged_and_requestes':profile_Illustrations.arranged_and_requestes,
			'teamedUp_and_scored':profile_Illustrations.teamedUp_and_scored,


			#notification part
			'notifications': profile_activityCalculations.notifications,

			# activity log dashboard
			'follow_notifications_count':profile_activityCalculations.follow_notifications_count,
			'comment_notifications_count':profile_activityCalculations.comment_notifications_count,	
			"message_notifications_count":profile_activityCalculations.message_notifications_count,
			"like_notifications_count":profile_activityCalculations.like_notifications_count,
			'follow_status':profile_activityCalculations.follow_status,
			
			
			
		}




	

class Post_Comment_DS():
	def __init__(self, request, post_id):

		self.user = request.user
		self.post = Post_DS.objects.get(id=post_id)
		
		#Comments Form
		if request.method == 'POST':
			self.form = CommentForm_DS(request.POST)
			if self.form.is_valid():
				self.comment = self.form.save(commit=False)
				self.comment.post = self.post
				self.comment.user = self.user
				self.comment.save()
				# return HttpResponseRedirect(reverse('postdetails_DS', args=[post_id]))
		else:
			self.form = CommentForm_DS()
		
		post_objects_get=Post_Objects_DS(request,post_id)
		post_objects_display=Post_Display_DS(request,post_id)
		post_objects_SkillsIllustrations=Post_Objects_SkillsIllustrations_DS(request,post_id)

		self.context = {
			'form':self.form,
			'post':self.post,

			'favorited':post_objects_display.favorited,
			'profile':post_objects_display.profile,
			'comments':post_objects_display.comments,
		########################################################## score

			'barChart_code_quality': post_objects_SkillsIllustrations.barChart_code_quality,
			'barChart_communication_skills' : post_objects_SkillsIllustrations.barChart_communication_skills,
			'barChart_team_work_skills' : post_objects_SkillsIllustrations.barChart_team_work_skills,
			'barChart_leadership_skills' : post_objects_SkillsIllustrations.barChart_leadership_skills,
			'barChart_problem_solving_skills' : post_objects_SkillsIllustrations.barChart_problem_solving_skills,
			'skills_avgScore' : post_objects_SkillsIllustrations.skills_avgScore,
			'skills_avgScore_dashboard' : post_objects_SkillsIllustrations.skills_avgScore_dashboard,
			'sum_of_post_quality' : post_objects_SkillsIllustrations.sum_of_post_quality,
			'bubblePlot' : post_objects_SkillsIllustrations.bubblePlot,

			#PROCESS QUALITY _SCORE
			'clean_NOTE' : post_objects_get.clean_NOTE,
			'refactored_NOTE' : post_objects_get.refactored_NOTE,
			'well_documented_NOTE' : post_objects_get.well_documented_NOTE,
			'unit_tested_NOTE' : post_objects_get.unit_tested_NOTE,
			'debuged_NOTE' : post_objects_get.debuged_NOTE,
			'debuged_with_other_team_members_NOTE' : post_objects_get.debuged_with_other_team_members_NOTE,
			'debuged_other_team_members_bugs_NOTE' : post_objects_get.debuged_other_team_members_bugs_NOTE,
			#PROCESS QUALITY _NOTE
			'analyzed_NOTE' : post_objects_get.analyzed_NOTE,
			'analyzed_with_other_team_members_NOTE' : post_objects_get.analyzed_with_other_team_members_NOTE,
			'analyzed_other_team_members_script_NOTE' : post_objects_get.analyzed_other_team_members_script_NOTE,
			'discussed_NOTE' : post_objects_get.discussed_NOTE,
			'discussed_with_other_team_members_NOTE' : post_objects_get.discussed_with_other_team_members_NOTE,
			'expected_problems_are_reasoned_NOTE' : post_objects_get.expected_problems_are_reasoned_NOTE,
			'arbitrary_problems_are_reasoned_NOTE' : post_objects_get.arbitrary_problems_are_reasoned_NOTE,
			'expected_constraints_are_reasoned_NOTE' : post_objects_get.expected_constraints_are_reasoned_NOTE,
			'arbitrary_constraints_are_reasoned_NOTE' : post_objects_get.arbitrary_constraints_are_reasoned_NOTE,
			'designed_with_one_approach_NOTE' : post_objects_get.designed_with_one_approach_NOTE,
			'designed_with_multiple_possible_approaches_NOTE' : post_objects_get.designed_with_multiple_possible_approaches_NOTE,

		}
















class Post_Directs_DS():
	def __init__(self, request, username):
		self.user = request.user
		self.messages = Message_DS.get_messages(user=self.user)
		self.active_direct = username
		self.directs = Message_DS.objects.filter(user=self.user, recipient__username=username)	

		self.form = MessageSendForm_DS()

		self.directs.update(is_read=True)
		for self.message in self.messages:
			if self.message['user'].username == username:
				self.message['unread'] = 0


	######### display
		profile_activityCalculations = Profile_activityCalculations_DS(user=self.user)
		profile_Illustrations = Profile_Illustrations_DS(user=self.user)

		

		self.context = {
			'directs': self.directs,
			'messages': self.messages,
			'active_direct':self.active_direct,
			'form': self.form,

			#notification part
			'notifications': profile_activityCalculations.notifications,

			# activity log dashboard
			'follow_notifications_count':profile_activityCalculations.follow_notifications_count,
			'comment_notifications_count':profile_activityCalculations.comment_notifications_count,	
			"message_notifications_count":profile_activityCalculations.message_notifications_count,
			"like_notifications_count":profile_activityCalculations.like_notifications_count,
			###################################################################
			"expreriencePost_notifications_count":profile_activityCalculations.expreriencePost_notifications_count,
			"all_OR_follower_post":profile_activityCalculations.all_OR_follower_post,
			'all_OR_follower_post_evaluation':profile_activityCalculations.all_OR_follower_post_evaluation,
			'expreriencePost_yourPost_count':profile_activityCalculations.expreriencePost_yourPost_count,

			'followingAndfollowers':profile_Illustrations.followingAndfollowers,
			'sum_of_Experience_unique_count':profile_Illustrations.sum_of_Experience_unique_count,

			'notifications_count':profile_activityCalculations.notifications_count,

			#chart
			"bubblePlot":profile_Illustrations.bubblePlot,
			'arranged_and_requestes':profile_Illustrations.arranged_and_requestes,
			'teamedUp_and_scored':profile_Illustrations.teamedUp_and_scored,
			
			'follow_status':profile_activityCalculations.follow_status,
			}






class Post_NewConversation_DS():
	def __init__(self, request, username):
		self.from_user = request.user
		self.body = ''
		self.body2=''

		self.task_choice=''
		self.project_choice=''
		self.examine_types=''
		self.task_method=''
		self.task_completion=''
		self.sdls_phase=''
		self.evaluation_duration=''
		try:
			self.to_user = User.objects.get(username=username)
		except Exception as e:
			return redirect('usersearch_DS')
		if self.from_user != self.to_user:
			Message_DS.send_message(self.from_user, self.to_user, self.body, self.body2, self.task_choice, self.project_choice, self.examine_types, self.task_method, self.task_completion, self.sdls_phase, self.evaluation_duration)
			# return redirect('NewConversation_DS')


		self.user = request.user
		self.messages = Message_DS.get_messages(user=self.user)
		self.active_direct = username
		self.directs = Message_DS.objects.filter(user=self.user, recipient__username=username)	

		self.form = MessageSendForm_DS()

		self.directs.update(is_read=True)
		for self.message in self.messages:
			if self.message['user'].username == username:
				self.message['unread'] = 0
				
		
	######### display
		profile_activityCalculations = Profile_activityCalculations_DS(user=self.user)
		profile_Illustrations = Profile_Illustrations_DS(user=self.user)

		

		self.context = {
			'directs': self.directs,
			'messages': self.messages,
			'active_direct': self.active_direct,
			'form': self.form,

			#notification part
			'notifications': profile_activityCalculations.notifications,

			# activity log dashboard
			'follow_notifications_count':profile_activityCalculations.follow_notifications_count,
			'comment_notifications_count':profile_activityCalculations.comment_notifications_count,	
			"message_notifications_count":profile_activityCalculations.message_notifications_count,
			"like_notifications_count":profile_activityCalculations.like_notifications_count,
			###################################################################
			"expreriencePost_notifications_count":profile_activityCalculations.expreriencePost_notifications_count,
			"all_OR_follower_post":profile_activityCalculations.all_OR_follower_post,
			'all_OR_follower_post_evaluation':profile_activityCalculations.all_OR_follower_post_evaluation,
			'expreriencePost_yourPost_count':profile_activityCalculations.expreriencePost_yourPost_count,

			'followingAndfollowers':profile_Illustrations.followingAndfollowers,
			'sum_of_Experience_unique_count':profile_Illustrations.sum_of_Experience_unique_count,

			'notifications_count':profile_activityCalculations.notifications_count,

			#chart
			"bubblePlot":profile_Illustrations.bubblePlot,
			'arranged_and_requestes':profile_Illustrations.arranged_and_requestes,
			'teamedUp_and_scored':profile_Illustrations.teamedUp_and_scored,
			
			'follow_status':profile_activityCalculations.follow_status,
			}







class Post_UserSearch_DS():
	def __init__(self, request):	
		# query part
		self.query = request.GET.get("q")
		self.page_number = request.GET.get('page')

		self.last_name_paginator=[]
		self.first_name_paginator=[]
		self.industry_and_projects_paginator=[]
		self.location_paginator=[]
		self.github_paginator=[]
		
		if self.query:
			self.users = Profile_DS.objects.filter(Q(last_name__icontains=self.query))
			self.paginator = Paginator(self.users, 9)
			for i in self.paginator.get_page(self.page_number):
				self.last_name_paginator.append(i)

		if self.query:
			self.first_name = Profile_DS.objects.filter(Q(first_name__icontains=self.query))
			self.paginator = Paginator(self.first_name, 9)
			for i in self.paginator.get_page(self.page_number):
				self.first_name_paginator.append(i)

		if self.query:
			self.industry_and_projects = Profile_DS.objects.filter(Q(industry_and_projects__icontains=self.query))
			self.paginator = Paginator( self.industry_and_projects , 9)
			for i in self.paginator.get_page(self.page_number):
				self.industry_and_projects_paginator.append(i)

		if self.query:
			self.location = Profile_DS.objects.filter(Q(location__icontains=self.query))
			self.paginator = Paginator( self.location , 9)
			for i in self.paginator.get_page(self.page_number):
				self.location_paginator.append(i)

		if self.query:
			self.github = Profile_DS.objects.filter(Q(github__icontains=self.query))
			self.paginator = Paginator( self.github , 9)
			for i in self.paginator.get_page(self.page_number):
				self.github_paginator.append(i)


		# msg part
		self.user=request.user
		self.messages = Message_DS.get_messages(self.user)
		self.active_direct = None
		self.directs = None

		if self.messages:
			self.message = self.messages[0]
			self.active_direct = self.message['user'].username
			self.directs = Message_DS.objects.filter(user=request.user, recipient=self.message['user'])
			self.directs.update(is_read=True)
			for self.message in self.messages:
				if self.message['user'].username == self.active_direct:
					self.message['unread'] = 0



	######### display
		profile_activityCalculations = Profile_activityCalculations_DS(user=self.user)
		profile_Illustrations = Profile_Illustrations_DS(user=self.user)

			
		self.context = {
		'last_name': self.last_name_paginator,
		'users_first_name':self.first_name_paginator,
		'users_industry_and_projects':self.industry_and_projects_paginator,
		'users_location':self.location_paginator,
		'users_github':self.github_paginator,

		#msg part
		'directs': self.directs,
		'messages': self.messages,
		'active_direct': self.active_direct,

		#notification part
		'notifications': profile_activityCalculations.notifications,

		# activity log dashboard
		'follow_notifications_count':profile_activityCalculations.follow_notifications_count,
		'comment_notifications_count':profile_activityCalculations.comment_notifications_count,	
		"message_notifications_count":profile_activityCalculations.message_notifications_count,
		"like_notifications_count":profile_activityCalculations.like_notifications_count,
		###################################################################
		"expreriencePost_notifications_count":profile_activityCalculations.expreriencePost_notifications_count,
		"all_OR_follower_post":profile_activityCalculations.all_OR_follower_post,
		'all_OR_follower_post_evaluation':profile_activityCalculations.all_OR_follower_post_evaluation,
		'expreriencePost_yourPost_count':profile_activityCalculations.expreriencePost_yourPost_count,

		'followingAndfollowers':profile_Illustrations.followingAndfollowers,
		'sum_of_Experience_unique_count':profile_Illustrations.sum_of_Experience_unique_count,

		'notifications_count':profile_activityCalculations.notifications_count,

		#chart
		"bubblePlot":profile_Illustrations.bubblePlot,
		'arranged_and_requestes':profile_Illustrations.arranged_and_requestes,
		'teamedUp_and_scored':profile_Illustrations.teamedUp_and_scored,
		
		'follow_status':profile_activityCalculations.follow_status,

		}

		