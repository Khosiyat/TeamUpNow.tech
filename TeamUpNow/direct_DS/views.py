from django.shortcuts import render, redirect
from django.template import loader, RequestContext
from django.http import HttpResponse, HttpResponseRedirect, HttpResponseBadRequest

from django.contrib.auth.decorators import login_required

from django.contrib.auth.models import User

from django.db.models import Q
from django.core.paginator import Paginator

from datetime import date, timedelta,datetime


from direct_DS.models import Message_DS
from direct_DS.forms import MessageSendForm_DS

from .utils import *
from authy_DS.utils import *
from TeamUpNow.model_objects_DS import *


from notifications_DS.models import Notification_DS
from post_DS.models import Follow_DS,Stream_DS,Stream_DS, Post_DS, Experience_chart
from authy_DS.models import Profile_DS


##########################################################################################################################################################################################
@login_required
def Inbox_DS(request):
	user=request.user
	messages = Message_DS.get_messages(user)
	active_direct = None
	directs = None

	######### display
	profile_activityCalculations = Profile_activityCalculations_DS(user=user)
	profile_Illustrations = Profile_Illustrations_DS(user=user)
	profile_Objects=Profile_Objects_DS(user=user)

	######### msg part
	if messages:
		message = messages[0]
		active_direct = message['user'].username
		directs = Message_DS.objects.filter(user=request.user, recipient=message['user'])
		directs.update(is_read=True)
		for message in messages:
			if message['user'].username == active_direct:
				message['unread'] = 0


	context = {
			'directs': directs,
			'messages': messages,
			'active_direct':active_direct,
			# 'form': form,

			#profile
			'profile':profile_Objects.profile,

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


	template = loader.get_template('templates_DS/direct/direct_DS.html')

	return HttpResponse(template.render(context, request))

##########################################################################################################################################################################################
@login_required
def UserSearch_DS(request):
	# query part
	query = request.GET.get("q")
	page_number = request.GET.get('page')

	last_name_paginator=[]
	first_name_paginator=[]
	industry_and_projects_paginator=[]
	location_paginator=[]
	github_paginator=[]
	
	if query:
		users = Profile_DS.objects.filter(Q(last_name__icontains=query))
		paginator = Paginator(users, 9)
		for i in paginator.get_page(page_number):
			last_name_paginator.append(i)

	if query:
		first_name = Profile_DS.objects.filter(Q(first_name__icontains=query))
		paginator = Paginator(first_name, 9)
		for i in paginator.get_page(page_number):
			first_name_paginator.append(i)

	if query:
		industry_and_projects = Profile_DS.objects.filter(Q(industry_and_projects__icontains=query))
		paginator = Paginator( industry_and_projects , 9)
		for i in paginator.get_page(page_number):
			industry_and_projects_paginator.append(i)

	if query:
		location = Profile_DS.objects.filter(Q(location__icontains=query))
		paginator = Paginator( location , 9)
		for i in paginator.get_page(page_number):
			location_paginator.append(i)

	if query:
		github = Profile_DS.objects.filter(Q(github__icontains=query))
		paginator = Paginator( github , 9)
		for i in paginator.get_page(page_number):
			github_paginator.append(i)



	# msg part
	user=request.user
	messages = Message_DS.get_messages(user)
	active_direct = None
	directs = None

	if messages:
		message = messages[0]
		active_direct = message['user'].username
		directs = Message_DS.objects.filter(user=request.user, recipient=message['user'])
		directs.update(is_read=True)
		for message in messages:
			if message['user'].username == active_direct:
				message['unread'] = 0




		######### display
	profile_activityCalculations = Profile_activityCalculations_DS(user=user)
	profile_Illustrations = Profile_Illustrations_DS(user=user)
	profile_Objects=Profile_Objects_DS(user=user)
	
	

	context = {
	'last_name': last_name_paginator,
	'users_first_name':first_name_paginator,
	'users_industry_and_projects':industry_and_projects_paginator,
	'users_location':location_paginator,
	'users_github':github_paginator,

	#msg part
	'directs': directs,
	'messages': messages,
	'active_direct': active_direct,

	#profile
	'profile':profile_Objects.profile,

	
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
			

	template = loader.get_template('templates_DS/direct/search_user_DS.html')
	
	return HttpResponse(template.render(context, request))

##########################################################################################################################################################################################
@login_required
def Directs_DS(request, username):
	user = request.user
	messages = Message_DS.get_messages(user=user)
	active_direct = username
	directs = Message_DS.objects.filter(user=user, recipient__username=username)	

	form = MessageSendForm_DS()

	directs.update(is_read=True)
	for message in messages:
		if message['user'].username == username:
			message['unread'] = 0



	######### display
	profile_activityCalculations = Profile_activityCalculations_DS(user=user)
	profile_Illustrations = Profile_Illustrations_DS(user=user)
	profile_Objects=Profile_Objects_DS(user=user)

	

	context = {
		'directs': directs,
		'messages': messages,
		'active_direct':active_direct,
		'form': form,

		#profile
		'profile':profile_Objects.profile,
		
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

	template = loader.get_template('templates_DS/direct/direct_DS_compose.html')

	return HttpResponse(template.render(context, request))

##########################################################################################################################################################################################
@login_required
def NewConversation_DS(request, username):
	from_user = request.user
	body = ''
	body2=''

	task_choice=''
	project_choice=''
	examine_types=''
	task_method=''
	task_completion=''
	sdls_phase=''
	evaluation_duration=''
	try:
		to_user = User.objects.get(username=username)
	except Exception as e:
		return redirect('UserSearch_DS')
	if from_user != to_user:
		Message_DS.send_message(from_user, to_user, body, body2, task_choice, project_choice, examine_types, task_method, task_completion, sdls_phase, evaluation_duration)
		# return redirect('NewConversation_DS')


	user = request.user
	messages = Message_DS.get_messages(user=user)
	active_direct = username
	directs = Message_DS.objects.filter(user=user, recipient__username=username)	

	form = MessageSendForm_DS()

	directs.update(is_read=True)
	for message in messages:
		if message['user'].username == username:
			message['unread'] = 0
			
	

		######### display
	profile_activityCalculations = Profile_activityCalculations_DS(user=user)
	profile_Illustrations = Profile_Illustrations_DS(user=user)
	profile_Objects=Profile_Objects_DS(user=user)

	context = {
		
		'directs': directs,
		'messages': messages,
		'active_direct':active_direct,
		'form': form,


		#profile
		'profile':profile_Objects.profile,
	
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

	template = loader.get_template('templates_DS/direct/direct_DS_compose.html')

	return HttpResponse(template.render(context, request))

##########################################################################################################################################################################################
@login_required
def SendDirect_DS(request):
	from_user = request.user
	to_user_username = request.POST.get('to_user')
	body = request.POST.get('body')
	body2=request.POST.get('body2')

	task_choice=request.POST.get('task_choice')
	project_choice=request.POST.get('project_choice')
	examine_types=request.POST.get('examine_types')
	task_method=request.POST.get('task_method')
	task_completion=request.POST.get('task_completion')
	sdls_phase=request.POST.get('sdls_phase')
	evaluation_duration=request.POST.get('evaluation_duration')
	
	if request.method == 'POST':
		to_user = User.objects.get(username=to_user_username)
		Message_DS.send_message(from_user, to_user, body, body2, task_choice, project_choice, examine_types, task_method, task_completion, sdls_phase, evaluation_duration)
		return redirect('Inbox_DS')
	else:
		HttpResponseBadRequest()

##########################################################################################################################################################################################

def checkDirects_DS(request):
	directs_count = 0
	if request.user.is_authenticated:
		directs_count = Message_DS.objects.filter(user=request.user, is_read=False).count()

	return {'directs_count':directs_count}


	# task_choice
	# project_choice
	# examine_types
	# task_method
	# task_completion
	# sdls_phase
	# evaluation_duration
	