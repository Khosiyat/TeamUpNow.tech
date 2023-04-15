from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.models import User

from django.contrib.auth.decorators import login_required
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth import update_session_auth_hash
from django.contrib.auth.models import User, Group
from django.contrib import messages

from django.db import transaction
from django.template import loader
from django.http import HttpResponse, HttpResponseRedirect
from django.urls import reverse, resolve
from django.core.paginator import Paginator

#local libraries
from authy_DS.models import Profile_DS
from post_DS.models import Post_DS, Experience_chart,  Follow_DS, Stream_DS
from authy_DS.forms import SignupForm_DS, LoginForm_DS, ChangePasswordForm_DS, EditProfileForm_DS
from notifications_DS.models import Notification_DS

from .decorators import *
from .utils import *
from TeamUpNow.model_objects_DS import (Post_Objects_DS, 
										 Post_Objects_SkillsIllustrations_DS, 
										 Post_Display_DS, 
										 Post_Display_contextList_DS, 
										 Profile_Objects_DS, 
										 Profile_dateCalculations_DS, 
										 Profile_activityCalculations_DS,
										 Profile_Illustrations_DS, 
										 Profile_ProjectsIllustrations_DS, 
										 Profile_Display_contextList_DS, 
										 EditProfile_objects_DS,
										 )

import math

#data visualize libraries
import pandas as pd
import plotly.figure_factory as ff
from plotly.offline import plot
import plotly.express as px

import numpy as np
import matplotlib.pyplot as plt


from datetime import date, timedelta,datetime

from dateutil import relativedelta

######################################################################### User Profile EvaluationList  #########################################################################
@login_required
def UserProfile_category_EvaluationList_DS(request, username):

	profile_Display_contextList=Profile_Display_contextList_DS(request,username)

	template = loader.get_template('templates_DS/UserProfile_category_EvaluationList_DS.html')

	context = profile_Display_contextList.context

	return HttpResponse(template.render(context, request))

######################################################################### User Profile ExperienceList #########################################################################
@login_required
def UserProfile_category_ExperienceList_DS(request, username):

	profile_Display_contextList=Profile_Display_contextList_DS(request,username)

	template = loader.get_template('templates_DS/UserProfile_category_ExperienceList_DS.html')

	context = profile_Display_contextList.context

	return HttpResponse(template.render(context, request))

######################################################################### User Profile DAYS #########################################################################

@login_required
def UserProfile_category_DAYS_DS(request, username):

	profile_Display_contextList=Profile_Display_contextList_DS(request,username)

	template = loader.get_template('templates_DS/UserProfile_category_DAYS_DS.html')

	context = profile_Display_contextList.context

	return HttpResponse(template.render(context, request))

######################################################################### User Profile YEARS #########################################################################

@login_required
def UserProfile_category_YEARS_DS(request, username):

	profile_Display_contextList=Profile_Display_contextList_DS(request,username)

	template = loader.get_template('templates_DS/UserProfile_category_YEARS_DS.html')

	context = profile_Display_contextList.context

	return HttpResponse(template.render(context, request))

######################################################################### User Profile WORK HISTORY  #########################################################################

@login_required
def UserProfile_category_WORK_HISTORY_DS(request, username):

	profile_Display_contextList=Profile_Display_contextList_DS(request,username)

	template = loader.get_template('templates_DS/UserProfile_category_WORK_HISTORY_DS.html')

	context = profile_Display_contextList.context

	return HttpResponse(template.render(context, request))

######################################################################### User Profile MONTHS #########################################################################

@login_required
def UserProfile_category_MONTHS_DS (request, username):

	profile_Display_contextList=Profile_Display_contextList_DS(request,username)

	template = loader.get_template('templates_DS/UserProfile_category_MONTHS_DS.html')

	context = profile_Display_contextList.context

	return HttpResponse(template.render(context, request))

######################################################################### User Profile #########################################################################

@login_required
def UserProfile_DS(request, username):

	profile_Display_contextList=Profile_Display_contextList_DS(request,username)

	template = loader.get_template('templates_DS/profile_main_DS.html')

	context = profile_Display_contextList.context

	return HttpResponse(template.render(context, request))
 
##########################################################################################################################################################################################

@login_required
def EditProfile_DS(request):
		
	editProfile_objects_DS=EditProfile_objects_DS(request)

	template = loader.get_template('templates_DS/edit_profile_DS.html')

	context = editProfile_objects_DS.context

	return HttpResponse(template.render(context, request))


##########################################################################################################################################################################################

@login_required
def UserProfile_notifications_DS_evaluated(request, username):

	profile_Display_contextList=Profile_Display_contextList_DS(request,username)

	template = loader.get_template('templates_DS/profile_notifications_DS_evaluated.html')

	context = profile_Display_contextList.context

	return HttpResponse(template.render(context, request))

##########################################################################################################################################################################################

@login_required
def UserProfile_notifications_DS_requested(request, username):

	profile_Display_contextList=Profile_Display_contextList_DS(request,username)

	template = loader.get_template('templates_DS/profile_notifications_DS_requested.html')

	context = profile_Display_contextList.context

	return HttpResponse(template.render(context, request))

##########################################################################################################################################################################################

@login_required
def UserProfile_notifications_DS_scored(request, username):
	
	profile_Display_contextList=Profile_Display_contextList_DS(request,username)

	template = loader.get_template('templates_DS/profile_notifications_DS_scored.html')

	context = profile_Display_contextList.context

	return HttpResponse(template.render(context, request))

##########################################################################################################################################################################################

@login_required
def UserProfile_notifications_DS_teamedUp(request, username):
	
	profile_Display_contextList=Profile_Display_contextList_DS(request,username)

	template = loader.get_template('templates_DS/profile_notifications_DS_teamedUp.html')

	context = profile_Display_contextList.context

	return HttpResponse(template.render(context, request))

##########################################################################################################################################################################################

@login_required
def FriendProfile_notifications_DS_evaluated(request, username):

	profile_Display_contextList=Profile_Display_contextList_DS(request,username)

	template = loader.get_template('templates_DS/profileFriend_notifications_DS_evaluated.html')

	context = profile_Display_contextList.context

	return HttpResponse(template.render(context, request))


##########################################################################################################################################################################################

@login_required
def FriendProfile_notifications_DS_requested(request, username):

	profile_Display_contextList=Profile_Display_contextList_DS(request,username)

	template = loader.get_template('templates_DS/profileFriend_notifications_DS_requested.html')

	context = profile_Display_contextList.context

	return HttpResponse(template.render(context, request))

##########################################################################################################################################################################################

@login_required
def FriendProfile_notifications_DS_scored(request, username):

	profile_Display_contextList=Profile_Display_contextList_DS(request,username)

	template = loader.get_template('templates_DS/profileFriend_notifications_DS_scored.html')

	context = profile_Display_contextList.context

	return HttpResponse(template.render(context, request))

##########################################################################################################################################################################################

@login_required
def FriendProfile_notifications_DS_teamedUp(request, username):

	profile_Display_contextList=Profile_Display_contextList_DS(request,username)

	template = loader.get_template('templates_DS/profileFriend_notifications_DS_teamedUp.html')

	context = profile_Display_contextList.context

	return HttpResponse(template.render(context, request))

######################################################################### login  #########################################################################

def login_DS(request):
	if request.method == "POST":
		username = request.POST['username']
		password = request.POST['password']
		user = authenticate(request, username=username, password=password)
		if user is not None:
			login(request, user)
			return redirect('index_DS')
		else:
			messages.success(request, ("There Was An Error Logging In, Try Again..."))	
			return redirect('login_DS')	
	else:
		return render(request, 'templates_DS/login_DS.html', {})
  
######################################################################### login directing to create WELCOME FIRST Project #########################################################################

def login_DS_CreateProject(request):
	if request.method == "POST":
		username = request.POST['username']
		password = request.POST['password']
		user = authenticate(request, username=username, password=password)
		if user is not None:
			login(request, user)
			return redirect('index_DS_CreateProject')
		else:
			messages.success(request, ("There Was An Error Logging In, Try Again..."))	
			return redirect('login_DS_CreateProject')	
			# return redirect('EditProfile_DS')	
	else:
		return render(request, 'templates_DS/login_DS_CreateProject.html', {})

######################################################################### SIGN UP GROUPS #########################################################################

def Signup_DS(request):
	form = SignupForm_DS()
	if request.method == "POST":
		form = SignupForm_DS(request.POST)
		if form.is_valid():
			user = form.save()
			username = form.cleaned_data.get('username')
			password = form.cleaned_data.get('password')
			user.set_password(password)
			
			user.save() 

			is_created, group = Group.objects.get_or_create(name='dataScientist')
			if is_created:
				user.groups.add(Group.objects.get(name='dataScientist'))
			else:
				user.groups.add(group)
			# user = authenticate(username=username, password=password)
			# group=user.groups.add(group)
			# group.save()

			# group.user_set.add(user)

			# login(request, user)
			messages.success(request, "Registration Successful!" + username)
			return redirect('login_DS_CreateProject')
	# else:
	# 	form = RegisterUserForm()
	# 	group = Group.objects.get(name='Recruiter')

	return render(request, 'templates_DS/Signup_DS.html', {
		'form':form,
		})


##########################################################################################################################################################################################

@login_required
def PasswordChange(request):
	user = request.user
	if request.method == 'POST':
		form = ChangePasswordForm_DS(request.POST)
		if form.is_valid():
			new_password = form.cleaned_data.get('new_password')
			user.set_password(new_password)
			user.save()
			update_session_auth_hash(request, user)
			return redirect('change_password_done')
	else:
		form = ChangePasswordForm_DS(instance=user)

	context = {
		'form':form,
	}

	return render(request, 'templates_DS/change_password.html', context)

@login_required
def PasswordChangeDone(request):
	return render(request, 'templates_DS/change_password_done.html')

##########################################################################################################################################################################################

@login_required
def follow_DS(request, username, option):
	following = get_object_or_404(User, username=username)

	try:
		f, created = Follow_DS.objects.get_or_create(follower=request.user, following=following)

		if int(option) == 0:
			f.delete()
			Stream_DS.objects.filter(following=following, user=request.user).all().delete()
		else:
			 posts = Post_DS.objects.all().filter(user=following)[:25]

			 with transaction.atomic():
			 	for post in posts:
			 		stream = Stream_DS(post=post, user=request.user, date=post.posted, following=following)
			 		stream.save()

		return HttpResponseRedirect(reverse('UserProfile_DS', args=[username]))
	except User.DoesNotExist:
		return HttpResponseRedirect(reverse('UserProfile_DS', args=[username]))


##########################################################################################################################################################################################

@login_required
def Delete_accoundt_DS(request):

	if request.user == request.user:
		delete_user = User.objects.get(username=request.user)
		delete_user.delete()
		return redirect('Signup_DS')
	else:
		return redirect('Signup_DS')

##########################################################################################################################################################################################

@login_required
def pre_Delete_accoundt_DS(request):
	# if request.method == 'POST':
	if request.user == request.user:
		delete_user = User.objects.get(username=request.user)
		context={'delete_user':delete_user}
		return render(request, 'templates_DS/pre_Delete_accoundt_DS.html', context)		
	else:
		return redirect('Signup_DS')		
