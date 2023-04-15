from django.shortcuts import render, get_object_or_404, redirect
from django.http import HttpResponse, HttpResponseRedirect
from django.template import loader

from django.contrib.auth.models import User, Group


from post_DS.models import Stream_DS, Post_DS,Experience_chart, Tag_DS, Likes_DS, PostFileContent_DS, Follow_DS
from post_DS.forms import NewPostForm_DS, Experience_chart_Form_DS
from stories_employer.models import Story_employer, StoryStream_employer

from comment_DS.models import Comment_DS
from comment_DS.forms import CommentForm_DS

from authy_DS.models import Profile_DS

from notifications_DS.models import Notification_DS
from direct_DS.models import Message_DS



from django.contrib.auth.decorators import login_required

from django.urls import reverse

from statistics import mode, mean


from authy_DS.utils import *
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
							Post_EditExperience_chart_DS,
							Post_Experience_chart_DS,
							Post_NewPost_DS,
							Post_Comment_DS,
							Post_EditPost_DS,

							Profile_Display_contextList_DS, 
							)

from .decorators import *

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


######################################################################### index directing to createProject #########################################################################

def index_DS_CreateProject(request):
	user = request.user
	# posts = Stream_DS.objects.filter(user=user)

	# stories = StoryStream_employer.objects.filter(user=user)


	posts = Stream_DS.objects.all()

	stories = StoryStream_employer.objects.all()


	group_ids = []

	for post in posts:
		group_ids.append(post.post_id)
		
	post_items = Post_DS.objects.filter(id__in=group_ids).all().order_by('-posted')		

	template = loader.get_template('templates_DS/index_DS_CreateProject.html')

	context = {
		'post_items': post_items,
		'stories': stories,

	}

	return HttpResponse(template.render(context, request))

######################################################################### index #########################################################################  

def index_DS(request):
	user = request.user
	posts = Stream_DS.objects.filter(user=user)

	stories = StoryStream_employer.objects.filter(user=user)


	group_ids = []

	for post in posts:
		group_ids.append(post.post_id)
		
	post_items = Post_DS.objects.filter(id__in=group_ids).all().order_by('-posted')		

	template = loader.get_template('templates_DS/index_DS.html')

	context = {
		'post_items': post_items,
		'stories': stories,

	}

	return HttpResponse(template.render(context, request))

######################################################################### Projects|Experience chart #########################################################################   

def Experience_chart_DS(request):
	user = request.user
	post=Experience_chart.objects.all()
	
	
	if request.method == 'POST':
		form = Experience_chart_Form_DS(request.POST)

		if form.is_valid():
			print("Form is Valid!")
			post_owner_form=form.save(commit=False)
			print("Commited False!")
			post_owner_form.user=request.user
			print("has user!")
			post_owner_form.save()
			print("Saved!")
			form.save_m2m()
			print("m2m Saved!")


			return redirect('index_DS')
			# return redirect('Experience_chart_DS')
		# print("Saved!")
	else:
		form = Experience_chart_Form_DS()
		print("NOT saved!")

	print("POST IS UNSUCCESSFUL!")


	context = {
	'form':form,
	# 'post':post,
}

	return render(request, 'newproject_Experience_chart_DS.html', context)

######################################################################### First Project|Experience chart #########################################################################   

def Experience_chart_FirstProject_DS(request):
	user = request.user
	post=Experience_chart.objects.all()
	
	
	if request.method == 'POST':
		form = Experience_chart_Form_DS(request.POST)

		if form.is_valid():
			print("Form is Valid!")
			post_owner_form=form.save(commit=False)
			print("Commited False!")
			post_owner_form.user=request.user
			print("has user!")
			post_owner_form.save()
			print("Saved!")
			form.save_m2m()
			print("m2m Saved!")


			return redirect('edit-profile_DS')
			# return redirect('Experience_chart_DS')
		# print("Saved!")
	else:
		form = Experience_chart_Form_DS()
		print("NOT saved!")

	print("POST IS UNSUCCESSFUL!")


	context = {
	'form':form,
	# 'post':post,
}

	return render(request, 'newproject_Experience_chart_FirstProject_DS.html', context)

##########################################################################################################################################################################################

def PostDetails_DS(request, post_id):

	post_objects=Post_Display_contextList_DS(request,post_id)

	template = loader.get_template('templates_DS/post_detail_DS.html')

	context = post_objects.context

	return HttpResponse(template.render(context, request))

##########################################################################################################################################################################################

def PostDetails_category_TechSKILLS_DS(request, post_id):

	post_objects=Post_Display_contextList_DS(request,post_id)

	template = loader.get_template('templates_DS/post_detail_TechSKILLS_DS.html')

	context = post_objects.context

	return HttpResponse(template.render(context, request))

##########################################################################################################################################################################################

def PostDetails_category_SOFT_SKILLS_DS(request, post_id):

	post_objects=Post_Display_contextList_DS(request,post_id)

	template = loader.get_template('templates_DS/post_detail_SOFT_SKILLS_DS.html')

	context = post_objects.context

	return HttpResponse(template.render(context, request))

##########################################################################################################################################################################################

def PostDetails_category_ALL_SKILLS_DS(request, post_id):

	post_objects=Post_Display_contextList_DS(request,post_id)

	template = loader.get_template('templates_DS/post_detail_ALL_SKILLS_DS.html')

	context = post_objects.context

	return HttpResponse(template.render(context, request))

##########################################################################################################################################################################################

def PostDetails_category_PROBLEM_SOLVING_APROACH_DS(request, post_id):

	post_objects=Post_Display_contextList_DS(request,post_id)

	template = loader.get_template('templates_DS/post_detail_PROBLEM_SOLVING_APROACH_DS.html')

	context = post_objects.context

	return HttpResponse(template.render(context, request))

##########################################################################################################################################################################################

def NewPost_DS(request):
		
	post_NewPost_DS=Post_NewPost_DS(request)

	template = loader.get_template('newpost_DS.html')

	context = post_NewPost_DS.context

	return HttpResponse(template.render(context, request))

##########################################################################################################################################################################################

# @login_required
def EditPost_DS(request, event_id):

	post_EditPost_DS=Post_EditPost_DS(request,event_id)

	template = loader.get_template('templates_DS/editPost_DS.html')

	context = post_EditPost_DS.context

	return HttpResponse(template.render(context, request))

##########################################################################################################################################################################################

def PostDetails_reqeustTalent_DS(request, post_id):

	post_objects=Post_Display_contextList_DS(request,post_id)

	template = loader.get_template('templates_DS/post_detail_reqeustTalent_DS.html')

	context = post_objects.context

	return HttpResponse(template.render(context, request))

##########################################################################################################################################################################################

# @login_required
def comment_DS(request, post_id):
	
	post_Comment_employer=Post_Comment_DS(request,post_id)

	template = loader.get_template('templates_DS/post_detail_reqeustTalent_DS.html')

	context = post_Comment_employer.context

	return HttpResponse(template.render(context, request))


##########################################################################################################################################################################################

# @login_required
def EditExperience_chart_DS(request, event_id):
	
	post_EditExperience_chart_DS=Post_EditExperience_chart_DS(request,event_id)

	template = loader.get_template('templates_DS/editExperience_chart_DS.html')

	context = post_EditExperience_chart_DS.context

	return HttpResponse(template.render(context, request))



# @login_required
def EditPost_DS(request, event_id):
	
	postEdit_DS=Post_EditPost_DS(request,event_id)

	template = loader.get_template('templates_DS/editPost_DS.html')

	context = postEdit_DS.context

	return HttpResponse(template.render(context, request))


##########################################################################################################################################################################################

# @login_required
def DeleteExperience_chart_DS(request, event_id):
	post = Experience_chart.objects.get(pk=event_id)
	if request.user == post.user:
		post.delete()
		# return redirect('Experience_chart_DS')		
		return redirect('index_DS')
	else:
		# return redirect('Experience_chart_DS')	
		return redirect('UserProfile_category_ExperienceList_DS')	


##########################################################################################################################################################################################

# @login_required
def pre_DeleteExperience_chart_DS(request, event_id):
	post = Experience_chart.objects.get(pk=event_id)
	if request.user == post.user:
		# post.delete()
		context={'post':post}
		return render(request, 'pre_DeleteExperience_chart_DS.html', context)		
	else:
		return redirect('index_DS')		

##########################################################################################################################################################################################

# @login_required
def DeletePost_DS(request, event_id):
	post = Post_DS.objects.get(pk=event_id)
	if request.user == post.user:
		post.delete()
		return redirect('index_DS')		
	else:
		return redirect('index_DS')		

##########################################################################################################################################################################################

# @login_required
def pre_DeletePost_DS(request, event_id):
	post = Post_DS.objects.get(pk=event_id)
	if request.user == post.user:
		# post.delete()
		context={'post':post}
		return render(request, 'pre_DeletePost_DS.html', context)		
	else:
		return redirect('index_DS')		

 	

##########################################################################################################################################################################################
# @login_required
def conciseness_DS(request, post_id):
	user = request.user
	post = Post_DS.objects.get(id=post_id)
	current_conciseness = post.conciseness
	conciseness_TRUE = Conciseness_DS.objects.filter(user=user, post=post).count()

	if not conciseness_TRUE:
		like = Conciseness_DS.objects.create(user=user, post=post)
		#like.save()
		current_conciseness = current_conciseness + 1

	else:
		Conciseness_DS.objects.filter(user=user, post=post).delete()
		current_conciseness = current_conciseness - 0

	post.conciseness = current_conciseness
	post.save()

	return HttpResponseRedirect(reverse('PostDetails_DS', args=[post_id]))

##########################################################################################################################################################################################
# @login_required
def relevancy_DS(request, post_id):
	user = request.user
	post = Post_DS.objects.get(id=post_id)
	current_relevancy = post.relevancy
	relevancy_TRUE = Relevancy_DS.objects.filter(user=user, post=post).count()

	if not relevancy_TRUE:
		like = Relevancy_DS.objects.create(user=user, post=post)
		#like.save()
		current_relevancy = current_relevancy + 1

	else:
		Relevancy_DS.objects.filter(user=user, post=post).delete()
		current_relevancy = current_relevancy - 0

	post.relevancy = current_relevancy
	post.save()

	return HttpResponseRedirect(reverse('PostDetails_DS', args=[post_id]))


 

##########################################################################################################################################################################################
#  @login_required
def favorite_DS(request, post_id):
	user = request.user
	post = Post_DS.objects.get(id=post_id)
	profile = Profile_DS.objects.get(user=user)

	if profile.favorites.filter(id=post_id).exists():
		profile.favorites.remove(post)

	else:
		profile.favorites.add(post)

	return HttpResponseRedirect(reverse('PostDetails_DS', args=[post_id]))


##########################################################################################################################################################################################

def tags_DS(request, tag_slug):
	tag = get_object_or_404(Tag_DS, slug=tag_slug)
	posts = Post_DS.objects.filter(tags=tag).order_by('-posted')

	template = loader.get_template('templates_DS/tag_DS.html')

	context = {
		'posts':posts,
		'tag':tag,
	}

	return HttpResponse(template.render(context, request))

